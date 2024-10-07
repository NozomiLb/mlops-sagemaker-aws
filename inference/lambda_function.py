import json
import boto3
import numpy as np
import base64
from sagemaker import runtime
from ..data.preprocess import preprocess_image

def lambda_handler(event, context):
    """
    Lambda handler to interact with SageMaker Endpoint and DynamoDB
    """
    # Get the image from the request
    try:
        body = json.loads(event['body'])
        image_base64 = body['image']
    except (KeyError, json.JSONDecodeError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input. Please provide a valid base64-encoded image.'})
        }

    # Decode the image from base64
    image_data = base64.b64decode(image_base64)
    image_path = '/tmp/uploaded_image.jpg'
    with open(image_path, 'wb') as f:
        f.write(image_data)

    # Preprocess the image
    image = preprocess_image(image_path)
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Call the SageMaker endpoint
    endpoint_name = 'cnn-model-endpoint'
    runtime_client = boto3.client('runtime.sagemaker')
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/x-npy',
        Body=image.tobytes()
    )

    prediction = np.frombuffer(response['Body'].read(), dtype=np.float32)
    predicted_class = int(np.argmax(prediction))

    # Get calorie info from DynamoDB based on predicted class
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CalorieInfo')
    response = table.get_item(Key={'food_class': predicted_class})

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Food class not found'})
        }

    calorie_info = response['Item']
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'predicted_class': predicted_class,
            'calories': calorie_info.get('calories', 'N/A'),
            'food_name': calorie_info.get('food_name', 'Unknown')
        })
    }

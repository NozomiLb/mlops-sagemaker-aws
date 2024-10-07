import boto3
import os

def create_dynamodb_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    
    # Create DynamoDB table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'food_id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'food_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    print(f"Creating DynamoDB table {table_name}...")
    table.wait_until_exists()
    print(f"Table {table_name} created successfully.")
    return table

def add_calorie_data(table, food_items):
    # Add calorie data to DynamoDB
    with table.batch_writer() as batch:
        for food_id, (food_name, calories) in food_items.items():
            batch.put_item(
                Item={
                    'food_id': food_id,
                    'food_name': food_name,
                    'calories': calories
                }
            )
    print("Calorie data added to DynamoDB successfully.")

def get_food_items_from_directory(train_dir):
    food_items = {}
    food_id = 1  # Starting ID for the food items
    
    # Loop through the directories inside the train folder
    for folder_name in os.listdir(train_dir):
        folder_path = os.path.join(train_dir, folder_name)
        
        # Ensure it's a directory
        if os.path.isdir(folder_path):
            # Add food item to dictionary with a dummy calorie count (you can modify this logic)
            food_items[str(food_id)] = (folder_name, 0)  # 0 calories for now
            food_id += 1
            
    return food_items

if __name__ == "__main__":
    table_name = "CalorieInfoTable"
    
    # Define the path to the train folder
    train_dir = '/data/train'
    
    # Get food items from the train directory
    food_items = get_food_items_from_directory(train_dir)
    
    # Create DynamoDB table
    table = create_dynamodb_table(table_name)
    
    # Add food items to the table
    add_calorie_data(table, food_items)
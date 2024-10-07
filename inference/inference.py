import boto3
import tensorflow as tf
from ..data.preprocess import preprocess_image

def load_model():
    s3 = boto3.client('s3')
    bucket_name = 'sagemkr-detect-food'
    prefix = 'subfolder_prefix'
    model_path = 's3://{}/{}/output/cnn_model.h5'.format(bucket_name,prefix)
    s3.download_file('bucket_name', 'subfolder_prefix/output/cnn_model.h5', 'cnn_model.h5')
    model = tf.keras.models.load_model('cnn_model.h5')
    return model

def predict(image_path):
    model = load_model()
    image = preprocess_image(image_path)
    image = image.reshape((1, 224, 224, 3))
    prediction = model.predict(image)
    return prediction

if __name__ == "__main__":
    image_path = "data/test/pizza/8917.jpg"
    prediction = predict(image_path)
    print("Predicted Class:", prediction)

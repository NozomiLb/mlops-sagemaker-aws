import os
import boto3
from model import create_cnn_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_model():
    # Load and preprocess data from S3
    s3 = boto3.client('s3')
    bucket_name = 'sagemkr-detect-food'
    prefix = 'subfolder_prefix'

    # Image Data Generator for Augmentation
    datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)

    train_generator = datagen.flow_from_directory('s3://{}/{}/train'.format(bucket_name, prefix),
                                                  target_size=(224, 224),
                                                  batch_size=32,
                                                  class_mode='sparse',
                                                  subset='training')

    val_generator = datagen.flow_from_directory('s3://{}/{}/test'.format(bucket_name, prefix),
                                                target_size=(224, 224),
                                                batch_size=32,
                                                class_mode='sparse',
                                                subset='validation')

    model = create_cnn_model()

    # Training the model
    model.fit(train_generator, validation_data=val_generator, epochs=10)

    # Save model to S3
    model.save('s3://{}/{}/output/cnn_model.h5'.format(bucket_name,prefix))

if __name__ == "__main__":
    train_model()

# Use an official SageMaker base image with TensorFlow
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-training:2.8.0-cpu-py38-ubuntu20.04

# Install any additional libraries required for your project
RUN pip install --upgrade pip && \
    pip install \
    boto3 \
    pandas \
    tensorflow \
    SageMaker \
    scikit-learn \
    requests \
    matplotlib \
    Pillow

# Copy the training and inference scripts into the container
COPY train.py /opt/ml/code/train.py
COPY inference.py /opt/ml/code/inference.py

# Set environment variables for SageMaker to recognize the script locations
ENV SAGEMAKER_PROGRAM train.py
ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/code/

# Set the entry point for training
ENTRYPOINT ["python", "/opt/ml/code/train.py"]
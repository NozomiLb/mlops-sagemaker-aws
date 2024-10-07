import sagemaker
import boto3
from sagemaker.tuner import HyperparameterTuner, IntegerParameter, CategoricalParameter
from sagemaker.tensorflow import TensorFlow

s3 = boto3.client('s3')
bucket_name = 'sagemkr-detect-food'
prefix = 'subfolder_prefix'

# Define the SageMaker TensorFlow estimator
estimator = TensorFlow(
    entry_point='train.py',
    role='SageMakerRole',
    instance_count=1,
    instance_type='ml.m5.xlarge',
    framework_version='2.4.1',
    py_version='py37',
    hyperparameters={
        'epochs': 10,
        'batch_size': 32
    }
)

# Define the hyperparameter ranges to tune
hyperparameter_ranges = {
    'epochs': IntegerParameter(5, 20),
    'batch_size': IntegerParameter(16, 64),
}

# Create the hyperparameter tuning job
tuner = HyperparameterTuner(
    estimator,
    objective_metric_name='validation:accuracy',
    hyperparameter_ranges=hyperparameter_ranges,
    objective_type='Maximize',
    max_jobs=10,
    max_parallel_jobs=2
)

# Start hyperparameter tuning job
tuner.fit({'train': 's3://{}/{}/train'.format(bucket_name,prefix), 'val': 's3://{}/{}/test'.format(bucket_name,prefix)})
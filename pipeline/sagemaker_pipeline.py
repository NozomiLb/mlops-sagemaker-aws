import sagemaker
from sagemaker.processing import Processor
from sagemaker.workflow.steps import ProcessingStep, TrainingStep, TransformStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.inputs import TrainingInput

role = 'arn:aws:iam::your-account-id:role/sagemaker-execution-role'

# Step 1: Data Processing
processor = Processor(
    role=role,
    image_uri='763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-processing:2.3-cpu-py37-ubuntu18.04',
    instance_count=1,
    instance_type='ml.m5.xlarge'
)

processing_step = ProcessingStep(
    name="DataPreprocessing",
    processor=processor,
    outputs=[sagemaker.processing.ProcessingOutput(source='/opt/ml/processing/output')],
    job_arguments=["--input-data", 's3://your-bucket/data', '--output-dir', '/opt/ml/processing/output']
)

# Step 2: Model Training
training_step = TrainingStep(
    name="ModelTraining",
    estimator=sagemaker.estimator.Estimator(
        role=role,
        image_uri='763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-training:2.3-gpu-py37-ubuntu18.04',
        instance_count=1,
        instance_type='ml.p3.2xlarge',
        hyperparameters={'epochs': 10, 'batch_size': 32},
        output_path='s3://your-bucket/output',
    ),
    inputs={'train': TrainingInput(s3_data='s3://your-bucket/train-data')}
)

# Step 3: Model Evaluation
transform_step = TransformStep(
    name="ModelEvaluation",
    transformer=sagemaker.transformer.Transformer(
        role=role,
        model_name='cnn-model',
        instance_count=1,
        instance_type='ml.m5.xlarge'
    ),
    transform_inputs=TrainingInput(s3_data='s3://your-bucket/test-data')
)

# Step 4: Deployment
deployment_step = TrainingStep(
    name="ModelDeployment",
    estimator=sagemaker.estimator.Estimator(
        role=role,
        model_uri='s3://your-bucket/output/model.tar.gz',
        instance_count=1,
        instance_type='ml.m5.xlarge'
    )
)

# Pipeline definition
pipeline = Pipeline(
    name="MLOpsPipeline",
    steps=[processing_step, training_step, transform_step, deployment_step]
)

if __name__ == "__main__":
    pipeline.upsert(role_arn=role)
    pipeline.start()

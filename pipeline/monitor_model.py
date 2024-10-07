import boto3
from sagemaker.model_monitor import DefaultModelMonitor

session = boto3.Session()
sm_client = session.client('sagemaker')

role = 'arn:aws:iam::your-account-id:role/sagemaker-execution-role'
monitor = DefaultModelMonitor(role=role,
                              instance_count=1,
                              instance_type='ml.m5.xlarge',
                              volume_size_in_gb=30)

# Baseline dataset and endpoint name
baseline_data = 's3://your-bucket/baseline-data'
endpoint_name = 'cnn-model-endpoint'

# Create Monitoring Schedule
monitor.create_monitoring_schedule(
    endpoint_input=endpoint_name,
    output_s3_uri='s3://your-bucket/monitoring-results',
    monitoring_schedule_name='model-monitor-schedule',
    schedule_cron_expression='cron(0 * * * ? *)',
    baseline_dataset_uri=baseline_data
)

print(f"Model monitoring schedule created for endpoint {endpoint_name}.")
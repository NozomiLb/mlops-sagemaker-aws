packages = [
    'boto3', 'tensorflow', 'sklearn', 'numpy', 'pandas', 'requests',
    'bs4', 'sagemaker'
]

for package in packages:
    try:
        __import__(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is NOT installed.")
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence
import boto3

ecr_client = boto3.client('ecr')

repository_name = "my_monitoring_app_repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)
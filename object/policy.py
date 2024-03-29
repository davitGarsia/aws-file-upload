import boto3
s3_client = boto3.client('s3')

def set_object_access_policy(aws_s3_client, bucket_name, file_name):
    response = aws_s3_client.put_object_acl(
        ACL="public-read",
        Bucket=bucket_name,
        Key=file_name
    )
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False


def put_policy():
  lfc = {
    "Rules": [
      {
        "Expiration": {
          "Days": 7
        },
        "ID": "devobjects",
        "Filter": {"Prefix": "dev"},
        "Status": "Enabled"
      }
    ]
  }
  s3_client.put_bucket_lifecycle_configuration(
    Bucket="bucket", LifecycleConfiguration=lfc
  )

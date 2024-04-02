import boto3
import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()


def create_s3_bucket(bucket_name: str, location: str) -> str:
    """
    Creates an S3 bucket in with name `bucket_name` in the specified region.

    Parameters
    ----------
    `bucket_name:`: The name of the S3 bucket as a string that we would like to create.

    `location`: The AWS region (represented as a string) in which we would like to create the S3 bucket.

    Returns
    -------
    The response from the bucket creation, or the error message.
    """

    try:

        # Create an S3 client
        s3 = boto3.client('s3')

        # Create the bucket
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': location  # Specify the region for the bucket
            }
        )

        return response

    except ClientError as e:

        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            return f"Bucket '{bucket_name}' already exists and is owned by you."

        else:
            return f"Error creating bucket: {e}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    # Call the function to create the bucket
    response = create_s3_bucket(
        bucket_name=os.environ['BUCKET_NAME'],
        location='us-west-2'
    )
    print(response)

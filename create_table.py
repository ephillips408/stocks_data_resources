import boto3
import os

from dotenv import load_dotenv

load_dotenv()

def create_table(local = True):
    """
    Creates a DynamoDB table locally for our stocks data.

    Defaults to a table creation on the local installation of DynamoDB for testing. To create the table in AWS,
    set the value of `local` to `False` as the function argument, i.e. `create_table(local = False)`
    """

    if local == True:

      dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id = os.environ['LOCAL_ACCESS_KEY_ID'],
        aws_secret_access_key = os.environ['LOCAL_SECRET_ACCESS_KEY'],
        region_name = "local",
        endpoint_url = "http://localhost:8000" # This makes sure we create the table locally
      )
    
    elif local == False:
      dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id = os.environ['ACCESS_KEY_ID'],
        aws_secret_access_key = os.environ['SECRET_ACCESS_KEY'],
        region_name = os.environ['TABLE_REGION']
      )

    table_creation_resp = dynamodb.create_table(
        TableName = os.environ['TABLE_NAME'],
        KeySchema = [
            {
              'AttributeName': 'pk',
              'KeyType': 'HASH'  # Partition Key
            }
        ],
        AttributeDefinitions = [
            {
              'AttributeName': 'pk',
              'AttributeType': 'S' # string data type
            }
        ],
        BillingMode = 'PAY_PER_REQUEST' # Sets the billing mode to On-Demand
    )

    return table_creation_resp

if __name__ == "__main__":
    response = create_table()
    print (response)
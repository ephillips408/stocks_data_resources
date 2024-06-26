import boto3
import os

from dotenv import load_dotenv

load_dotenv()


def create_table(table_name: str, local=True) -> str:
    """
    Creates a DynamoDB table locally for our stocks data.

    Defaults to a table creation on the local installation of DynamoDB for testing. To create the table in AWS,
    set the value of `local` to `False` as the function argument, i.e. `create_table(local = False)`

    Parameters
    ----------
    `table_name`: `str`
        The name of the table we would like to create 

    `local`: `bool` 
        Determines whether we create a DynamoDB table locally or in AWS. The default value is set to `True`, so a local table will be created. 
        To create a table in AWS, set `local = False`
    """

    if local == True:

        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.environ['LOCAL_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['LOCAL_SECRET_ACCESS_KEY'],
            region_name="local",
            # This makes sure we create the table locally
            endpoint_url="http://localhost:8000"
        )

    elif local == False:
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.environ['ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['SECRET_ACCESS_KEY'],
            region_name=os.environ['TABLE_REGION']
        )

    table_creation_resp = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'pk',
                'KeyType': 'HASH'  # Partition Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'pk',
                'AttributeType': 'S'  # string data type
            },
            {
                'AttributeName': 'symbol',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',  # Sets the billing mode to On-Demand
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'SymbolIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'symbol',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            }
        ],
        Tags=[
            {
                'Key': 'project-name',
                'Value': 'stocks-project'
            }
        ]
    )

    return table_creation_resp


if __name__ == "__main__":
    response = create_table(
        table_name=os.environ['TABLE_NAME'],
        local=False
    )
    print(response)

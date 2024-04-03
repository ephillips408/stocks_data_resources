### DynamoDB Stocks Project

This project makes an API call using the [alphavantago.co](https://www.alphavantage.co/) API, then pushes the cleaned data to a local installation of DynamoDB using AWS Lambda functions. Installation instructions for DynamoDB locally can be found [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html).

This repo will contain useful commands and resource creation for future reference, and the Lambda functions that are used to complete the process.

To begin the process, we will need to first create the resources in AWS. This can be done by runnning the `create_table.py` file, and the `create_s3_bucket.py` file in this repo.

To see how we push the data obtained from the API call to DynamoDB, please see [this repo](https://github.com/ephillips408/lambda_get_stock_data)

To see how we move the data from DynamoDB to a .csv file in S3, please see [this repo](https://github.com/ephillips408/stocks_data_to_s3)
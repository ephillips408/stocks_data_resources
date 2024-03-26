### DynamoDB Stocks Project

This project makes an API call using the [alphavantago.co](https://www.alphavantage.co/) API, then pushes the cleaned data to a local installation of DynamoDB using AWS Lambda functions. Installation instructions for DynamoDB locally can be found [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html).

This repo will contain useful commands and resource creation for future reference, and each Lambda function will receive its own repo. 

There is one work in progress at the moment, and it involves using a Lambda function to pushh data returned from the Alphanvantage API linked above to a locally installed version of DynamoDB. The repo can be found [here](https://github.com/ephillips408/lambda_get_stock_data).
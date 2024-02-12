
# ELT pipeline
## ▶️ Getting started

## part 1

1. Check if you already have Node.js installed. Run this command in your terminal:

```bash
# install requirements (recommended)
pip install requirements.txt
```
2. build .env.dist file

aws_access_key_id = "your access key" <br>
aws_secret_access_key = "your secret key" <br>
bucket_name = "your bucket name" <br>
object_key = "s3 object key" <br>
table_name = "your Table Name" <br>
region = "your cloud region" <br>

3. install your csv or csvs in your S3 bucket 

<h5> data.csv </h5>

4. [build your S3 bucket and insert your data](https://aws.amazon.com/s3/)

5. [build your dynamodb connection and Roles](https://aws.amazon.com/dynamodb/)

6. run Tranform/main.py

## part 2

1. build a lambda function or run directly from Makfile

2. build a dynamodb connection with the lambda function IAM Role

3. connect s3 with lambda IAM Role

4. Run Makefile 

5. test your API


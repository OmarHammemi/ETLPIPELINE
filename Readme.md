
# ELT pipeline
## ▶️ Getting started

## part 1

1. Check if you already have Node.js installed. Run this command in your terminal:

```bash
# install requirements (recommended)
pip install requirements.txt
```
2. build .env.dist file

aws_access_key_id = "your access key" 1. 
aws_secret_access_key = "your secret key" 2.
bucket_name = "your bucket name" 3.
object_key = "s3 object key" 4.
table_name = "your Table Name" 5.
region = "your cloud region" 6.

3. install your csv or csvs in your S3 bucket 

<h5> data.csv </h5>

4. [build your dynamodb connection and Roles](https://aws.amazon.com/dynamodb/)

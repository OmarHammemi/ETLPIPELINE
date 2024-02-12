
# ELT pipeline
## ▶️ Getting started

## part 1

1. Check if you already have Node.js installed. Run this command in your terminal:

```bash
# install requirements (recommended)
pip install requirements.txt
```
2. build .env.dist file

aws_access_key_id = "your access key"
aws_secret_access_key = "your secret key"
bucket_name = "your bucket name"
object_key = "s3 object key"
table_name = "your Table Name"
region = "your cloud region"

3. install your csv or csvs in your S3 bucket 

<h5> data.csv </h5>

4. [build your dynamodb connection and Roles](https://aws.amazon.com/dynamodb/)

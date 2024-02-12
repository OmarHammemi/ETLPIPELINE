
from dotenv import dotenv_values
import boto3
import pandas as pd
from datetime import datetime

class Transform:
    def __init__(self):
        envVars = dotenv_values('.env.dist')
        session = boto3.Session(
                    aws_access_key_id=envVars['aws_access_key_id'],
                    aws_secret_access_key=envVars['aws_secret_access_key'] ,
                    region_name=envVars['region']
                )
        self.bucket_name = envVars['bucket_name']
        self.object_key = envVars['object_key']
        self.dynamodb = session.resource('dynamodb')
        self.tableName=envVars['table_name']
        self.table = self.dynamodb.Table(self.tableName)
        self.s3=session.client('s3')
    def read_csv(self):
        # Download the object from S3 to the local file
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
        data = pd.read_csv(obj['Body'])
        return data
    def putItemToDynamo(self,item_id, item_data):
        table=self.dynamodb.Table(self.tableName)
        table.put_item(
            Item={
                'PK': "ELT",
                'SK': item_id,
                **item_data 
            }
        )
        return "item ADDed to db"
    def transform_data(self):
        data=self.read_csv()
        data_dict = data.to_dict('records')
        for dt in data_dict:
            print(dt)
            self.putItemToDynamo(datetime.now(
            ).strftime("%Y-%m-%d"),dt)
            
            
if __name__ == "__main__":
    transform = Transform()
    transform.transform_data()
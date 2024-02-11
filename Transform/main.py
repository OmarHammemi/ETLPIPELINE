
from dotenv import dotenv_values
import boto3
import pandas as pd
import  psycopg2

class Transform:
    def __init__(self):
        envVars = dotenv_values('.env.dist')
        session = boto3.Session(
                    aws_access_key_id=envVars['aws_access_key_id'],
                    aws_secret_access_key=envVars['aws_secret_access_key'] ,
                    region_name='eu-west-1'
                )
        self.bucket_name = 'elt-pipeline-test'
        self.object_key = 'data.csv'
        self.s3=session.client('s3')
        self.db_host = envVars['db_host']
        self.db_name = envVars['db_name']
        self.db_user = envVars['db_user']
        self.db_password = envVars['db_password']
        self.db_port = envVars['db_port']
    def read_csv(self):
        # Download the object from S3 to the local file
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
        data = pd.read_csv(obj['Body'])
        return data
    def transform_data(self, data):
        conn = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            port=self.db_port
        )
        cursor = conn.cursor()
        data=self.read_csv()
        for _, row in data.iterrows():
            cursor.execute("""
                INSERT INTO your_table_name (column1, column2, ...)
                VALUES (%s, %s, ...);
            """, (row['column1'], row['column2'], ...))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()
        
                
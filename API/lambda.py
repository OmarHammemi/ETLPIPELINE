import json
import boto3
from decimal import Decimal

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'ELT_test'
table = dynamodb.Table(table_name)

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def handler(event, context):
    # Check if the request is a GET method
    if event['httpMethod'] == 'GET':
        # Query DynamoDB for first 10 items
        response = table.scan(Limit=10)
        items = response['Items']
        
        # Convert items to JSON
        json_items = json.dumps(items, default=decimal_serializer)
        
        # Return a successful response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json_items
        }
    else:
        # Return an error response
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Invalid request method'})
        }

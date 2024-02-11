import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'ELT_test'
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        # Check if the request is a GET method
        if event['httpMethod'] == 'GET':
            # Query DynamoDB for first 10 items
            response = table.scan(Limit=10)
            items = response['Items']
            
            # Return a successful response
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps(items)
            }
        else:
            # Return an error response for unsupported methods
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Method not allowed'})
            }
    except Exception as e:
        # Return an error response for any exceptions
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

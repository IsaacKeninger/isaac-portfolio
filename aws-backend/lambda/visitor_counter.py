
# This is the code I used for the AWS Lambda Function

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('VisitorCounterTable')

def lambda_handler(event, context):

    response = table.get_item(Key={'counterID': 'visitorCount'})
    
    current_count = response.get('Item', {}).get('count', 0)

    new_count = current_count + 1

    table.put_item(Item={'counterID': 'visitorCount', 'count': new_count})
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS'
        },
        'body': str(new_count)
    }


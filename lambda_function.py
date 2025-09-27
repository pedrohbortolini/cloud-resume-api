import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

# Função para converter Decimal em int
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError

def lambda_handler(event, context):
    # Incrementa o contador
    response = table.update_item(
        Key={'id': 'visitor'},
        UpdateExpression='ADD visits :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )

    visits = response['Attributes']['visits']

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'https://pedrobortolini.com.br/'
        },
        'body': json.dumps({'visits': visits}, default=decimal_default)  # usa a função de conversão
    }

import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    sns.publish(
        PhoneNumber=event['RecipientNumber'],
        Message=event['Message']
    )
    
    return 'Your SMS has been sent'
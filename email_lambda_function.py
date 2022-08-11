import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source='hodote76@gmail.com',
        Destination={
            'ToAddresses': [
                event['RecipientEmail'],
            ]
        },
        Message={
            'Subject': {
                'Data': 'Welcome to severless sending application'
            },
            'Body': {
                'Text': {
                    'Data': event['Message']
                }
            }
        }
    )
    return 'Email sent!'

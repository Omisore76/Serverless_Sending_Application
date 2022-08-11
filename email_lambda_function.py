import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source='hodote76@gmail.com',
        Destination={
            'ToAddresses': [
                event['destinationEmail'],
            ]
        },
        Message={
            'Subject': {
                'Data': 'Welcome to severless sending application'
            },
            'Body': {
                'Text': {
                    'Data': event['message']
                }
            }
        }
    )
    return 'Email sent!'
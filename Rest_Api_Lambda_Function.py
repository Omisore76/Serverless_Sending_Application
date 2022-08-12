import boto3 

import json

stepfunction=boto3.client('stepfunctions')

def lambda_handler(event, context):
    stepfunction.start_execution(
        stateMachineArn="arn:aws:states:us-east-1:658387634975:stateMachine:MyStateMachine",
        input=event['body']
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"Status": "Instruction sent to the REST API Handler!"},
        )
    }
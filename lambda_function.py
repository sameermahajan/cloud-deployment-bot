import json
import boto3

REGION = 'us-east-1'
AWS_ACCESS_KEY = <your AWS access key>
AWS_SECRET = <your AWS secret>
AMI = 'ami-07d0cf3af28718ef8'
INSTANCE_TYPE = 't2.micro'

def lambda_handler(event, context):
    print('received request: ' + str(event))
    aws_service = event['currentIntent']['slots']['ServiceType']
    instance_type = event['currentIntent']['slots']['InstanceType']
    os = event['currentIntent']['slots']['OS']
    key = event['currentIntent']['slots']['Key']
    print ("aws_service = {} instance_type = {} os = {} key = {}".format(aws_service,
                                                        instance_type,
                                                        os,
                                                        key))
            
    msg = ""
    
    if aws_service.lower() != 'ec2':
        msg = "Unsupported AWS service "
    
    if os.lower() == 'ubuntu':
        ami = 'ami-07d0cf3af28718ef8'
    else:
        msg += "Unsupported operating system "
        
    if instance_type.lower() != "t2.micro":
        msg += "Unsupported instance type "
        
    if msg == "":
        EC2 = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET, region_name=REGION)
    
        instance = EC2.run_instances(
            ImageId=ami,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            InstanceInitiatedShutdownBehavior='terminate',
            KeyName=key
        )
    
        msg = "New instance created {}".format(instance['Instances'][0]['InstanceId'])
    
    print (msg)
    
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": msg
            },
        }
    }
    
    print('response = ' + str(response))
    return response

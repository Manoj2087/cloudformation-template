import boto3
from crhelper import CfnResource

client = boto3.client('autoscaling')
helper = CfnResource()

@helper.create
@helper.update
def enable_instance_protection(event, _):
    # Enable Autoscaling Group instance protection(Scale in) - for ASG
    response = client.update_auto_scaling_group(
        AutoScalingGroupName=event['ResourceProperties']['AutoScalingGroupName'],
        NewInstancesProtectedFromScaleIn=True
    )
    print(response)

@helper.delete
def no_op(_, __):
    pass

def handler(event, context):
    helper(event, context)
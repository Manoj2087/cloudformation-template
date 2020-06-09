import boto3
from crhelper import CfnResource

ecsClient = boto3.client('ecs')
asClient = boto3.client('autoscaling')
helper = CfnResource()

@helper.create
@helper.update
def enable_instance_protection(event, _):
    # Fetch the ASG ARN
    asResponse = asClient.describe_auto_scaling_groups(
        AutoScalingGroupNames=[
            event['ResourceProperties']['AutoScalingGroupName'],
        ]
    )
    autoScalingGroupARN = asResponse[0].AutoScalingGroupARN
    print('autoScalingGroupARN:')
    print(autoScalingGroupARN)

    # Create ECS Cluster provider
    response = ecsClient.create_capacity_provider(
        name=event['ResourceProperties']['Name'],
        autoScalingGroupProvider={
            'autoScalingGroupArn': autoScalingGroupARN,
            'managedScaling': {
                'status': event['ResourceProperties']['ManagedScalingStatus'],
                'targetCapacity': int(event['ResourceProperties']['ManagedScalingTargetCapacity']),
                'minimumScalingStepSize': int(event['ResourceProperties']['ManagedScalingMinimumScalingStepSize']),
                'maximumScalingStepSize': int(event['ResourceProperties']['ManagedScalingMaximumScalingStepSize'])
            },
            'managedTerminationProtection': event['ResourceProperties']['ManagedTerminationProtection']
        }
    )
    print(response)

@helper.delete
def no_op(_, __):
    pass

def handler(event, context):
    helper(event, context)
# Project Title
A cloud formation template that sets up a Script Server.

## Prerequisites
AWS account with permission to run Cloudformation(CF) and delpoy the instances created as part of the CF template

## Deployment
Launch the CF template via AWS Console or CLI

```
# Deploy stack
aws cloudformation create-stack \
--stack-name <stack-name> \
--template-body file://network/2-subnet-network.yaml \
--parameters \
ParameterKey=ProjectName,ParameterValue=<project-name> \
ParameterKey=CidrPrefix,ParameterValue="10.10" \
--on-failure DO_NOTHING \
--region <region>

# Delete stack
aws cloudformation delete-stack \
--stack-name <stack-name>
--region <region>
```


## Versioning
For the versions available, see the
* Version <1.0>  
    Version Features
      - Delpoys the VPC environment with 2 public ,public
       , Internet gateway.
      - Deploy and configure Script Server.
      - Outputs the Script Server public IP   

## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

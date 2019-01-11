# Project Title
A cloud formation template that sets up a Script Server.

## Prerequisites
AWS account with permission to run Cloudformation(CF) and delpoy the instances created as part of the CF template

## Deployment
Launch the CF template via AWS Console or CLI
**Parameters required**
'''
aws cloudformation create-stack \
--stack-name myteststack \
--template-body file://2-subnet-network.yaml \
--parameters \
ParameterKey=ProjectName,ParameterValue=test \
ParameterKey=CidrPrefix,ParameterValue="10.10" \
--on-failure DO_NOTHING \
--region ap-southeast-2
'''


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

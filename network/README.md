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
--region <region>

# Delete stack
aws cloudformation delete-stack \
--stack-name <stack-name> \
--region <region>
```


## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

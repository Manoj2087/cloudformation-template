## Deployment
Launch the CF template via AWS Console or CLI

```
# Deploy/update
aws cloudformation deploy \
--template-file network/2-subnet-network.yml \
--stack-name <stack-name> \
--parameter-overrides \
ProjectName=<project-name> \
CidrPrefixe="10.10" \
--region <region>
```

# Delete stack
```
aws cloudformation delete-stack \
--stack-name <stack-name> \
--region <region>
```


## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

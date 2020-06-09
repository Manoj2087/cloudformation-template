## Deployment
Launch the CF template via AWS Console or CLI

```
# Deploy/update
aws cloudformation deploy \
--template-file ecs-capacity-provider/ecs-capacity-provider-v2.yml \
--stack-name test-ecs-capacity-provider \
--parameter-overrides \
CidrPrefixe="10.10" \
EC2KeyPair="DevOpsPro" \
--capabilities CAPABILITY_IAM \
--region ap-southeast-2


```

# Delete stack
```
aws cloudformation delete-stack \
--stack-name <stack-name> \
--region <region>
```


## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

## Deployment
Launch the CF template via AWS Console or CLI

```
# Deploy/update stack
aws cloudformation deploy \
--template-file ec2-fleet/c2-fleet.yml \
--stack-name <stack-name> \
--region <region>

# Delete stack
aws cloudformation delete-stack \
--stack-name <stack-name> \
--region <region>
```

## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

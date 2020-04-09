## Deployment
Launch the CF template via AWS Console or CLI

```
# Deploy stack
aws cloudformation create-stack \
--stack-name <stack-name> \
--template-body file://ec2-fleet/ec2-fleet.yaml \
--region <region>

# Delete stack
aws cloudformation delete-stack \
--stack-name <stack-name> \
--region <region>
```

## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

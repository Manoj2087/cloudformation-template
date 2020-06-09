## Deploy 2-subnet-network Private and Public subnet
Launch the CF template via AWS Console or CLI

```
# Deploy/update
aws cloudformation deploy \
--template-file public-templates/network/2-subnet-network.yml \
--stack-name 2-subnet-network \
--parameter-overrides \
ProjectName=2-subnet-network \
CidrPrefixe="10.10" \
--region ap-southeast-2

# Delete
aws cloudformation delete-stack \
--stack-name 2-subnet-network \
--region ap-southeast-2

```

## Deploy 2-subnet-network Public subnet only
```
# Deploy/update
aws cloudformation deploy \
--template-file public-templates/network/2-subnet-network-public-only.yml \
--stack-name test2 \
--parameter-overrides \
ProjectName=test2 \
CidrPrefixe="10.10" \
--region ap-southeast-2

# Delete
aws cloudformation delete-stack \
--stack-name test2 \
--region ap-southeast-2
```


## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

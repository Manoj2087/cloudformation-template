# Cloud Formation Templates
This repo has some of the commmonly used cloudformation templates.

## Prerequisites
AWS account with permission to run Cloudformation(CF) and delpoy the instances created as part of the CF template

## Sync template to S3 for Nested stacks
The below command copies all the files in this folder ans subfolders with extention '.yml' to the s3 bucket with public-read object permission.  
```
aws s3 cp . \
s3://<s3-bucket-name> \
--exclude "*" \
--include "*.yml" \
--delete \
--acl public-read \
--recursive \
--region <region>
```

## [Network](/network/README.md)

## [EC2 Fleet](/ec2-fleet/README.md)

## Authors
 **Manoj Balaji Alaghappan**  - Cloud Architect

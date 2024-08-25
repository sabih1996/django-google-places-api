# Deployment

This application is deployed to AWS using ECS and CDK. The infrastructure is defined in the lib/ directory, following best practices of separating concerns for VPC, ECS, and ECR.

### AWS CDK Deployment

- Install AWS CDK:

```
npm install -g aws-cdk
```

- Bootstrap your AWS environment (if not already done):

```
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

- Deploy the infrastructure:


```
cdk deploy
```
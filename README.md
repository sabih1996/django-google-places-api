# Django Google Places API
This project is a Django-based API that integrates with the Google Places API. The application is designed to allow users to search for places, retrieve location data, and interact with the Google Places service via RESTful endpoints. The application is containerized using Docker and deployed on AWS using ECS (Elastic Container Service), with infrastructure managed by AWS CDK (Cloud Development Kit).

## Features
- Google Places API Integration: Fetch and search location data using the Google Places API.
- Django REST Framework: RESTful endpoints for accessing location data.
- AWS Deployment: Infrastructure managed with AWS CDK and deployed on ECS with Fargate.
- Continuous Deployment: Automated CI/CD pipeline using GitHub Actions for deployment to AWS.

## Infrastructure Overview

The application is deployed on AWS with the following architecture:

- Amazon ECS (Fargate): The application runs as a Fargate service in an ECS cluster.
- Amazon ECR: Docker images are built and stored in Amazon ECR (Elastic Container Registry).
- VPC: A custom VPC with subnets and NAT gateways to host the ECS cluster.
- Application Load Balancer (ALB): Manages traffic to the ECS service.
- RDS (Optional): For database management, PostgreSQL can be set up on Amazon RDS.
- AWS CDK: The infrastructure is defined using AWS CDK in Python.

## Prerequisites

- Google Places API Key: Required for Google Places API integration.
- AWS Account: Set up and configured with the AWS CLI.
- Docker: Installed locally for containerization.
- Python 3.8+: Required for local development.
- GitHub Secrets: Ensure you have set the required secrets in your GitHub repository for CI/CD (e.g., AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, ECR_REGISTRY, ECR_REPOSITORY).

## Local Development Setup

1) Clone the repository:
***
```
git clone https://github.com/your-username/django-google-places-api.git
cd django-google-places-api
```
2) Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate
```
3) Install dependencies:
```
pip install -r requirements.txt
```
4) Set up your environment variables. Create a .env file in the root directory with the following:
```
GOOGLE_PLACES_API_KEY=your_google_places_api_key
DJANGO_SECRET_KEY=your_django_secret_key
DATABASE_URL=your_database_url
```
5) Run database migrations:
```
python manage.py migrate
```
6) Start the development server:
```
python manage.py runserver
```

## AWS Infrastructure Setup
This project uses AWS CDK to define and deploy infrastructure on AWS. The following steps will guide you through setting up the infrastructure for deployment.

### Step 1: Install AWS CDK
Ensure that you have the AWS CDK installed globally:
```
npm install -g aws-cdk
```
### Step 2: Bootstrap the AWS Environment
Before deploying, bootstrap your AWS environment:

```
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```
### Step 3: Deploy the Infrastructure
To deploy the infrastructure, use the following command:

```
cdk deploy
```

This will deploy the VPC, ECS cluster, ECR repository, and other necessary AWS resources.

# Step 4: Build and Push Docker Image to ECR
Manually build and push the Docker image to Amazon ECR (Elastic Container Registry):

```
docker build -t your-ecr-repo:latest .
docker tag your-ecr-repo:latest aws_account_id.dkr.ecr.region.amazonaws.com/your-ecr-repo:latest
docker push aws_account_id.dkr.ecr.region.amazonaws.com/your-ecr-repo:latest
```

## GitHub Actions CI/CD Pipeline
This project is configured with GitHub Actions to automate the deployment process. The workflow defined in .github/workflows/deploy.yml will:

1) Build the Docker image.
2) Push the Docker image to ECR.
3) Deploy the new Docker image to the ECS service.

### Setting Up GitHub Secrets
To enable the CI/CD pipeline, you need to add the following secrets to your GitHub repository:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- ECR_REGISTRY: The ECR registry URL.
- ECR_REPOSITORY: The ECR repository name.

## Contact
For any inquiries or issues, feel free to reach out via GitHub issues. Or email me on hafizsabihulhassan1996@gmail.com.
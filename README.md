# **Flask Application with Docker, CI/CD Pipeline, and AWS Deployment**

## **Project Overview**
This project is a basic Flask application that:
- Runs a simple "Hello, World!" route.
- Is containerized using Docker.
- Uses GitHub Actions for CI/CD pipeline to:
  - Run tests using `pytest`.
  - Build and push the Docker image to AWS Elastic Container Registry (ECR).
  - Deploy the Docker image from AWS ECR to an EC2 instance.

## **Project Structure**
```
.
├── src
│   └── app.py               # Flask application (hello world route)
├── Dockerfile               # Docker configuration file for the application
├── tests
│   └── test_app.py          # Pytest test cases
├── .github
│   └── workflows
│       └── ci-cd.yml   # GitHub Actions CI/CD pipeline
├── requirements.txt         # Python dependencies
└── README.md                # Documentation file (this file)
```

## **Requirements**
- Before getting started, ensure the following are installed:
- **Docker**: For containerizing the application.
- **AWS CLI**: For interacting with AWS services (ECR, EC2).
- **GitHub**: A GitHub repository to store and version the code.
- **Pytest**: For testing the Flask application.

### Prerequisites
- AWS Account with ECR and EC2 instances set up.
- Docker installed on local machine.
- GitHub repository set up with code.

## **Flask Application (`src/app.py`)**
- The Flask application serves a simple "Hello, World!" route. 

## **Docker Configuration (`Dockerfile`)**
- The `Dockerfile` is used to containerize the Flask application. It contains the necessary instructions to create a Docker image for the app.

## **Test Configuration (`tests/test_app.py`)**
- The test file is used to ensure the Flask application is working as expected. We use `pytest` to write a simple test case.

## **Requirements File (`requirements.txt`)**
- This file lists all the dependencies needed to run the Flask application.

## **CI/CD Pipeline Configuration (`.github/workflows/ci-cd.yml`)**
- GitHub Actions is used to automate the CI/CD pipeline, which includes:
    Checkout code
    Set up Python
    Install depedencies
    Run tests (optional)
    Build Docker image
    Set up AWS CLI
    Log in to AWS ECR
    Tag Docker image for ECR
    Push Docker image to ECR
    Create .ssh directory (if not present)
    Decode SSH private key
    Add SSH key to SSH agent
    Debug - Check if key file exists
    Deploy to AWS EC2

## **CI/CD Workflow Overview**
- This GitHub Actions workflow automates the testing, building, and deployment of a Flask application to AWS. It is triggered on any push to the `main` branch and consists of the following steps:

### **1. Build Job**

- **Checkout Code**: Retrieves the repository code.
- **Set Up Python**: Installs Python 3.8.
- **Install Dependencies**: Installs project dependencies from `requirements.txt`.
- **Run Tests**: Executes tests using `pytest`.
- **Build Docker Image**: Builds the Docker image for the Flask app.

### **2. Push Docker Image to AWS ECR**

- **Set Up AWS CLI**: Configures AWS CLI with credentials stored in GitHub Secrets.
- **Log in to ECR**: Authenticates Docker to push images to AWS ECR.
- **Tag Docker Image**: Tags the Docker image for AWS ECR.
- **Push Docker Image**: Pushes the tagged image to ECR.

### **3. Deploy to AWS EC2**

- **Set Up SSH**: Configures SSH access using a private key stored in GitHub Secrets.
    # Private key (.pem) to base64 encoded
    - Convert the Private key (.pem) to base64 encoded and store in .txt file (in local)
    command: base64 -i projects.pem | tr -d '\n' > projectPemKey.txt
    - then open the .txt file and copy the whole content and paste in Github cctions 
    secret.

- **Deploy Docker Image**: SSHs into the EC2 instance, pulls the image from ECR, and runs the container on EC2.

### **Secrets Configuration**
Ensure the following secrets are set in GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ACCOUNT_ID`
- `AWS_SSH_KEY` (SSH private key for EC2)
- `AWS_EC2_PUBLIC_IP` (EC2 instance public IP)
These can be configured in the GitHub repository under **Settings > Secrets**.

## **Testing the Application**
- Once deployed on EC2, Check Security group name from EC2 instace details, 
then select that group and edit inbound rules. Then add a Custom TCP with 5000 port and 0.0.0.0/0

Test the application in browser:
```
http://<EC2_PUBLIC_IP>:5000/
```

## **Conclusion**

This project demonstrates how to containerize a simple Flask application using Docker and automate its deployment pipeline using GitHub Actions, AWS ECR, and EC2. The CI/CD pipeline ensures continuous integration by running tests, building the Docker image, and automatically deploying the application to the EC2 instance.

For production usage, consider:
- Adding additional security measures (e.g., SSL, environment variables).
- Using a load balancer and scaling EC2 instances.
- Automating health checks and monitoring.

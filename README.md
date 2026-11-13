# Containerized Application Deployment and Management Using Docker

## Project Overview

This project demonstrates the development, containerization, deployment, and management of a web application using Docker and Docker Compose.

The application is a Visitor Management System (VMS) developed using Python Flask and PostgreSQL. It allows users to register visitors, manage visitor records, and track visitor check-in and check-out details.

The application is containerized using Docker and deployed on an AWS EC2 instance.

## Live Application

**AWS Deployment:** http://16.171.166.103:5001

## Technologies Used

- Python
- Flask
- HTML and CSS
- Docker
- Docker Compose
- PostgreSQL
- Gunicorn
- AWS EC2
- Git and GitHub

## Features

- Application dashboard
- Visitor registration
- Purpose of visit
- Visitor check-in and check-out
- Visitor history
- Search visitor records
- Total visitor count
- Today's visitor count
- PostgreSQL database integration
- Application health check
- Database connectivity check
- Docker containerization
- AWS EC2 deployment

## Project Structure

```text
Containerized-Application-Deployment-Using-Docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── schema.sql
├── .env.example
├── .dockerignore
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Technologies and Architecture

- **Flask:** Handles application logic and visitor management.
- **PostgreSQL:** Stores visitor details and check-in/check-out records.
- **Docker:** Packages the application into containers.
- **Docker Compose:** Manages the web application and database services.
- **Gunicorn:** Runs the Flask application.
- **AWS EC2:** Hosts the deployed application.

## How to Run the Project Locally

### Prerequisites

- Python
- Docker Desktop
- Git

### Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Abhina7736/Containerized-Application-Deployment-Using-Docker.git
```

2. Navigate to the project directory:

```bash
cd Containerized-Application-Deployment-Using-Docker
```

3. Create a `.env` file using `.env.example` as a reference. Configure the required database environment variables.

4. Build and start the containers:

```bash
docker compose up --build -d
```

5. Initialize the PostgreSQL database table:

```bash
docker compose exec -T db psql -U postgres -d dockerdb < schema.sql
```

6. Open the application in your browser:

```text
http://localhost:5000
```

**Note:** The local application port depends on the port mapping configured in `docker-compose.yml`.

## Useful Docker Commands

### View Running Containers

```bash
docker compose ps
```

### View Application Logs

```bash
docker compose logs
```

### Stop Containers

```bash
docker compose down
```

## Health Check Endpoints

- `/health` – Checks whether the application is running.
- `/db-check` – Checks PostgreSQL database connectivity.

## AWS Deployment

The Visitor Management System is deployed on an AWS EC2 Ubuntu instance using Docker and Docker Compose.

- **Cloud Platform:** AWS EC2
- **Operating System:** Ubuntu 24.04 LTS
- **Application Host Port:** 5001
- **Container Port:** 5000
- **Database:** PostgreSQL 16

**Live Application:** http://16.171.166.103:5001

## Future Enhancements

- Automated deployment using CI/CD
- Improved visitor reporting
- User authentication and role management
- Enhanced application security

## Author

**Abhina**

## GitHub Repository

[Containerized Application Deployment and Management Using Docker](https://github.com/Abhina7736/Containerized-Application-Deployment-Using-Docker)

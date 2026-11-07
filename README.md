# Containerized Application Deployment and Management Using Docker

## Project Overview
This project demonstrates how to develop, containerize, deploy, and manage a web application using Docker. It uses Python Flask for the web application and PostgreSQL for database management.

The application includes a Visitor Management System that allows users to register visitors and manage their check-in and check-out details.

## Technologies Used
- Python
- Flask
- Docker
- Docker Compose
- PostgreSQL
- HTML and CSS
- AWS EC2 (Cloud Deployment)

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
- Docker containerization

## Project Structure

```text
Docker Project/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## How to Run the Project

### Prerequisites
- Python
- Docker Desktop
- Git

### Run Using Docker Compose

1. Open the project folder in VS Code.
2. Make sure Docker Desktop is running.
3. Configure the database environment variables in the `.env` file.
4. Open the terminal in the project folder.
5. Run:

```bash
docker compose up --build -d
```

6. Open the browser and visit:

```text
http://localhost:5000
```

## Useful Docker Commands

Stop containers:

```bash
docker compose down
```

View running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs
```

## Future Enhancements
- Cloud deployment using AWS EC2
- Automated deployment using CI/CD
- Improved visitor reporting and management

## Author
Abhina
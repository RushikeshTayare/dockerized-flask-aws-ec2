# Dockerized Flask Application Deployment on AWS EC2

## Project Overview

This project demonstrates the deployment of a Python Flask web application inside a Docker container on an AWS EC2 instance.

The application is containerized using Docker to ensure a consistent runtime environment and simplify deployment. The Dockerized application is hosted on an Amazon EC2 Linux instance and made accessible through the EC2 public IP address.

## Architecture

```text
             User / Browser
                    |
                    v
             Internet
                    |
                    v
             AWS EC2 Instance
                    |
                    v
               Docker
                    |
                    v
             Flask Container
                    |
                    v
             Flask Web App
```

## Technologies Used

- **AWS EC2:** Cloud server hosting
- **Amazon Linux:** Server operating system
- **Docker:** Application containerization
- **Python:** Application programming language
- **Flask:** Python web framework
- **Git & GitHub:** Version control and source code management
- **Linux:** Server administration and command-line operations

## Project Features

- Flask web application deployment
- Docker image creation
- Container-based application execution
- AWS EC2 cloud hosting
- Linux server configuration
- GitHub-based source code management
- Application access through EC2 public IP

## Project Structure

```text
docker-aws-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Deployment Steps

### 1. Launch AWS EC2 Instance

- Launch an Amazon Linux EC2 instance.
- Configure the security group.
- Allow SSH (Port 22).
- Allow application traffic (Port 5000 or your configured application port).

### 2. Install Docker

```bash
sudo yum update -y
sudo yum install docker -y
```

Start and enable Docker:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Add the EC2 user to the Docker group:

```bash
sudo usermod -aG docker ec2-user
```

Reconnect to the EC2 instance for group changes to take effect.

### 3. Clone the Repository

```bash
git clone https://github.com/RushikeshTayare/dockerized-flask-aws-ec2.git
```

Navigate into the project:

```bash
cd dockerized-flask-aws-ec2
```

### 4. Build Docker Image

```bash
docker build -t flask-aws-app .
```

### 5. Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-container flask-aws-app
```

### 6. Verify Container

```bash
docker ps
```

View application logs:

```bash
docker logs flask-container
```

### 7. Access the Application

Open your browser:

```text
http://YOUR-EC2-PUBLIC-IP:5000
```

Replace `YOUR-EC2-PUBLIC-IP` with your actual EC2 public IP address.

## Docker Commands Used

| Command | Purpose |
|---|---|
| `docker build` | Build Docker image |
| `docker images` | List Docker images |
| `docker run` | Start a container |
| `docker ps` | List running containers |
| `docker logs` | View container logs |
| `docker stop` | Stop a container |
| `docker rm` | Remove a container |
| `docker rmi` | Remove an image |

## Key Learning Outcomes

- Understanding Docker containerization.
- Deploying Flask applications on AWS EC2.
- Managing Docker containers on Linux.
- Configuring AWS security groups and network access.
- Working with Git and GitHub for project version control.
- Understanding cloud-based application deployment.

## Future Improvements

- Automate deployment using CI/CD pipelines.
- Configure Nginx as a reverse proxy.
- Enable HTTPS using SSL certificates.
- Push Docker images to Amazon ECR.
- Implement monitoring and logging.
- Deploy using Docker Compose.

## Author

**Rushikesh Tushar Tayare**

Cloud Computing & DevOps Learner

- GitHub: https://github.com/RushikeshTayare
- Portfolio: https://rushikeshtayare.in

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.

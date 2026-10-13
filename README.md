# 🚀 Python Multibranch CI/CD Pipeline with Jenkins & Docker

A hands-on DevOps project demonstrating how to build, containerize, publish, and deploy a Python Flask application using **Jenkins Multibranch Pipelines, Docker, GitHub, and Docker Hub**.

The project uses separate Git branches to represent different deployment environments: Development, Staging, and Production.

## 📌 Project Overview

This project automates the application delivery workflow. Whenever a branch is built by Jenkins, the pipeline checks out its source code, builds a Docker image, pushes the image to Docker Hub, and deploys the application as a Docker container.

It demonstrates practical CI/CD concepts, environment separation, image versioning, credential management, and troubleshooting real container startup failures.

## 🏗️ Architecture

```text
                    GitHub Repository
                   /        |        \
                 dev       stg       prod
                  |         |          |
                  +---------+----------+
                            |
                    Jenkins Multibranch
                         Pipeline
                            |
                    Checkout Source Code
                            |
                     Build Docker Image
                            |
                     Push to Docker Hub
                            |
                    Run Docker Container
                            |
              +-------------+-------------+
              |             |             |
            Dev App       Staging App   Production App
           Port 5001       Port 5002      Port 5003
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web application framework |
| Git & GitHub | Source control and branch management |
| Jenkins | CI/CD automation |
| Jenkinsfile | Pipeline as Code |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Linux | Container execution environment |

## 🌿 Branch Strategy

The project uses three deployment branches:

| Branch | Environment | Host Port | Container Port |
|---|---|---:|---:|
| `dev` | Development | 5001 | 5000 |
| `stg` | Staging | 5002 | 5000 |
| `prod` | Production | 5003 | 5000 |

Each environment runs in its own Docker container, allowing the environments to be managed independently.

**Note:** These host ports are explicitly configured in the current Jenkinsfile. They are not dynamically allocated.

## ⚙️ CI/CD Workflow

The Jenkins pipeline consists of the following stages:

### 1. Clone Repository
Checks out the source code from the branch being built using Jenkins SCM integration.

### 2. Configure Branch
Identifies the branch through Jenkins' `BRANCH_NAME` environment variable and configures the corresponding host port.

### 3. Build Docker Image
Builds a Docker image using the repository's Dockerfile.

Example image tag:

```bash
docker build -t hello-python-nti-dev:2 .
```

### 4. Push Docker Image
Authenticates with Docker Hub using Jenkins credentials, tags the image, and pushes it to the registry.

Example image reference:

```text
ahmed00farouk/hello-python-nti:dev-2
```

The image tag includes the branch name and Jenkins build number to distinguish versions.

### 5. Run Docker Container
Removes the previous container for the same branch and starts a replacement container using the newly built image.

Example:

```bash
docker rm -f hello-python-nti-dev
docker run -d \
  --name hello-python-nti-dev \
  --restart unless-stopped \
  -p 5001:5000 \
  hello-python-nti-dev:2
```

The container listens on port `5000`, while the host exposes it on the configured environment port.

## 🐳 Docker Image

The application is packaged into a Docker image based on `python:3.12-slim`.

The Dockerfile installs the dependencies from `requirements.txt`, copies the application source, exposes port `5000`, and starts the Flask application.

## 🔐 Credentials and Security

Docker Hub authentication is handled through Jenkins credentials rather than hardcoding credentials in the Jenkinsfile.

The pipeline uses Jenkins' `withCredentials` mechanism and `--password-stdin` for Docker authentication.

**Security considerations:**
- Never commit passwords, access tokens, or other secrets to GitHub.
- Use Jenkins credentials with appropriate access restrictions.
- Protect production deployments with approvals and restricted permissions.
- Use a credential helper or an appropriate secure credential-management strategy where needed.

## 🧪 Validation and Troubleshooting

The project included practical troubleshooting of a container startup failure.

**Issue:** The container entered a `Restarting (1)` state.

**Root cause:** Markdown code-fence text (` ```python `) was accidentally included in `hello.py`, causing a Python `SyntaxError`.

**Resolution:**
1. Inspected container logs using `docker logs`.
2. Identified the syntax error in the application source.
3. Corrected the source code in GitHub.
4. Rebuilt and redeployed the application through Jenkins.
5. Verified the running container and application response.

Useful diagnostic commands:

```bash
# Inspect running containers
docker ps

# Inspect application logs
docker logs hello-python-nti-dev

# Inspect container details
docker inspect hello-python-nti-dev

# Test the development application locally
curl http://localhost:5001
```

## 🚀 Access the Applications

When the containers are running and the host ports are reachable:

- Development: `http://localhost:5001`
- Staging: `http://localhost:5002`
- Production: `http://localhost:5003`

If Docker runs inside a separate virtual machine, use the VM's reachable IP address instead of `localhost`.

## 📚 Key Learning Outcomes

Through this project, I practiced:

- Designing a Jenkins Multibranch Pipeline.
- Managing development, staging, and production branches.
- Implementing Pipeline as Code with a `Jenkinsfile`.
- Building and tagging Docker images.
- Publishing versioned images to Docker Hub.
- Managing credentials securely through Jenkins.
- Automating container replacement and deployment.
- Troubleshooting failed containers through logs and runtime inspection.
- Understanding the difference between a successful image build and a successfully running application.

## 🔮 Potential Improvements

- Add automated unit and integration tests.
- Introduce health checks and deployment verification.
- Implement dynamically assigned host ports or a reverse proxy.
- Add approval gates before production deployment.
- Integrate image vulnerability scanning.
- Add rollback strategies and deployment notifications.

## 👨‍💻 Author

**Ahmed Farouk**

DevOps & Cloud Engineering Learner

GitHub: [@drift3](https://github.com/drift3)

Docker Hub: [ahmed00farouk](https://hub.docker.com/u/ahmed00farouk)

---

*Built as a hands-on project to practice CI/CD automation, containerization, and branch-based application delivery.*

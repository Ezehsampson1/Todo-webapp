# Dockerized Python Todo Webapp
A simple Todo List web Application built with Python and Flask, containerized with Docker. This project demonstrates foundational DevOps practices: writing production-conscious application code, building lean Docker images, and documenting infrastructure clearly.

# What This Project Demonstrates
- Writing a minimal, functional Python/Flask web app
- Structuring a Dockerfile with layer caching in mind
- Keeping container images small and secure
- Writing clear documentation [Readme.md]

 ## Tech Stack
```
| Tool           | Purpose                      | Version  |
|---------------|------------------------------|----------|
| Python        | Application language         | 3.12     |
| Flask         | Lightweight web framework    | 3.0.3    |
| Docker        | Containerization             | 24+      |
```


## Project Structure
```
 Todo-webapp/
|---app/
|   |---app.py
|   |---requirements.txt
|   |---templates/
|       |---index.html
|---Dockerfile
|---.dockerignore
|---README.md
```



## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running
- That's it. No Python installation required on your machine


## Getting Started

### 1. Clone the repository 
git clone https://github.com/Ezehsampson1/Todo-webapp

cd Todo-webapp

### 2. Build the Docker image
docker build -t todo-webapp:v1 .

### 3. Run the container
docker run -p 5000:5000 Todo-webapp:v1

### 4. Open the app
visit http://localhost:5000 

Author:: Engr Sampson Ezeh


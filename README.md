# Task Manager

A web-based Task Management application built using **FastAPI, SQLite, HTML, CSS, JavaScript, and Docker**.

The project allows users to create, view, update, and delete tasks through REST API endpoints, with a simple web dashboard.

## Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Containerization:** Docker
- **API Testing:** Swagger UI
- **Version Control:** Git and GitHub

## Features

- Create new tasks.
- View all saved tasks.
- Update existing tasks.
- Mark tasks as completed or pending.
- Delete tasks.
- Store task information using SQLite.
- Serve frontend files using FastAPI.
- Run the application inside a Docker container.
- Persist database data using Docker Volumes.

## Project Structure

text
task-manager/
│
├── app/
│   ├── main.py
│   └── database.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── tests/
│   └── test_main.py
│
├── data/
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md


## Installation and Setup

### 1. Clone the Repository

bash
git clone YOUR_REPOSITORY_URL

bash
cd task-manager

### 2. Create a Virtual Environment

bash
python -m venv .venv


Activate it on Windows:

powershell
.venv\Scripts\activate

### 3. Install Dependencies

bash
pip install -r requirements.txt

### 4. Run the Application

bash
uvicorn app.main:app --reload

Open your browser:

- Dashboard: http://127.0.0.1:8000/
- API Documentation: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Running with Docker

### 1. Build the Docker Image

bash
docker build -t task-manager .

### 2. Create a Docker Volume

bash
docker volume create task-manager-data


### 3. Run the Container

bash
docker run -d -p 8000:8000 --name task-manager-container -v task-manager-data:/app/data task-manager


### 4. Access the Application

http://127.0.0.1:8000/

### 5. Check Running Containers

bash
docker ps


### 6. Check Docker Volumes

bash
docker volume ls


Docker Volumes provide persistent storage for the SQLite database, allowing database data to survive container removal and recreation.

## Future Improvements

- Implement automated testing with Pytest.
- Set up CI/CD using GitHub Actions.
- Automate Docker image builds.
- Deploy the application to a cloud platform.
- Improve the dashboard UI and user experience.

## Learning Objectives

This project is also a hands-on learning experience covering:

- Backend development with FastAPI.
- REST API development and CRUD operations.
- SQLite database integration.
- Frontend and backend communication.
- Docker image creation and containerization.
- Persistent storage using Docker Volumes.
- Git and GitHub workflows.
- CI/CD automation.



Built as a hands-on project to learn Backend Development and DevOps.

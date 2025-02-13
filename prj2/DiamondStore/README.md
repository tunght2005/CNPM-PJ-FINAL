# Diamond Store Project

## Prerequisites
- Docker
- Docker Compose

## Setup and Installation

1. Clone the repository

2. Build and run the containers

3. Run migrations

4. Create superuser

Database Configuration
The MySQL database is configured with:

Database name: PNJ
Username: root
Password: yourpassword
Host: db
Port: 3306
Accessing the Application
Main application: http://localhost:8000
Admin panel: http://localhost:8000/admin
Common Commands
Start containers: docker-compose up -d
Stop containers: docker-compose down
View logs: docker-compose logs -f
Access Django shell: docker-compose exec web python [manage.py](http://_vscodecontentref_/0) shell
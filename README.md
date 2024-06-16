<<<<<<< HEAD Table of Contents

1. Prerequisites
2. Installation
3. Running the Application
4. API Documentation
5. Endpoints
   
Prerequisites:

Before you begin, ensure you have met the following requirements:
->Python 3.7+
->Pip (Python package installer)
->Git (optional, if you want to clone the repository)
Installation

Clone the repository:
git clone https://github.com/yourusername/your_project.git

Or download the ZIP file from GitHub and extract it.

Navigate into the project directory:
cd your_project

Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:
On Windows:

=> venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Running the Application:
To run the FastAPI application, follow these steps:

1. Ensure you are in the project directory where main.py is located.

2. Run the FastAPI server using uvicorn:

    uvicorn app.main:app --reload

app.main:app refers to main module in the app directory and app is the name of the FastAPI instance.
--reload enables automatic reloading of the server when code changes.
Open your web browser and go to http://127.0.0.1:8000 to access the API documentation (Swagger UI).
API Documentation

Once the application is running, you can view the API documentation and interact with the endpoints:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Endpoints

Authentication:
Register: POST /auth/register
Login: POST /auth/login


User Management:
Get current user: GET /users/me/
Update current user: PUT /users/me/
Delete current user: DELETE /users/me/


Account Management:
Add money to account: POST /account/add 
Remove money from account: POST /account/remove 
Get account balance: GET /account/balance
Get transaction history: GET /account/history

=======

Project
3bd8905eda38963d3698b5fddecac7000693c55c

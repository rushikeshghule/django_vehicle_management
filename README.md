
# Vehicle Management System
This is a CRUD (Create, Read, Update, Delete) application for vehicle management. The system allows users to manage information about vehicles, such as their number, type, model, and description.

## Features
User authentication (register and login)
User authorization (different levels of access for super admin, admin, and user)
Vehicle information management (CRUD operations)
IP filtering (restriction to specific IP addresses)
## Prerequisites
Python 3.x
Django 3.x
Bootstrap 4.x
## Steps
### 1) Open the terminal or command prompt
### 2)Change the directory to the root folder of the project, "django_vehicle_management-master", using the following command:
cd django_vehicle_management-master
### 3)Change the directory to the inner folder "vehiclemanagementproject" using the following command:
cd vehiclemanagementproject
### 4)Install the required packages by running the following command:
pip install -r requirements.txt
### 5)Apply the migrations using the following command:
python manage.py makemigrations
python manage.py migrate
### 6)Run the development server using the following command:
python manage.py runserver

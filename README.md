# Restaurant Management System (Django)

A simple Restaurant Management System built using Django. This project helps manage menu items, orders, customers, and basic restaurant operations.

---

## 📌 Features
- User authentication (Login/Register)
- Menu management
- Order management
- Admin dashboard
- Basic restaurant workflow handling

---

## 🧰 Requirements
Make sure you have the following installed:

- Python (3.8 or above recommended)
- pip (Python package manager)
- Git (optional but recommended)

---

## 📁 Project Setup Guide

Follow these steps carefully to run the project on your local machine.

---

## 1️⃣ Clone the Repository or Simply Download Zip and extract

```bash
git clone https://github.com/prakashtaz0091/Restaurant-Management-System
cd restaurant-management-system
```
OR
[Click here to download](https://github.com/prakashtaz0091/Restaurant-Management-System/archive/refs/heads/master.zip)

## 2️⃣ Create Virtual Environment (venv)

A virtual environment is an isolated Python environment that allows you to install dependencies separately for each project.

▶ Create venv
```bash
python -m venv venv
```
This creates a folder named venv in your project directory.

## 3️⃣ Activate Virtual Environment
🪟 Windows (CMD)
```bash
venv\Scripts\activate
```
🪟 Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```
🍎 macOS / 🐧 Linux
```bash
source venv/bin/activate
```
After activation, you should see (venv) in your terminal.

## 4️⃣ Install Dependencies
What is requirements.txt?

requirements.txt is a file that contains all Python packages required for the project. Instead of installing packages one by one, you install everything at once using this file.

▶ Install packages
```bash
pip install -r requirements.txt
```
## 5️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## 6️⃣ Create Superuser (Admin Panel)
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

## 7️⃣ Run the Development Server
```bash
python manage.py runserver
```
Now open your browser and visit:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/

## 🧠 Notes for Students
1. Always activate venv before running the project

2. Install new packages using pip install package-name and update requirements:
```bash
pip freeze > requirements.txt
```
3. Never upload venv/ to GitHub

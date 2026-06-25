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

---
# ESC/POS Printer Testing Using Docker

This guide explains how to install Docker and run the following images:

* `gilbertfl/escpos-netprinter:3.2`
* `ghcr.io/lezram/escpos-emulator`

---

# Prerequisites

Verify Docker is installed:

```bash
docker --version
docker compose version
```

---

# 1. Install Docker

## Linux (Ubuntu/Debian)

Install Docker Engine, Docker CLI, and Compose plugin.

### Add Docker Repository

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker

```bash
sudo apt update

sudo apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

### Start Docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

### Optional: Run Without sudo

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Verify

```bash
docker run hello-world
```

---

## macOS

Docker Engine cannot run natively on macOS because Docker containers require a Linux kernel.

Install a lightweight Docker-compatible runtime:

### Option 1: Colima (Recommended)

Install prerequisites:

```bash
brew install docker docker-compose colima
```

Start Colima:

```bash
colima start
```

Verify:

```bash
docker version
docker run hello-world
```

### Option 2: Rancher Desktop

Install:

```bash
brew install --cask rancher
```

Enable Docker compatibility mode and verify:

```bash
docker version
```

---

## Windows

Docker Engine cannot run directly on Windows without a Linux VM.

### Option 1: Docker CLI + WSL2 + Docker Engine (Recommended)

Install WSL2:

```powershell
wsl --install
```

Install Ubuntu from Microsoft Store.

Inside Ubuntu:

```bash
sudo apt update

# Follow Linux installation instructions above
```

Verify:

```bash
docker version
docker run hello-world
```

### Option 2: Rancher Desktop

Install using Winget:

```powershell
winget install RancherDesktop.RancherDesktop
```

Enable Docker CLI support.

Verify:

```powershell
docker version
```

> Note: Docker Desktop is intentionally omitted from this guide because it is significantly heavier than the alternatives above.

---

# 2. Pull Required Images

```bash
docker pull ghcr.io/lezram/escpos-emulator
docker pull gilbertfl/escpos-netprinter:3.2
```

Verify:

```bash
docker images
```

---

# 3. Start ESC/POS Emulator

Run the emulator container:

```bash
docker run -d \
  --name escpos-emulator \
  -p 8080:8080 \
  -p 9100:9100 \
  ghcr.io/lezram/escpos-emulator
```

Verify:

```bash
docker ps
```

---

# 4. Access Emulator UI

Open:

```text
http://localhost:8080
```

The web interface displays received ESC/POS print jobs.

---

# 5. Test Printing

Send plain text:

```bash
echo "Hello ESC/POS" | nc localhost 9100
```

Send ESC/POS commands:

```bash
printf "\x1B\x40Hello World\n\n\n" | nc localhost 9100
```

Refresh the emulator UI to view output.

---

# 6. Run Network Printer Container

```bash
docker run -d \
  --name escpos-netprinter \
  gilbertfl/escpos-netprinter:3.2
```

Verify:

```bash
docker ps
```

---

# 7. Docker Compose Example

Create a file named `docker-compose.yml`.

```yaml
services:
  escpos-emulator:
    image: ghcr.io/lezram/escpos-emulator
    container_name: escpos-emulator
    ports:
      - "8080:8080"
      - "9100:9100"

  escpos-netprinter:
    image: gilbertfl/escpos-netprinter:3.2
    container_name: escpos-netprinter
    depends_on:
      - escpos-emulator
```

Start:

```bash
docker compose up -d
```

View status:

```bash
docker compose ps
```

Stop:

```bash
docker compose down
```

---

# 8. Logs

View emulator logs:

```bash
docker logs escpos-emulator
```

View printer logs:

```bash
docker logs escpos-netprinter
```

Follow logs:

```bash
docker logs -f escpos-emulator
```

---

# 9. Cleanup

Stop containers:

```bash
docker stop escpos-emulator escpos-netprinter
```

Remove containers:

```bash
docker rm escpos-emulator escpos-netprinter
```

Remove images:

```bash
docker rmi \
  ghcr.io/lezram/escpos-emulator \
  gilbertfl/escpos-netprinter:3.2
```

---

# Troubleshooting

## Check Running Containers

```bash
docker ps -a
```

## Check Open Ports

Linux/macOS:

```bash
lsof -i :8080
lsof -i :9100
```

Windows:

```powershell
netstat -ano | findstr 8080
netstat -ano | findstr 9100
```

## Test Connectivity

```bash
nc -vz localhost 9100
```

Expected output:

```text
Connection to localhost 9100 port [tcp/*] succeeded
```

## Check Docker Status

```bash
docker info
```

If Docker is not running, start the runtime (Docker Engine, Colima, Rancher Desktop, etc.) and retry.

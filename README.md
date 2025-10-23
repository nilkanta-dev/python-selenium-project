# Selenium Automation Framework

A complete end-to-end Selenium test automation framework built using **Python**, **Pytest**, **Allure**, **Selenium Grid**, and **Docker Compose** — designed for scalability, maintainability, and CI/CD integration via **Jenkins**.

---

## Overview

This project automates the test cases of [automationexercise.com](https://automationexercise.com) using a **Page Object Model (POM)** design.  
It supports **local**, **remote (Selenium Grid)**, and **CI/CD pipeline** executions.  
The framework is containerized with **Docker Compose**, making it easy to spin up a full test environment with Jenkins and Selenium Grid nodes.

---

## Key Features

- **Page Object Model (POM)** – clean separation between test logic and UI interactions.  
- **Pytest** – simple, modular, and powerful testing framework.  
- **Allure Reports** – visually rich test reporting with detailed logs, screenshots, and metrics.  
- **Selenium Grid Integration** – parallel test execution across browsers (Chrome, Firefox).  
- **Docker Compose Support** – run Jenkins, Selenium Hub, and standalone browser nodes via containers.  
- **Jenkins Pipeline** – includes a `Jenkinsfile` to automate test execution and reporting.  
- **Chrome DevTools Protocol (CDP)** – used for capturing performance metrics, network mocking, and offline testing.  

---

## Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3.x** | Core language |
| **Selenium** | Browser automation |
| **Pytest** | Test framework |
| **Allure** | Test reporting |
| **Selenium Grid** | Distributed test execution |
| **Docker & Docker Compose** | Container orchestration |
| **Jenkins** | CI/CD automation |
| **CDP (Chrome DevTools Protocol)** | Network and performance control |

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/nilkanta-dev/python-selenium-project.git
cd python-selenium-project
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run tests

```bash
pytest -v
```

### Run tests with allure

```bash
pytest -v --alluredir=reports
allure serve reports
```

### Run with Docker Compose

```bash
docker compose up -d
```

### License

```bash
This project is licensed under the MIT License.
```

### Author

**Nilkanta@33**<br>
Full-Stack Python Developer





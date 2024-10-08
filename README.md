# Personal Portfolio Website

This is a personal portfolio website built using Django. It showcases various projects, skills, job experiences, education, interests, and certificates.

## Live Link
[Live Project Link](https://arshia1212.eu.pythonanywhere.com/)

## Features
- **Projects**: Display a list of projects with details such as name, description, source link, live link, and status.
- **Skills**: Showcase skills with name, description, and logo.
- **Job Experience**: List job experiences with company name, position, start date, and end date.
- **Education**: Display educational background with university name, degree, start date, and end date.
- **Interests**: List personal interests with name and description.
- **Certificates**: Showcase certificates with name and certificate link.

## Technologies Used
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
- ![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
- ![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/serene1212/portfolio-website.git
    cd personal_portfolio
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```bash
    cp sample.env .env
    # Edit the .env file to add your settings
    ```

5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Running Tests
This project is implemented with Test-Driven Development (TDD). To run the tests, use the following command:
```bash
python manage.py test

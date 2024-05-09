# International Conference on Science, Infrastructure Technology, and Regional Development (ICoSITeR) 2021 Website

[![Build Status](https://img.shields.io/travis/user/repo.svg)](https://travis-ci.org/user/repo)
> This project has been discontinued because the event have passed
## Description

The International Conference on Science, Infrastructure Technology, and Regional Development (ICoSITeR) 2021 Website serves as the digital hub for the annual international conference organized by the Institut Teknologi Sumatera (ITERA). It was meticulously crafted to facilitate seamless communication, efficient information dissemination, and smooth participant registration processes.

## Installation

To install and run this project locally, follow these steps:

### Installation Steps:

1. **Install Python:**
   - If Python is not already installed on your system, download and install it from the [official Python website](https://www.python.org/).

2. **Install MySQL Database Server:**
   - Download and install MySQL Community Server from the [official MySQL website](https://dev.mysql.com/downloads/mysql/).

3. **Clone This Repository:**
    - Clone this project to your machine
      ```bash
      git clone https://github.com/enricojoe/icositer2020.git
      ```

4. **Install All Dependencies:**
   - Install all dependencies that needed in this web from requirements.txt:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run Migrations:**
   - Navigate to your Django project directory and run database migrations to create database tables:
     ```bash
     python website_icositer/manage.py migrate
     ```

6. **Start Development Server:**
    - Start the Django development server:
      ```bash
      python manage.py runserver
      ```

7. **Access the website:**
    - After successfully run the server, the website can access at `http://localhost:3306`

## Features

- Information Platform: The website acts as a centralized information hub, providing updates and insights on the conference's progress and activities.
- Participant Registration: Participants can easily register their works and submissions through the intuitive user interface.
- Backend Framework: Powered by Django, a robust and scalable backend framework renowned for its flexibility and security.
- Frontend Styling: Utilizes Bootstrap for frontend styling, ensuring a responsive and visually appealing user experience across devices.
- Database Management: Utilizes MySQL for efficient data storage and retrieval, enabling seamless management of user inputted data and files.
- CRUD Functionality: Allows users to perform Create, Read, Update, and Delete operations on submitted data, ensuring flexibility and control.
- Informational Post Management: Enables CRUD operations on informational post content, empowering administrators to efficiently manage and update conference-related information.

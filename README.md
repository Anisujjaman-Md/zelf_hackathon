# Zelf Hackathon

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Requirements

- Python 3.12
- Django 5.0
- Postgres 16

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Anisujjaman-Md/zelf_hackathon.git
    cd zelf_hackathon
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

    - For macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Configuration

1. Configure Database

    Make a copy of .env.example as .env

## Usage

Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

``` 
    Content List : POST /api/zelf/content-list
    Statistics : POST /api/zelf/statistics
```
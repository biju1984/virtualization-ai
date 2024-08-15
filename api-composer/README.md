# API Composer

This project is an API Composer tool that uses OpenAI to generate API specifications based on user input. The generated specifications can be refined and saved to a database for further use.

## Project Structure

```
api-composer/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── base_handler.py
│   │   │   ├── openai_handler.py
│   │   │   ├── refine_prompt_handler.py
│   │   │   ├── save_specification_handler.py
│   │   │   ├── ...
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging_config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── specification.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── api_schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_service.py
│   │   ├── prompt_service.py
│   │   ├── ...
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   ├── validators.py
│   ├── main.py
│   ├── healthcheck.py
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│       ├── ...
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   ├── test_services.py
│   ├── ...
├── .env
├── alembic.ini
├── requirements.txt
├── README.md
```

## Setup

1. Create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the environment variables in a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
DB_TYPE=postgresql
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name
MONGO_URI=your_mongodb_uri
SQLALCHEMY_DATABASE_URL=your_sqlalchemy_database_url
```

4. Run the database migrations:

```bash
alembic upgrade head
```

5. Start the application:

```bash
uvicorn app.main:app --reload
```

## Usage

- Access the API at `http://localhost:8000/api`.
- Use the provided endpoints to generate, refine, and save API specifications.

## Testing

Run the tests:

```bash
pytest
```

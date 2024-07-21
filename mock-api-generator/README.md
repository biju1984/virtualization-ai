# Virtualization.ai

Virtualization.ai is a commercial-grade application that allows users to create API mocks using natural language processing. The application leverages OpenAI's GPT-3 to generate API specifications, provides versioning, and publishes mock APIs that can be accessed via dynamic, user-friendly URLs.

## Features

- **Natural Language Processing**: Generate API specifications from natural language descriptions.
- **API Specification Management**: Create, retrieve, update, and version API specifications.
- **Publishing**: Publish mock APIs with dynamic URLs.
- **Mock Server**: Serve mock responses based on the published API specifications.
- **User Authentication**: Secure user authentication and management.

## Project Structure

```plaintext
.
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── published_api.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   ├── services.py
│   │   ├── utils.py
│   │   └── version.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── celery_config.py
│   │   ├── config.py
│   │   ├── logging_config.py
│   │   ├── scheduler.py
│   │   └── security.py
│   ├── events.py
│   ├── main.py
│   ├── middleware.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── gpt3.py
│   │   ├── openai_integration.py
│   │   ├── published_api.py
│   │   └── version.py
│   ├── schemas
│   │   ├── published_api.py
│   │   └── version.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── api_service.py
│   │   ├── gpt_service.py
│   │   ├── openai_service.py
│   │   └── user_service.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_routes.py
│   │   └── test_services.py
│   └── utils
│       ├── __init__.py
│       ├── helpers.py
│       └── validators.py
├── docs
│   ├── api_documentation.md
│   ├── architecture.md
│   ├── release_notes.md
│   └── setup_guide.md
├── infra
│   ├── ci_cd
│   │   ├── github_actions.yml
│   │   └── gitlab_ci.yml
│   ├── docker
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   └── init_db.sh
│   ├── k8s
│   │   ├── configmap.yaml
│   │   ├── deployment.yaml
│   │   ├── ingress.yaml
│   │   └── service.yaml
│   ├── scripts
│   │   ├── backup.sh
│   │   ├── health_check.sh
│   │   └── restore.sh
│   └── terraform
│       ├── main.tf
│       ├── outputs.tf
│       ├── provider.tf
│       └── variables.tf
├── project-root
└── requirements.txt

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Docker (for containerization)
- OpenAI API Key

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/mock-api-generator.git
    cd mock-api-generator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    DATABASE_URL=postgresql://user:password@localhost/dbname
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run database migrations**:
    ```bash
    alembic upgrade head
    ```

6. **Start the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

### Running Tests

To run the tests, use the following command:
```bash
pytest

## Usage

1. **Register a new user**:
    ```http
    POST /register
    {
        "username": "testuser",
        "password": "password"
    }
    ```

2. **Create an API specification**:
    ```http
    POST /api_specifications
    {
        "name": "Visa Installment Plan",
        "description": "API for Visa installment plans",
        "request_structure": {
            "accountOrCardIdPresent": true,
            "accountReference": "string",
            "additionalParams": {},
            "eppProvider": "string",
            "partnerMerchantReferenceID": "string",
            "tokenizedCard": {
                "cardId": "string",
                "cardToken": "string",
                "cardType": "string"
            },
            "transactionAmount": 0,
            "transactionCurrency": "string"
        },
        "response_structure": {
            "installmentPlans": [
                {
                    "planId": "string",
                    "provider": "string",
                    "terms": "string",
                    "interestRate": 0,
                    "monthlyPayment": 0,
                    "totalAmount": 0
                }
            ],
            "status": "string"
        }
    }
    ```

3. **Publish the API**:
    ```http
    POST /publish_api
    {
        "api_spec_id": 1
    }
    ```

4. **Test the mock API**:
    ```http
    GET /api/visa-installment-plan
    ```

## Documentation

- [API Documentation](docs/api_documentation.md)
- [Architecture](docs/architecture.md)
- [Setup Guide](docs/setup_guide.md)
- [Release Notes](docs/release_notes.md)

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) before making any contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the GPT-3 API
- FastAPI for the web framework
- SQLAlchemy for ORM
- PostgreSQL for the database

## Contact

For any questions or feedback, please reach out to us at contact@example.com.

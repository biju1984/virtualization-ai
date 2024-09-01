from app.models.database import Base
from app.models.user import User
from app.models.project import Project
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.models.project import Project
import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# Import your models here so that Alembic can detect them

# Alembic Config object, which provides access to values within the .ini file
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Metadata object for 'autogenerate' support
target_metadata = Base.metadata

# Set up the SQLAlchemy URL from environment variable
sqlalchemy_url = os.getenv('SQLALCHEMY_DATABASE_URL')
if sqlalchemy_url is None:
    raise ValueError(
        "The environment variable 'SQLALCHEMY_DATABASE_URL' is not set.")
config.set_main_option('sqlalchemy.url', sqlalchemy_url)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel

# Ensure the app code is discoverable
sys.path.append(os.getcwd())

# Import your metadata
from apps.models import target_metadata

config = context.config

# 1. PULL FROM YOUR ENV
# Your env has: POSTGRES_URL=postgresql+asyncpg://admin:password@postgres:5432/nucleus_db
raw_url = os.getenv("POSTGRES_URL")

if raw_url:
    # 2. CONVERT ASYNC TO SYNC
    # Alembic needs psycopg2 to run migrations.
    sync_url = raw_url.replace("asyncpg", "psycopg2")
    
    # 3. INJECT INTO CONFIG
    # This replaces the %(POSTGRES_URL)s placeholder in alembic.ini
    config.set_main_option("sqlalchemy.url", sync_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Ensure the 'nucleus' schema exists
        connection.execute("CREATE SCHEMA IF NOT EXISTS nucleus;")
        
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            version_table_schema="nucleus",
            include_schemas=True
        )

        with context.begin_transaction():
            context.run_migrations()

# Standard offline/online check
if context.is_offline_mode():
    # Setup for offline if needed
    pass
else:
    run_migrations_online()
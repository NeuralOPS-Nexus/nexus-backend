import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, text
from alembic import context

# Ensure the app code is discoverable
sys.path.append(os.getcwd())

# 1. IMPORT YOUR NEW METADATA (From our SQLAlchemy 2.0 Base)
from apps.models import target_metadata

config = context.config

# 2. PULL FROM YOUR ENV
raw_url = os.getenv("POSTGRES_URL")

if raw_url:
    # Alembic needs psycopg2 (sync) even if the app uses asyncpg
    sync_url = raw_url.replace("asyncpg", "psycopg2")
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
        # 1. CREATE BOTH SCHEMAS (nucleus for core, history for logs)
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS nucleus;"))
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS history;"))
        connection.commit() 
        
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            version_table_schema="nucleus", # Keep migration history in the core schema
            include_schemas=True,           # Tell Alembic to scan both schemas
        )

        with context.begin_transaction():
            context.run_migrations()
            
if context.is_offline_mode():
    # Setup for offline if needed
    pass
else:
    run_migrations_online()
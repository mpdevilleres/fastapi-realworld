# Add base directory to PYTHONPATH
# ------------------------------------------------
import sys
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent
sys.path.append(str(env_path))
# ------------------------------------------------

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app import models
from app.config import SQLALCHEMY_DATABASE_URL

config = context.config
fileConfig(config.config_file_name)

target_metadata = models.Base.metadata


def run_migrations_offline():
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    config_dict = config.get_section(config.config_ini_section)
    config_dict['sqlalchemy.url'] = SQLALCHEMY_DATABASE_URL

    connectable = engine_from_config(
        config_dict,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

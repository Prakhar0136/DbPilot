import pytest
from app.database.connection import check_db_connection


def test_database_connection():
    """Verify that PostgreSQL is reachable via check_db_connection."""
    assert check_db_connection() is True
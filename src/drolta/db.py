"""Drolta SQLite Database Wrappers.

The way that Drolta wraps database instances is adapted from Pandas.

References:
- https://github.com/pandas-dev/pandas/blob/main/pandas/io/sql.py
"""

import sqlite3
from contextlib import contextmanager
from typing import Any, Optional


class SQLiteDatabase:
    """Manages a sqlite database connection."""

    __slots__ = ("conn",)

    conn: sqlite3.Connection
    """The connection to the database."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        super().__init__()
        self.conn = conn

    @contextmanager
    def run_transaction(self):
        """Execute a transaction on the database."""

        cur = self.conn.cursor()
        try:
            yield cur
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise
        finally:
            cur.close()

    def drop_table(self, table_name: str) -> None:
        """Drop the given table if it exists."""
        self.execute(f"DROP TABLE IF EXISTS {table_name};")

    def get_row_count(self, table_name: str) -> int:
        """Get the number of rows in a table."""
        if self.table_exists(table_name):
            cursor = self.conn.cursor()

            cursor.execute(f"""
                SELECT COUNT(*) FROM {table_name};
            """)

            row_count = cursor.fetchone()[0]

            cursor.close()

            return row_count

        # Raise key error because no table was found with the given name
        raise KeyError(table_name)

    def table_exists(self, table_name: str) -> bool:
        """Return True if a table exists with the given name."""
        cursor = self.conn.cursor()

        cursor.execute("""
            WITH all_tables AS (
                SELECT name FROM sqlite_master WHERE type='table'
                UNION
                SELECT name FROM sqlite_temp_master WHERE type='table'
            )
            SELECT *
            FROM all_tables
            WHERE name = ?;
        """, (table_name,))

        exists = cursor.fetchone() is not None

        cursor.close()

        return exists

    def execute(self, sql: str, params: Optional[tuple[Any, ...]] = None) -> None:
        """Execute an operation on the database.

        Parameters
        ----------
        sql: str
            A SQL expression.
        params: tuple of Any, optional
            Parameters to pass to the SQL expression.
        """
        with self.run_transaction() as cur:
            if params:
                cur.execute(sql, params)
            else:
                cur.execute(sql)

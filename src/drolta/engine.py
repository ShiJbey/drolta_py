"""Drolta Query Engine."""

from __future__ import annotations

import sqlite3
from typing import Any, Optional

from drolta.db import SQLiteDatabase
from drolta.interpreter import DroltaResult, DroltaInterpreter


class QueryEngine:
    """
    A QueryEngine manages user-defined content and handles queries to SQLite.
    """

    __slots__ = ("_interpreter",)

    _interpreter: DroltaInterpreter

    def __init__(self, conn: sqlite3.Connection) -> None:
        self._interpreter = DroltaInterpreter(SQLiteDatabase(conn))

    def execute_script(self, drolta_script: str) -> None:
        """Load rules and aliases from a Drolta script.

        Parameters
        ----------
        drolta_script : str
            Drolta script text containing rule and alias definitions.
        """

        self._interpreter.execute_script(drolta_script)

    def query(
        self,
        drolta_query: str,
        bindings: Optional[dict[str, Any]] = None,
    ) -> DroltaResult:
        """Query the SQLite database and return a cursor to the results.

        Parameters
        ----------
        drolta_query : str
            Text defining a Drolta query.
        conn: sqlite3.Connection
            A sqlite3 Connection object.
        bindings: dict[str, Any]
            Bindings of query variables to values.

        Returns
        -------
        DroltaResult
            The result of the query.
        """

        return self._interpreter.query(drolta_query, bindings)

"""Drolta Data Classes.

"""

from __future__ import annotations

import dataclasses

from drolta.ast import ExpressionNode


@dataclasses.dataclass(slots=True)
class RuleData:
    """A Drolta query rule."""

    name: str
    params: list[tuple[str, str]]
    where_expressions: list[ExpressionNode]


@dataclasses.dataclass(slots=True)
class EngineData:
    """Holds all the data managed by the engine."""

    aliases: dict[str, str] = dataclasses.field(default_factory=dict)
    rules: dict[str, RuleData] = dataclasses.field(default_factory=dict)
    temp_table_names: list[str] = dataclasses.field(default_factory=list)

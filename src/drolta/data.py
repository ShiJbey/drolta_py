"""Drolta Data Classes.

"""

from __future__ import annotations

import dataclasses
from typing import Optional

from drolta.ast import (
    ExpressionNode,
    GroupByExpression,
    LimitExpression,
    OrderByExpression,
)


@dataclasses.dataclass(slots=True)
class ResultVariable:
    """A query rule result variable."""

    var_name: str
    aggregate_name: str = ""
    alias: str = ""

    def __str__(self):
        final_str = self.var_name

        if self.aggregate_name:
            final_str = f"{self.aggregate_name}({final_str})"

        if self.alias:
            final_str = f'{final_str} AS "{self.alias}"'

        return final_str


@dataclasses.dataclass(slots=True)
class RuleData:
    """A Drolta query rule."""

    name: str
    result_vars: list[ResultVariable]
    where_expressions: list[ExpressionNode]
    order_by: Optional[OrderByExpression]
    group_by: Optional[GroupByExpression]
    limit: Optional[LimitExpression]


@dataclasses.dataclass(slots=True)
class EngineData:
    """Holds all the data managed by the engine."""

    aliases: dict[str, str] = dataclasses.field(default_factory=dict)
    rules: dict[str, RuleData] = dataclasses.field(default_factory=dict)

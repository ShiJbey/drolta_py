# Drolta: A SQLite Query Engine for Python

![Package Version badge](https://img.shields.io/pypi/v/drolta)
![Supported Python Versions badge](https://img.shields.io/pypi/pyversions/drolta)
![License badge](https://img.shields.io/pypi/l/drolta)
![Monthly downloads badge](https://img.shields.io/pypi/dm/drolta)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

Drolta is an experimental SQLite query engine for wiring more simplified, composable, and declarative queries using a logic programming-inspired syntax. Drolta was initially developed to simplify querying social simulation data generated by NPC interactions in simulation-focused narrative games. SQL, while powerful, is not the most user-friendly language for beginners. We found it challenging to determine how to properly join tables when searching for complex patterns that need to match relationship patterns with specific event sequences. Additionally, we found that SQL queries could quickly become unwieldy and difficult to understand
as more tables and common table expressions were added.

Drolta was developed to simplify this process and provide an alternative to raw SQL that is more accessible to a broader audience of game designers. Drolta pulls inspiration from logic programming languages and technologies like [Prolog](https://en.wikipedia.org/wiki/Prolog), [Datomic](https://docs.datomic.com/datomic-overview.html),
and [TED](https://github.com/ianhorswill/TED). It abstracts away the complexities of joining tables, allowing users to focus on specifying what variables they care about and how they should match (unify) within the query. The result is a query expression that is much more concise and legible than the raw SQL equivalent.

> [!NOTE]
> This is an experimental project. There will be bugs, and potentially breaking changes between feature-level releases. If there is enough interest in Drolta, I may invest more time into producing a stable API. Feel free to try it in your projects. Open a new GitHub issue if you find bugs or unexpected behavior. Thank you for trying Drolta.

## Table of Contents

- [Drolta: A SQLite Query Engine for Python](#drolta-a-sqlite-query-engine-for-python)
  - [Table of Contents](#table-of-contents)
  - [📖 Documentation](#-documentation)
    - [Why Drolta?](#why-drolta)
    - [Installation](#installation)
    - [Getting Started](#getting-started)
    - [Design Philosophy](#design-philosophy)
    - [Queries](#queries)
    - [Predicates](#predicates)
    - [Rules](#rules)
    - [Table/Rule Aliases](#tablerule-aliases)
    - [Output Variable Aliases](#output-variable-aliases)
    - [Filter Statements](#filter-statements)
      - [Comparison Filtering](#comparison-filtering)
      - [Membership filtering](#membership-filtering)
    - [NULL Checking](#null-checking)
    - [AND-Statements](#and-statements)
    - [OR-Statements](#or-statements)
    - [NOT-Statements](#not-statements)
    - [ORDER BY](#order-by)
    - [GROUP BY](#group-by)
    - [LIMIT](#limit)
    - [Aggregation Functions](#aggregation-functions)
    - [Comments](#comments)
  - [💢 Troubleshooting](#-troubleshooting)
    - [OperationalError: database is locked](#operationalerror-database-is-locked)
  - [🧪 Running Unit Tests](#-running-unit-tests)
  - [🎨 Syntax Highlighting Support](#-syntax-highlighting-support)
  - [🏆 Ports and Applications](#-ports-and-applications)
  - [🧱 Editing the Parser](#-editing-the-parser)
  - [📦 Packaging](#-packaging)
  - [🤝 License](#-license)

## 📖 Documentation

### Why Drolta?

Drolta was designed to help game designers work with character data within
simulation-driven emergent narrative games. So, simulation games like Crusader Kings,
Civilization, World Box, Dwarf Fortress, etc. Drolta was developed to help with my
dissertation research on story sifting. It helps you look for arbitrarily complex
patterns in characters' social connections or event histories. Drolta is a good
alternative to SQL.

The easiest way to demonstrate the benefit of Drolta is with an example. Below are two
examples of the same query. This query was used to inspect data
from [Minerva](https://github.com/ShiJbey/minerva), a storyworld simulation that
simulates families competing for power and land. The query is intended to find pairs of
characters who are rivals, half-siblings, and serve as the heads of their respective
family/clan. Minerva is all about inter-family conflicts like this.

The first version of the query is written in Drolta. The second version is written in
pure SQL. Notice the Drolta version's conciseness and how easy it is to understand its
intentions compared to the SQL version. While the pure SQL version has its benefits,
Drolta's syntax is more accessible to new users. The query engine performs all necessary joins, variable unification, and filtering. Drolta is not a replacement for SQL, but it makes it easier
to write queries.

**Drolta Query:**

```plaintext
FIND
    ?c0, ?c1
WHERE
    family_head(head_id=?c0, end_date=NULL)
    family_head(head_id=?c1, end_date=NULL)
    (?c0 != ?c1)
    relation(character_id=?c0, target_id=?c1, relation_type="rival")
    relation(character_id=?c1, target_id=?c0, relation_type="rival")
    half_siblings(character_a=?c0, character_b=?c1)
LIMIT
    10;
```

**SQL Query:**

```sql
SELECT DISTINCT
    c0.uid as c0,
    c1.uid as c1
FROM
    characters c0,
    characters c1,
    families f0
WHERE
 (
    (
        EXISTS (
            SELECT
                1
            FROM
                family_heads fh
            WHERE
                fh.head = c0.uid
                AND fh.family = f0.uid
                AND fh.end_date = NULL
        )
        AND EXISTS (
            SELECT
                1
            FROM
                family_heads fh
            WHERE
                fh.head = c1.uid
                AND fh.family = f0.uid
                AND fh.end_date = NULL
        )
    )
    AND EXISTS (
        WITH
            Rivals AS (
                SELECT
                    r1.character_id AS character_a_uid,
                    r1.target_id AS character_b_uid
                FROM
                    relations r1
                JOIN relations r2 ON
                (
                    r1.character_id = r2.target_id
                    AND r2.target_id = r1.character_id
                    AND r1.relation_type = "Rival"
                    AND r2.relation_type = "Rival"
                )
            )
        SELECT
            1
        FROM
            Rivals
        WHERE
            character_a_uid = c0.uid
            AND character_b_uid = c1.uid
    )
    AND EXISTS (
        WITH
            HalfSiblings AS (
                SELECT
                    s.character_id AS sibling1_uid,
                    s.sibling_id AS sibling2_uid
                FROM
                    siblings s
                    JOIN characters c1 ON s.character_id = c1.uid
                    JOIN characters c2 ON s.sibling_id = c2.uid
                WHERE
                (
                    c1.biological_father = c2.biological_father
                    AND c1.mother != c2.mother
                )
                OR (
                    c1.mother = c2.mother
                    AND c1.biological_father != c2.biological_father
                )
            )
        SELECT
            1
        FROM
            HalfSiblings
        WHERE
            sibling1_uid = c0.uid  AND sibling2_uid = c1.uid
    )
) AND c0.uid != c1.uid
LIMIT
    10;
```

### Installation

This package can be installed from PyPI.

```bash
pip install drolta
```

You can test the installation by printing the current drolta version in the Python REPL. Depending on when you install drolta, the version should be greater than or equal to the one printed below.

```bash
$ python3

>>> import drolta
>>> drolta.__version__
0.4.1
```

### Getting Started

You can a getting started sample in this Google Colab Notebook. This sample contains data based on characters from HBO's House of the Dragon Series.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ShiJbey/drolta_py/blob/main/samples/getting_started.ipynb)

Alternatively, the same sample code can be found [here](./samples/getting_started.py).

### Design Philosophy

Drolta has three design goals:

1. **Readability** - Users should be able to easily understand the intent of a query
2. **Declarative Syntax** - Queries should be more about what you want to find and less
   about how to find it.
3. **Reuse and Composition** - Users should be able to reuse query logic to compose
   larger queries.

Drolta is not focused on being the most performant query engine. Every abstraction has a
cost. However, it does aim to be an accessible alternative to raw SQL.

### Queries

Queries are the main focus of Drolta. They enable users to search for information within
the database. Drolta's query engine is an alternative to executing queries in raw SQL.

**Example queries:**

```plaintext
FIND
    ?siblingId, ?siblingName
WHERE
    PaternalHalfSiblings(x=?adam_id, x=?siblingId)
    character(id=?character_id, name="Addam")
    character(id=?siblingId, name=?siblingName)
ORDER BY ?siblingId;
```

Queries have two required parts: a `FIND`-clause and a `WHERE`-clause. It may also have
additional statements following the WHERE clause to help with sorting and limiting
output size (see [GROUP BY](#group-by), [ORDER BY](#order-by), and [LIMIT](#limit)).

The `FIND`-clause always goes first and signals the start of the query. The find-clause
contains all variables output by the query and their aliases if provided. The output
variable aliases differ from [rule/predicate aliases](#tablerule-aliases). They are used to give
alternate column names to the query output. Otherwise, the column names will match the
variable names without the leading '?'.

Variables in drolta are identifiers with a leading '?' (question mark). For example,
`?character_id`. Variable names may not start with a number and may only contain
letters, numbers, and underscores.

**Examples of valid variable names:**

```plaintext
?id
?family_id
?name
?a_b_c_123
?_x
```

**Examples of invalid variable names:**

```plaintext
apple
?
?123
?family-id
?character&house
```

When writing a query, the goal is to find values in the database that hold true across
all predicates, rules, and filters within the where-clause. This process is
called [variable unification](https://en.wikipedia.org/wiki/Unification_(computer_science)).
Instead of performing variable assignments, like one would do in a language like Java (
Example: `int x = 10;`), users specify where variables are used, and the query engine
ensures that results bound to those variables are valid. In this way, Drolta is more
similar to a logic programming language.

### Predicates

Predicates are treated as base facts about the world. Each predicate corresponds
one-to-one with a table in your database. If you would like to change the predicate
name, use an [alias](#tablerule-aliases). Each column of a table corresponds to one of the
parameters that can be bound by the predicate. Users cannot create new predicates except
by creating new database tables. Alternatively, users can define new [rules](#rules) to
take advantage of existing predicates.

Let's use the `characters` table from the [Getting Started](#getting-started) sample as
an example. Inside SQLite, you would have something like the following:

| id  | name     | house     | sex | life_stage | is_alive |
| --- | -------- | --------- | --- | ---------- | -------- |
| 1   | Rhaenyra | Targaryen | F   | Adult      | 1        |
| 2   | Laenor   | Velaryon  | M   | Adult      | 1        |
| 3   | Harwin   | Strong    | M   | Adult      | 1        |
| 4   | Jacaerys | Targaryen | M   | Teen       | 1        |
| ... | ...      | ...       | ... | ...        | ...      |

You can access this table using the `character` predicate and setting any of the column
names equal to a variable or value. For example, the following query uses the predicate
for characters in a query to get all characters that belong to House Targaryen. The
predicate binds their IDs and names to the `?character_id` and `?name` variables while
also performing a minor filter on the 'house' column.

```plaintext
FIND
    ?character_id,
    ?name
WHERE
    characters(id=?character_id, name=?name, house="Targaryen")
```

### Rules

Rules are used to define reusable queries that are treated like predicates within other
rules and queries. Rules have two parts: a `DEFINE` clause and a `WHERE` clause. The
`DEFINE`- clause is where users specify the name of the rule and the variables output by
the rule. The `WHERE` clause is the same as with queries. It is where all calls to
predicates, rules, and filters are placed.

Rules are loaded into the query engine by placing them inside a Drolta script and
loading the script content with the `QueryEngine.execute_script(...)` method.

Currently, rules may only have one definition (unlike Prolog). Redefining a rule will
overwrite any pre-existing definition.

Below is an example of a rule for finding characters in a game who are paternal
half-siblings (they share the father but not the same mother).

```plaintext
DEFINE
    PaternalHalfSiblings(?x, ?y)
WHERE
    relation(from_id=?x, to_id=?x_bf, type="BiologicalFather")
    relation(from_id=?y, to_id=?y_bf, type="BiologicalFather")
    relation(from_id=?x, to_id=?x_m, type="Mother")
    relation(from_id=?y, to_id=?y_m, type="Mother")
    (?x_m != ?y_m);
```

### Table/Rule Aliases

Aliases allow users to refer to tables and rules by alternative names. This feature is
mainly used to create aliases for SQLite table names since Prolog generally uses
singular nouns while SQL tables use plural nouns. Since Drolta pulls design inspiration
from Prolog, singular nouns generally read better than plural.

In the example below, perhaps we have a database of information about non-player
characters in a video game. We want to reference the `characters` database table using
an alias.

Aliases must be defined in a drolta script and loaded into the query engine using the
`QueryEngine.execute_script(...)` method.

```plaintext
ALIAS characters AS character;
```

Later in your script, you can use this alias when defining rules.

```plaintext
ALIAS characters AS character;

DEFINE adult(?x) WHERE character(uid=?x, age>18);
```

### Output Variable Aliases

To help with readability, output variables for queries and rules may also have aliases. The aliases specified after the variable and may be used with [aggregation functions](#aggregation-functions) to supply more meaningful names. These aliases would then be used when (1) calling a rule within a query or (2) getting the names of the columns in the final query result.

Below is an example of a rule using an alias for house size. Notice we use the size parameter when calling the rule instead of `?character_id`, and we also alias `house_id` to `id`.

```plaintext
RULE
    HouseSize(?house_id AS id, COUNT(?character_id) AS size)
WHERE
    characters(id=?character_id, house_id=?house_id)
GROUP BY ?house_id
ORDER BY ?size DESC;

--

FIND
    ?house_id, ?house_size
WHERE
    HouseSize(id=?house_id, size=?house_size)
    (?house_size < 4)
```

### Filter Statements

Filters are how users specify constraints on variable values in the output. For example,
filters would help to check if a character is over a given age or if they belong to one
of a set of noble houses. Drolta supports comparison filters and list membership checks.
Filters can be chained together with [AND](#and-statements) and [OR](#or-statements) to
create sophisticated constraints.

#### Comparison Filtering

Drolta supports the following comparison operators:

- `=`: Checks if two values are equivalent (Example: `(?age = 32)`)
- `!=`: Checks if two value are not equivalent (Example: `(?age != 32)`)
- `<`: Checks if a value is less than another (Example: `(?age < 32)`)
- `>`: Checks if a value is greater than another (Example: `(?age > 32)`)
- `<=`: Checks if a value is less than or equal to another (Example: `(?age <= 32)`)
- `>=`: Checks if a value is greater than or equal to another (Example: `(?age >= 32)`)

The value to the left of the operator must always be a variable. The value to the right
of the operator can be a number, text, or another variable.

#### Membership filtering

Membership filtering uses the `IN` keyword to check if a variable's value is within a
given list of values, or `NOT IN` to check if a value is absent from a list. The list cannot contain variables. Also, the data type of all the
values in the list should be the same (all integers, floats, or strings).

The filter statement below will pass if the `?house` value is equal to any of the house
names within the provided list.

```plaintext
(?house IN ["Targaryen", "Velaryon", "Lannister"])
```

### NULL Checking

Sometimes, you may want to check if a value is missing or NULL within the database. The
`NULL` keyword can be used within predicates, rules, and filters to check for null
values.

The following example code shows how to check for null values in a predicate/rule. This
predicate would bind all characters that do not belong to a house because their house
value is not present.

```plaintext
character(id=?character_id, house=NULL)
```

The following code does the same as the previous example, but it uses a filter instead
of passing NULL directly to the `character` predicate.

```plaintext
character(id=?character_id, house=?house)
(?house = NULL)
```

### AND-Statements

**Syntax:**

```plaintext
(<filter_statement> AND <filter_statement>)
```

The `AND` keyword is used between filter conditions to signal that both filters (on the
left and right sides) must hold true for the entire filter to pass.

**Example:**

The example code below is a query that uses the `AND` keyword to check that characters
returned by the query are older than 32 and belong to House Belmont.

```plaintext
FIND
    ?character_id, ?age
WHERE
    character(id=?character_id, age=?age, house=?house)
    ((?age > 32) AND (?house = "Belmont"));
```

### OR-Statements

**Syntax:**

```plaintext
(<filter_statement> OR <filter_statement>)
```

The `OR` keyword is used between filter conditions to signal that one or both filter
statements must hold true for the entire filter to pass.

**Example:**

The example code below is a query that uses the `OR` keyword to check that characters
returned by the query belong to either House Targaryen or House Belmont.

```plaintext
FIND
    ?character_id, ?house
WHERE
    character(id=?character_id, house=?house)
    ((?house = "Targaryen") OR (?house = "Belmont"));
```

### NOT-Statements

**Syntax for Filters:**

```plaintext
NOT <filter_statement>
```

**Syntax for Predicates/Rules:**

```plaintext
NOT <predicate or rule>
```

The `NOT` keyword can be used with predicates, rules, and filters. It has different
semantics depending on whether it is used with a filter statement versus a
predicate/rule. When used with a filter statement, it inverts the result of the
condition. So, `(NOT (?age > 32))` is equivalent to `(age <= 32)`.

When `NOT` is used with a predicate or rule, it causes the predicate/rule to act like a
filter, removing any variable values returned by the predicate/rule. Just like filters,
predicates and rules preceded by `NOT` cannot be the first statement within a WHERE
clause because they need something to filter.

**Example:**

Below is an example of `NOT` being used with a rule. In the query, we use `NOT` to
remove all results from the query where the characters belong to the same house. You can
assume that we have rules named `FromSameHouse` and `HalfSiblings` that we defined when
creating the database.

```plaintext
FIND
    ?x, ?y
WHERE
    character(id=?x)
    character(id=?y)
    HalfSiblings(character_a=?x, character_b=?y)
    NOT FromSameHouse(character_a=?x, character_b=?y);
```

### ORDER BY

**Syntax:**

```plaintext
ORDER BY <output_column> [ASC | DESC] [NULLS FIRST | NULLS LAST], ...
```

`ORDER BY` is a statement that tells Drolta to order rows according to one of a query's
output variables (or its alias). `ORDER BY` is borrowed directly from SQL. It is
optional but should be placed after the `WHERE` statement. `ORDER BY` can be used in any
order with `GROUP BY`. Rows can be ordered in ascending order or descending order depending on if ASC or DESC is supplied. By default ASC is used if not specified. Additionally, users can specify if rows with NULL values should come first or last in the ordering using `NULLS FIRST` or `NULLS LAST`.

**Example:**

Get a table of character names and life stages, then order the rows alphabetically by
name.

```plaintext
FIND
    ?name,
    ?life_stage
WHERE
    characters(name=?name, life_stage=?life_stage)
ORDER BY ?name;
```

### GROUP BY

**Syntax:**

```plaintext
GROUP BY <output_column> [, <output_column_1>, ...]
```

`GROUP BY` is a statement that tells Drolta to group rows according to one of a query's
output variables (or its alias). `GROUP BY` is borrowed directly from SQL. It is
optional but should be placed after the `WHERE` statement. `GROUP BY` can be used in any
order with `ORDER BY`. You can specify that items be grouped by more than one column by supplying 2 or more variable names, separated by commas.

**Example:**

Get a table of character names and life stages, then group the rows by life stage (
Child, Teen, Adult, Senior).

```plaintext
FIND
    ?name,
    ?life_stage
WHERE
    characters(name=?name, life_stage=?life_stage)
GROUP BY ?life_stage;
```

### LIMIT

**Syntax:**

```plaintext
LIMIT <integer> [OFFSET <integer>]
```

`LIMIT` tells the query to limit the result to a given number of rows. This should be
the last statement in your query if you choose to use it. It is helpful for keeping
output sizes small if needed. You can optionally supply an offset to tell the query to return results starting at a given row and counting down. By default the offset is implicitly set to 0 to start at the first row.

**Example:**

Get a table of character names and life stages, and limit the result to the first five
rows.

```plaintext
FIND
    ?name,
    ?life_stage
WHERE
    characters(name=?name, life_stage=?life_stage)
LIMIT 5;
```

```plaintext
-- Query below does the same as the previous, but returns results starting at row 10

FIND
    ?name,
    ?life_stage
WHERE
    characters(name=?name, life_stage=?life_stage)
LIMIT 5 OFFSET 10;
```

### Aggregation Functions

Drolta supports the basic [SQLite aggregation functions](https://www.sqlite.org/lang_aggfunc.html): COUNT, SUM, MIN, MAX, and AVG. In Drolta, they have the same behavior as they would in SQLite. Remember that aggregate functions such as COUNT should be used with GROUP BY. Aggregate functions are called within the FIND-clause of queries or the DEFINE-clause of rules (see examples below). Aggregates results may also be aliased to a different output name using `AS <alias>`.

```plaintext
-- An example query using COUNT to get house IDs mapped to their size.

FIND
    ?house_id, COUNT(?character_id) AS size
WHERE
    characters(id=?character_id, house_id=?house_id)
GROUP BY ?house_id
ORDER BY ?size DESC;
```

```plaintext
-- An example rules using MAX to find the house with the highest reputation.

DEFINE
    HighestHouseRep(MAX(?rep))
WHERE
    houses(reputation=?rep);

DEFINE
    MostInfluentialHouse(?house_id, ?rep)
WHERE
    HighestHouseRep(?rep)
    houses(id=?house_id, reputation=?rep);
```

### Comments

Drolta supports line and block comments. Below are examples of both.

```plaintext
-- This is a line comment

/*

This is a block comment
that spans multiple lines.

*/
```

## 💢 Troubleshooting

### OperationalError: database is locked

If you receive this error. Then the cursor of a previous query was not properly closed. This often happens when an exception is thrown within an IPython notebook before the contents of a result are read and destroyed. Restarting the kernel/runtime will remove the problem. Then you should reevaluate your code and ensure you do one of the following.

1. Call `fetch_all()` on the result.
2. Call `fetch_chunks()` and read all the chunks.
3. Call `fetch_chunks()`, read some chunks, and call `destroy()` on the result to free resources.
4. Use the result in a context manager with-statement to have resources automatically destroyed. For example, `with engine.query(...) as result`.

## 🧪 Running Unit Tests

Drolta uses [PyTest](https://docs.pytest.org/en/stable/) for unit testing. All tests are
in the [/tests](./tests) directory. When contributing features or bug fixes to this
repository, please ensure all the tests pass before making a pull request. Thank you.

```bash
# Step 1: Install dependencies for testing and development (PyTest)
python -m pip install -e ".[development]"

# Step 2: Run PyTest
pytest
```

## 🎨 Syntax Highlighting Support

Drolta is an experimental query language. There are no VSCode extensions to provide
syntax highlighting support. If enough people use this Drolta, I'll consider
implementing a VSCode extension. Alternatively, if you're interested in implementing it,
I'd love to hear about it. Please email me.

## 🏆 Ports and Applications

If you're using drolta or have created a port of drolta for another language. Please
contact me to have it listed here. I'd love to have a port for C# in Unity and one for
Godot.

## 🧱 Editing the Parser

Drolta uses [ANTLR4](https://www.antlr.org/) to generate its parser. If you modify the
`*.g4` grammar file, you must run the command below. It will generate new base classes
for the parser.

```bash
antlr4 -Dlanguage=Python3 -listener -no-visitor ./src/drolta/Drolta.g4 -o ./src/drolta/parsing
```

**WARNING:** This can cause breaking changes in the implementation that must be
addressed before using the package.

You can visualize an example parse tree with the following command (assuming you have
`antlr4-tools` installed by pip).

```bash
antlr4-parse src/drolta/Drolta.g4 prog -gui
```

## 📦 Packaging

Drolta is packaged using [Hatchling](https://hatch.pypa.io/1.9/). The following command
will create build and source distributions.

```bash
$ python3 -m build

dist/
├── drolta-<VERSION>-py3-none-any.whl
└── drolta-<VERSION>.tar.gz
```

## 🤝 License

This project is licensed under the [MIT License](./LICENSE).

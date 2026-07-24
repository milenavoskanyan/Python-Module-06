# Python Module 06 – Mastering Python Imports

This project focuses on understanding Python's import system by building a small alchemy-themed package. Rather than implementing complex algorithms, the goal is to learn how Python organizes code into modules and packages and how different import mechanisms work together.

## What This Project Teaches

Throughout the project, the following concepts are explored:

* Creating and organizing Python modules and packages.
* The purpose of `__init__.py` and how it turns a directory into a package.
* Importing entire modules versus importing specific objects.
* Absolute imports and when they should be used.
* Relative imports and how they simplify imports within packages.
* Exposing a controlled public API through `__init__.py`.
* Using `__all__` to define a package's public interface.
* Creating aliases for imported objects.
* Accessing nested modules through package initialization.
* Understanding circular imports, why they occur, and several ways to resolve them.
* Following Python's recommended package organization practices.

## Project Structure

```text
.
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_alembic_2.py
├── ft_alembic_3.py
├── ft_alembic_4.py
├── ft_alembic_5.py
├── ft_distillation_0.py
├── ft_distillation_1.py
├── ft_kaboom_0.py
├── ft_kaboom_1.py
├── ft_transmutation_0.py
├── ft_transmutation_1.py
├── ft_transmutation_2.py
└── alchemy
    ├── __init__.py
    ├── elements.py
    ├── potions.py
    ├── grimoire
    │   ├── __init__.py
    │   ├── light_spellbook.py
    │   ├── light_validator.py
    │   ├── dark_spellbook.py
    │   └── dark_validator.py
    └── transmutation
        ├── __init__.py
        └── recipes.py
```

## Project Parts

### Part I – The Alembic

Introduces the fundamentals of Python imports by demonstrating different ways of accessing modules and functions, as well as exposing selected objects through a package interface.

### Part II – Distillation

Demonstrates importing functionality across multiple modules and packages while building reusable components that depend on one another.

### Part III – The Great Transmutation

Explores the differences between absolute and relative imports, showing when each approach is appropriate and how they coexist in larger projects.

### Part IV – Avoid the Explosion

Demonstrates circular dependencies by intentionally creating one failing example and one working solution. The project shows how moving an import inside a function can delay imports and safely break circular dependencies.

## Running the Examples

Each script demonstrates a different import concept.

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py
python3 ft_alembic_5.py

python3 ft_distillation_0.py
python3 ft_distillation_1.py

python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py

python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

> **Note:** `ft_kaboom_1.py` is expected to raise an exception, as it intentionally demonstrates a circular import.

## Requirements

* Python 3.10+
* Full type annotations
* Compatible with `flake8`
* Compatible with `mypy`

## Author

Milena Voskanyan

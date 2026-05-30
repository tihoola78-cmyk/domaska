import pytest
import sqlite3
from datetime import datetime, timezone


@pytest.fixture
def connection():
    conn = sqlite3.connect(':memory:')
    conn.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            deleted_at TIMESTAMP
        )
    ''')
    yield conn
    conn.close()


@pytest.fixture
def student_data():
    return {
        "name": "Иван Петров",
        "email": "ivan.petrov@example.com"
    }


def test_create_student(connection, student_data):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (student_data["name"], student_data["email"])
    )
    connection.commit()

    cursor.execute(
        "SELECT id, name, email FROM students WHERE email = ?",
        (student_data["email"],)
    )
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == student_data["name"]
    assert row[2] == student_data["email"]


def test_update_student(connection, student_data):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (student_data["name"], student_data["email"])
    )
    connection.commit()

    new_name = "Петр Иванов"
    cursor.execute(
        "UPDATE students SET name = ? WHERE email = ?",
        (new_name, student_data["email"])
    )
    connection.commit()

    cursor.execute(
        "SELECT name FROM students WHERE email = ?",
        (student_data["email"],)
    )
    assert cursor.fetchone()[0] == new_name


def test_soft_delete_student(connection, student_data):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (student_data["name"], student_data["email"])
    )
    connection.commit()

    now = datetime.now(timezone.utc)
    cursor.execute(
        "UPDATE students SET deleted_at = ? WHERE email = ?",
        (now, student_data["email"])
    )
    connection.commit()

    cursor.execute(
        "SELECT deleted_at FROM students WHERE email = ?",
        (student_data["email"],)
    )
    assert cursor.fetchone()[0] is not None

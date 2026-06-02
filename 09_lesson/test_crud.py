import pytest
from datetime import datetime, timezone
import time
from models import Student


@pytest.fixture
def student_data():
    # Уникальный email на основе времени
    unique_email = f"test.{int(time.time() * 1000)}@example.com"
    return {
        "name": "Иван Петров",
        "email": unique_email
    }


def test_create_student(session, student_data):
    student = Student(**student_data)
    session.add(student)
    session.commit()
    assert student.id is not None


def test_update_student(session, student_data):
    student = Student(**student_data)
    session.add(student)
    session.commit()

    new_name = "Петр Иванов"
    student.name = new_name
    session.commit()

    updated_student = session.get(Student, student.id)
    assert updated_student.name == new_name


def test_soft_delete_student(session, student_data):
    student = Student(**student_data)
    session.add(student)
    session.commit()

    student.deleted_at = datetime.now(timezone.utc)
    session.commit()

    deleted_student = session.get(Student, student.id)
    assert deleted_student.deleted_at is not None

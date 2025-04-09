import pytest
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError

# Подключение к тестовой БД
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Модель Student для тестирования
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Фикстура для сессии БД
@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Тест на добавление
def test_create_student(db_session):
    # Удаляем тестовые данные, если они есть
    db_session.query(Student).filter(Student.email == "test@example.com").delete()
    db_session.commit()
    
    # Создаём нового студента
    new_student = Student(name="Test Student", email="test@example.com")
    db_session.add(new_student)
    db_session.commit()
    
    # Проверяем, что студент добавлен
    student = db_session.query(Student).filter(Student.email == "test@example.com").first()
    assert student is not None
    assert student.name == "Test Student"
    
    # Удаляем тестовые данные
    db_session.delete(student)
    db_session.commit()

# Тест на обновление
def test_update_student(db_session):
    # Создаём тестового студента
    student = Student(name="Update Test", email="update@example.com")
    db_session.add(student)
    db_session.commit()
    
    # Обновляем имя
    student.name = "Updated Name"
    db_session.commit()
    
    # Проверяем обновление
    updated_student = db_session.query(Student).filter(Student.email == "update@example.com").first()
    assert updated_student.name == "Updated Name"
    
    # Удаляем тестовые данные
    db_session.delete(updated_student)
    db_session.commit()

# Тест на удаление (soft delete)
def test_soft_delete_student(db_session):
    # Создаём тестового студента
    student = Student(name="Delete Test", email="delete@example.com")
    db_session.add(student)
    db_session.commit()
    
    # "Удаляем" (soft delete)
    student.is_active = False
    db_session.commit()
    
    # Проверяем, что студент "удалён"
    deleted_student = db_session.query(Student).filter(Student.email == "delete@example.com").first()
    assert deleted_student.is_active is False
    
    # Удаляем тестовые данные полностью
    db_session.delete(deleted_student)
    db_session.commit()
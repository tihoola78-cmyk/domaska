import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


@pytest.fixture(scope="session")
def engine():
    engine = create_engine('sqlite:///:memory:')
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
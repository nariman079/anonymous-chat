import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database
from starlette.testclient import TestClient

from src.database import Base, get_db
from src.main import app


@pytest.fixture(scope='function')
def session_local():
    DATABASE_URL = "sqlite:///./test_temp.db"
    engine = create_engine(DATABASE_URL)

    assert not database_exists(DATABASE_URL), "Test database already exists. Aborting tests."

    # Create test database and tables
    Base.metadata.create_all(engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield session_local

    # Drop the test database
    drop_database(DATABASE_URL)


def temp_db(f):
    def func(*args, **kwargs):
        def override_get_db():
            try:
                db = session_local()
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_db] = override_get_db

        f(*args, **kwargs)

        app.dependency_overrides[get_db] = get_db

    return func


client = TestClient(app)

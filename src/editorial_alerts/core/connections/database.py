import os
from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine, Connection
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, sessionmaker


class DatabaseConnection:
    def __init__(self, url: str | URL, *, echo: bool = False) -> None:
        self._engine: Engine | None = create_engine(url, echo=echo, connect_args = {"check_same_thread": False})
        self._sessionmaker: sessionmaker[Session] | None = sessionmaker(bind=self._engine, expire_on_commit=False)

    @property
    def engine(self) -> Engine | None:
        return self._engine

    def has_engine(self) -> bool:
        return self._engine is not None

    def close(self) -> None:
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None
            self._sessionmaker = None

    @contextmanager
    def connect(self) -> Generator[Connection, None, None]:
        if self._engine is None:
            raise RuntimeError("Database connection is closed")
        with self._engine.begin() as connection:
            yield connection

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        if self._sessionmaker is None:
            raise RuntimeError("Database connection is closed")
        with self._sessionmaker() as session:
            try:
                yield session
            except Exception:
                session.rollback()
                raise

    def get_session(self) -> Generator[Session, None, None]:
        with self.session() as session:
            yield session


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./editorial.db")
db = DatabaseConnection(DATABASE_URL)

def get_db() -> Generator[Session, None, None]:
    yield from db.get_session()
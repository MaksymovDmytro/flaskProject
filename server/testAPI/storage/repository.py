from contextlib import contextmanager
from logging import getLogger

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

logger = getLogger("Flask-Project-Logger")
Base = declarative_base()


class ConnectionManager:

    def __init__(self, uri: str):
        try:
            self.engine = create_engine(uri)
            self.Session = sessionmaker(bind=self.engine)
        except Exception as e:
            logger.error(e)
        else:
            logger.debug(self.engine.engine)


    @contextmanager
    def session_scope(self) -> Session:
        session = self.Session(expire_on_commit=False)
        try:
            logger.debug(f"Initialized session")
            # Yield session to the scope
            yield session
            # Commit changes after
            session.commit()
        except Exception as e:
            logger.error(e)
            # Rollback if transaction failed
            session.rollback()
            raise
        finally:
            logger.debug("Session closed")
            # Close session eventually
            session.close()


class Repository:

    def __init__(self, model=None, connection_manager: ConnectionManager = None) -> None:
        self._cm = connection_manager
        self._model = model

    def get_object(self, pk):
        """
        Returns an object based on primary key
        """
        with self._cm.session_scope() as session:
            obj = None
            try:
                obj = session.query(self._model).get(pk)
            except Exception as e:
                logger.error(e)
                raise
            finally:
                return obj

    def filter_by(self, **kwargs):
        """
        Filters objects based on given column_name=value set
        """
        with self._cm.session_scope() as session:
            objs = None
            try:
                objs = session.query(self._model).filter_by(
                    **kwargs,
                )
            except Exception:
                raise
            finally:
                return objs

    def filter(self, *args):
        """
        Filters objects based on given column_name=value set
        """
        with self._cm.session_scope() as session:
            objs = None
            try:
                objs = session.query(self._model).filter(
                    *args,
                )
            except Exception:
                raise
            finally:
                return objs

    def bulk_save(self, objs: list):
        with self._cm.session_scope() as session:
            try:
                session.bulk_save_objects(objs)
            except Exception:
                raise

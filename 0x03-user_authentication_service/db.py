#!/usr/bin/env python3
"""
DB Module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Saves a user to the database
        Args:
            email: (str) user's email address
            hashed_password: (str) email password (hashed)
        Return: User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Takes in arbitrary keyword arguments and
        return the first row in the users table filtered by the
        method's input arguments
        Args:
            **kwargs
        Return:
            User object or error if not found
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
        except InvalidRequestError as err:
            raise err
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Method uses self.find_user_by to locate the user to update,
        then will update the user's attributes as passed in the method's
        arguments then commit changes to the database
        Args:
            user_id: (int) user id to be updated
            kwargs: keyword arguments containing information to be updated
        Return:
            NoneType object: None
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError
        for k, v in kwargs.items():
            if hasattr(user, k):
                setattr(user, k, v)
            else:
                raise ValueError
        self._session.add(user)
        self._session.commit()

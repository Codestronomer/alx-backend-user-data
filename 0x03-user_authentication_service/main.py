#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
"""
test_db = DB()

user_1 = test_db.add_user("test@test.com", "superhashedpwd")
print(user_1.id)

find_user = test_db.find_user_by(email="test@test.com")
#print(find_user.id)

try:
    find_user = test_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = test_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")

try:
    test_db.update_user(user_1.id, hashed_password="NewPwd")
    print("Password updated")
except ValueError:
    print("Error")

print(test_db.find_user_by(id=user_1.id).hashed_password)
"""

from auth import Auth

email = "me@me.com"
password = "mySecurePwd"

auth = Auth()
"""
try:
    user = auth.register_user(email, password)
    print("Successfully created a new user!")
except ValueError as err:
    print("Cound not create a new user : {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))
"""

auth.register_user(email, password)
"""
print(auth.valid_login(email, password))
print(auth.valid_login(email, "WrongPwd"))
print(auth.valid_login("unknown@email", password))
"""
print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))

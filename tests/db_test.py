#!flask/bin/python
import unittest
from app import db, models
# db.create_all()
# users = models.User.query.all()
# print(users)
u = models.User(username='xulu', password='123')
# u=models.User.query.one()
db.session.add(u)
db.session.commit()
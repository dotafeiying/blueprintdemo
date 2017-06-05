#!flask/bin/python
import unittest
from app import db, models
from app.models import Role

# users = models.User.query.all()
# print(users)
# u = models.User(username='yuanjie', password='123')
# db.session.add(u)
# db.session.commit()

Role.insert_roles()
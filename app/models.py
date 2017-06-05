from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
from app import app


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.SmallInteger, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'STAFF': (Permission.ONLY_QUERY, True),
            'HIGH_STAFF': (Permission.ONLY_QUERY|
                       Permission.FORBID, False),
            'LEADER': (Permission.ONLY_QUERY|
                       Permission.FORBID|
                       Permission.ASSIGN, False),
            'ADMINISTATOR': (0xff, False)
        }#除了onlyquery之外，其他的都是模式false
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                # 如果用户角色没有创建: 创建用户角色
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    # email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=False, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # config_content = config[os.getenv('FLASK_CONFIG') or 'default']

    def  __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)
        #继承了父类的初始化方法,super等价于UserMixin
        # self.role = kwargs['role_id']
        app_ctx = app.app_context()
        app_ctx.push()
        print(current_app.config['FLASKY_ADMIN'])
        if self.role is None:
            if self.username == current_app.config['FLASKY_ADMIN']:
            #验证email是否为设置的管理员的email
                print('t')
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.username == current_app.config['FLASKY_FORBID']:
            #验证username是否为设置的协管员的username
                self.role = Role.query.filter_by(name='HIGH_STAFF').first()
            if self.role is None:
            #如果经过了上一步权限还为空，就给个默认的User权限
                print('f')
                self.role = Role.query.filter_by(default=True).first()

    def can(self,permissions):
    #这个方法用来传入一个权限来核实用户是否有这个权限,返回bool值
        return self.role is not None and \
        (self.role.permissions & permissions) == permissions

    def is_administrator(self):
    #因为常用所以单独写成一个方法以方便调用，其它权限也可以这样写
        return self.can(Permission.ADMINISTRATOR)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Permission:
    ONLY_QUERY = 0x01#仅查询
    FORBID = 0x03#封号
    ASSIGN= 0x07#分配行号
    ADMINISTRATOR = 0x0f#这个权限要异或

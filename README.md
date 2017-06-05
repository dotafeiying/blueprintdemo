# blueprintdemo
# flask 大型项目的模板 包含基础的用户登录、权限管理、数据库迁移
本示例演示在flask中大型项目中如何使用蓝本（本示例中的main、auth）

首次运行该示例，请按如下步骤操作：

1.安装flask、mysql.connector驱动、Flask-Login（用于用户登录认证）、Flask-SQLAlchemy（ORM技术）。

2.将config.py配置中的SQLALCHEMY_DATABASE_URI修改为自己的数据库连接配置。

3.运行db.create_all()，根据SQLAlchemy模型创建数据库表。

4.运行Role.insert_roles()，初始化用户角色。

5.u = models.User(username='xxx', password='xxx')
  db.session.add(u)
  db.session.commit()
  用来创建用户，用户信息保存在mysql数据库中。

# 如果是中大型的应用话，可以参考本示例的项目结构，避免重复造轮子。

# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from config import MYSQL_PASS, MYSQL_USER, MYSQL_HOST

Base = automap_base()

# 数据库连接
MYSQL_CONN = 'mysql+mysqldb://{0}:{1}@{2}/Blog?charset=utf8'.format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
database = create_engine(MYSQL_CONN, pool_recycle=120)

# 默认自动flush（一旦flush就能在query中拿到数据），但是不自动提交（不提交就不会真的写到数据库中去），
# 由程序自己控制，这样有利于事务的控制
DBSession = sessionmaker(bind=database, autoflush=True, autocommit=False, expire_on_commit=True)


def get_session():
    """ 每次返回一个session的实例就实际上从连接池里面拿走一个conn，从conn可以拿出一个transaction（事务）来用 """
    return DBSession()


class ArticleModel(Base):
    __tablename__ = 'article'


Base.prepare(database, reflect=True)

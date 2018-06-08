# -*- coding: utf-8 -*-

import traceback
from schemer import Schema
from app.blog.entity.article_cls import Article

from repository.mysql import get_session
from repository.mysql.article_rep import ArticleRepository


class Controller(object):

    def __init__(self):
        pass

    def find_all(self):
        """ 查全部 """
        try:
            ar = ArticleRepository()
            article_list = ar.find_all()
            return article_list
        except:
            traceback.print_exc()

    def find_with_info(self, **kwargs):
        """ 条件查 """
        try:
            ar = ArticleRepository()
            article = ar.find_one(**kwargs)
            return article

        except:
            traceback.print_exc()

    def find_hot(self):
        """ 查最热 """
        try:
            ar = ArticleRepository()
            article = ar.find_hot()
            return article

        except:
            traceback.print_exc()

    def create_article(self, param):
        """ 创建 """

        param_schema = Schema({
            'id': {'type': basestring, 'required': False},
            'no': {'type': basestring, 'required': False},
            'author': {'type': basestring, 'required': False, 'default': 'zhuxin'},
            'title': {'type': basestring, 'required': True},
            'intro': {'type': basestring, 'required': False},
            'content': {'type': basestring, 'required': True},
            'category': {'type': basestring, 'required': False, 'default': 'test'},
            'views': {'type': basestring, 'required': False},
            'modified': {'type': basestring, 'required': False},

        })
        param_schema.validate(param)  # 检测不通过直接抛异常
        param_schema.apply_defaults(param)  # attach 默认值

        article_param = {
            'id': param.get('id'),
            'no': param.get('no'),
            'author': param.get('author'),
            'title': param.get('title'),
            'intro': param.get('intro'),
            'content': param.get('content'),
            'category': param.get('category'),
            'views': param.get('views'),
            'modified': param.get('modified')
        }
        session = get_session()

        try:
            article = Article(**article_param)

            ar = ArticleRepository(session)
            ar.save(article)
            session.commit()
            session.close()

            return article

        except:
            traceback.print_exc()

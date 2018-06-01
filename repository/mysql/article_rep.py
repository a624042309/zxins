# -*- coding: utf-8 -*-
# import markdown
# from flask import Markup
from sqlalchemy.orm.exc import NoResultFound
from app.blog.application.entity.article_cls import Article
from repository.mysql import get_session, ArticleModel


class ArticleRepository(object):

    def __init__(self, session=None):
        self.session = session or get_session()

        # 决定是否自己销毁session, 而不是依赖上层回收
        if session is None:
            self.auto_close_session = True
        else:
            self.auto_close_session = False

    def __del__(self):
        try:
            if self.auto_close_session:
                self.session.close()
        except:
            pass

    def find_all(self):
        results = self.session.query(ArticleModel).all()

        objs = []
        for result in results:
            modified = str(result.modified).split(' ')[0]
            param = dict(
                no=result.no,
                author=result.author,
                title=result.title,
                content=result.content,
                category=result.category,
                views=result.views,
                modified=modified,
            )
            article = Article(**param)
            objs.append(article)
        return objs

    def find_one(self, **kwargs):
        try:
            criterion = [getattr(ArticleModel, i) == kwargs[i] for i in kwargs]
            result = self.session.query(ArticleModel).filter(*criterion).one()
            modified = str(result.modified).split(' ')[0]

            param = dict(
                no=result.no,
                author=result.author,
                title=result.title,
                content=result.content,
                category=result.category,
                views=result.views,
                modified=modified,
            )
            article = Article(**param)

            return article

        except NoResultFound:
            return None

        except Exception as e:
            raise e


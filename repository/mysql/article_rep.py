# -*- coding: utf-8 -*-
from sqlalchemy.orm.exc import NoResultFound
from app.blog.entity.article_cls import Article
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
        hot = self.find_hot()
        results = self.session.query(ArticleModel).all()

        objs = []
        for result in results:
            if int(result.id) != int(hot.id):
                modified = str(result.modified).split(' ')[0]
                param = dict(
                    id=str(result.id),
                    no=result.no,
                    author=result.author,
                    title=result.title,
                    intro=result.intro,
                    content=result.content,
                    category=result.category,
                    views=result.views,
                    modified=modified,
                )
                article = Article(**param)
                objs.append(article)

        # TODO: 反转列表要改成数据库排序
        return list(reversed(objs))

    def find_one(self, **kwargs):
        try:
            criterion = [getattr(ArticleModel, i) == kwargs[i] for i in kwargs]
            result = self.session.query(ArticleModel).filter(*criterion).one()
            modified = str(result.modified).split(' ')[0]

            param = dict(
                id=str(result.id),
                no=result.no,
                author=result.author,
                title=result.title,
                intro=result.intro,
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

    def find_hot(self):
        """ 查最新&浏览量最高的 """
        views_sql = "select max(id) from article where views = (select max(views) from article)"
        max_id = self.session.execute(views_sql).first()

        model = self.session.query(ArticleModel).filter(ArticleModel.id == max_id['max(id)']).one()
        param = {
            'id': str(model.id),
            'no': model.no,
            'author': model.author,
            'title': model.title,
            'intro': model.intro,
            'content': model.content,
            'category': model.category,
            'views': model.views,
            'modified': str(model.modified)
        }
        article = Article(**param)
        return article

    def save(self, article):
        try:
            import datetime
            model = ArticleModel()
            model.no = article.no
            model.author = article.author
            model.title = article.title
            model.intro = article.intro
            model.content = article.content
            model.category = article.category
            model.views = article.views
            model.created = datetime.datetime.now()
            model.modified = datetime.datetime.now()
            self.session.add(model)

        except Exception as e:
            self.session.rollback()
            raise e


if __name__ == '__main__':
    ar = ArticleRepository()
    ar.find_all()

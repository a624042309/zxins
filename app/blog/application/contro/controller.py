# -*- coding: utf-8 -*-

import traceback
from repository.mysql.article_rep import ArticleRepository


class Controller(object):

    def __init__(self):
        pass

    def get_all_article(self):
        try:
            ar = ArticleRepository()
            article_list = ar.find_all()

            return article_list

        except:
            traceback.print_exc()

    def get_one_article(self, **kwargs):
        try:
            ar = ArticleRepository()
            article = ar.find_one(**kwargs)

            return article

        except:
            traceback.print_exc()

# -*- coding: utf-8 -*-

import traceback
from repository.mysql.article import ArticleRepository


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

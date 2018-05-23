# -*- coding: utf-8 -*-


class Article(object):
    """ 文章类 """

    def __init__(self, **kwargs):
        """
        :param author:  作者
        :param title:   标题
        :param content: 内容
        :param label:   标签
        """
        self.no = kwargs.get('no')
        self.author = kwargs.get('author')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.category = kwargs.get('category')
        self.views = kwargs.get('views')

    def dictify(self):
        d = dict(filter(lambda x: isinstance(x[1], (str, float, int, unicode)), self.__dict__.items()))
        return d

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
        self.author = kwargs.get('author')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.label = kwargs.get('label')

    def dictify(self):
        d = dict(filter(lambda x: isinstance(x[1], (str, float, int, unicode)), self.__dict__.items()))
        return d

if __name__ == '__main__':
    d = {
        'author': 'zz',
        'title': 'zz',
        'content': 'zzz',
        'label': 'll'
    }

    a = Article(**d)
    print a.dictify()
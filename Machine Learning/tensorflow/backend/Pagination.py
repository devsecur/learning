from math import ceil


class Pagination(object):
    def __init__(self, content, per_page=20):
        self.content = content
        self.per_page = per_page

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self, page):
        return self.page > 1

    @property
    def has_next(self, page):
        return page < self.pages(self)

    def page(self, page):
        return self.content[(page-1)*self.per_page:page*self.per_page]

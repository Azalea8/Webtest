"""
自定义的分页组件
"""
from django.utils.safestring import mark_safe

class Pagination(object):

    def __init__(self, request, data_all_list, page_size=10, plus=4):
        self.page = request.GET.get('page', '1')
        self.search_data = request.GET.get('q', '')

        if self.page.isdecimal():
            self.page = int(self.page)
        else:
            self.page = 1

        self.page_size = page_size

        if data_all_list.count() % page_size != 0:
            self.page_max = data_all_list.count() // page_size + 1
        else: self.page_max = data_all_list.count() / page_size

        self.page_list = [self.page + i for i in range(-plus, plus+1)]
        self.page = max(1, self.page)
        self.page = min(self.page_max, self.page)
        self.l = (self.page - 1) * self.page_size
        self.r = self.page * self.page_size
        self.data_list = data_all_list[self.l: self.r]

    def html(self):
        page_str_list = []

        for P in self.page_list:
            ele = ''
            if 0 < P <= self.page_max and P != self.page:
                ele = '<li><a href="?q={}&page={}">{}</a></li>'.format(self.search_data, P, P)
            elif 0 < P <= self.page_max and P == self.page:
                ele = '<li class="active"><a href="?q={}&page={}">{}</a></li>'.format(self.search_data, P, P)
            page_str_list.append(ele)

        ele = '<li><a href="?q={}&page={}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>'.format(self.search_data, self.page_max)
        page_str_list.append(ele)

        page_string = mark_safe("".join(page_str_list))
        return page_string



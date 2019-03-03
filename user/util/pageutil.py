from django.core.paginator import Paginator


def get_one_page(objects, page, number_for_one_page):
    pages = Paginator(objects, number_for_one_page)
    return pages.page(page)
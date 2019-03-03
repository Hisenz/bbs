from django.core.paginator import Paginator


def get_one_page(objects, page, number_for_one_page):
    pages = Paginator(objects, number_for_one_page)
    try:
        return pages.page(page)
    except:
        return pages.page(1)
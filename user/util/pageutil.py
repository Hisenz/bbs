from django.core.paginator import Paginator


def get_one_page(objects, page, number_for_one_page):
    pages = Paginator(objects, number_for_one_page)
    try:
        return pages.page(page)
    except:
        if page > pages.num_pages:
            return pages.page(pages.num_pages)
        else:
            return pages.page(1)
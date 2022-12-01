from rest_framework.pagination import CursorPagination


# class ReviewsPagination(PageNumberPagination):
#     page_size = 3
#     page_query_param = 'p'
#     page_size_query_param = 'size'
#     max_page_size = 6

# class ReviewsPagination(LimitOffsetPagination):
#     default_limit = 3
#     max_limit = 6
#     # limit_query_param = 'limit'
#     # offset_query_param = 'offset'

class ReviewsPagination(CursorPagination):

    page_size = 3
    ordering = 'created'
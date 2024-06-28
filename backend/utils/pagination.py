from rest_framework import pagination

class DefaultPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"


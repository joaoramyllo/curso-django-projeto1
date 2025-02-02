from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):

    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qtd_pages = 5,
            current_page = 1,     

            )
        self.assertEqual([1, 2, 3, 4, 5], pagination)

        
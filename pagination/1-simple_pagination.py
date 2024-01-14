#!/usr/bin/env python3
""" pagination tools """
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """  a helper function to get page number and pagination limit  """

    last = page_size * page
    first = (page - 1) * page_size
    return (first, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return a correct pagination  """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        pages = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pages[0]: pages[1]]

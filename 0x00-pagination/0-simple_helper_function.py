#!/usr/bin/env python3
"""
This module contains a simple helper function.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index.
    """
    return ((page - 1) * page_size, page * page_size)

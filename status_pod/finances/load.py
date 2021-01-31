"""

    this module provides loading finance data from different sources

    sources:
        - excel
        - txt file
        - message
"""
import typing as t
import csv

from collections import defaultdict


def get_raw_file_data_as_matrix(path):
    """WARNING: may be long reading due to list()"""
    with open(path) as f:
        r = csv.reader(f)
        return list(r)


def get_headers(r: iter) -> t.List[t.Optional[t.List]]:
    """
    WARNING: modifies r

    retrieves headers from file
    for building index

    current file format assumed 2 first lines as headers
    """

    try:
        return [next(r), next(r)]
    except StopIteration:
        # if wrong headers format
        return []


def get_index_position_in_headers(index: str, headers: t.List[t.List]):
    # так как хедеров не один (сейчас 2) - ищем наш индекс в каждом из них
    for header in headers:
        if index in header:
            try:
                return header.index(index)
            except ValueError:
                continue
    return None


def map_index_to_its_position(indexes: t.List[str], headers: t.List[t.List]):
    return {
        index: get_index_position_in_headers(index, headers)
        for index in indexes
    }


def build_index_on_raw_file_data(path, indexes: t.List[str] = None):
    # TODO make index names case insensitive
    indexes = [] if not indexes else indexes
    index = defaultdict(list)
    with open(path) as f:
        rows = csv.reader(f)
        headers = get_headers(rows)
        index_to_position = map_index_to_its_position(indexes, headers)
        for row in rows:
            for index_ in indexes:
                pos = index_to_position[index_]
                index[row[pos]].append(row)
    return index

from pytest import fixture

from status_pod.finances.load import build_index_on_raw_file_data


@fixture
def path_to_table_data():
    return 'status_pod/tests/table.csv'


@fixture
def table_data_bites():
    pass


@fixture
def table_data_from_csv_file(path_to_table_data):
    def data_retrieving_function(index: str):
        return build_index_on_raw_file_data(path=path_to_table_data, indexes=[index])
    return data_retrieving_function

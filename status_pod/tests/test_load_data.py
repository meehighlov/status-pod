from status_pod.finances.analytic_models.meta import TableRow


def test_data_loading(table_data_from_csv_file):
    index, headers_list = table_data_from_csv_file(index='Дата')

    assert index
    assert headers_list

    assert all(isinstance(value, TableRow) for value in index.values())

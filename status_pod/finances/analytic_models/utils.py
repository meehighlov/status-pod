def process_number_from_table(num: str):
    try:
        return float(num)
    except ValueError:
        num = num.replace('\xa0', '').replace(' ₽', '')  # хз поможет ли это, когда числа в экселике будут еще больше
        # TODO доработать нормально
        return float(num)

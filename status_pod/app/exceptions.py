class AppError(Exception):
    message = 'App error occurred'

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get('message', self.message)


class LoadFinancesError(AppError):
    message = 'Error while parsing finance data'

class AppError(Exception):
    message = 'App raised an error'

    def __init__(self, *args, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def __str__(self):
        return f'{type(self)} message: {self.message}'


class TimeoutAppError(AppError):
    message = 'Time of a task execution is up'


class HTMLAttributeNoFoundAppError(AppError):
    message = 'HTML attribute could not be parsed'

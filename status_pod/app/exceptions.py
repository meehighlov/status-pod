class AppError(Exception):
    pass


class LoadFinancesError(AppError):
    pass


class SpendingAnalyticsAlgorithmError(AppError):
    pass

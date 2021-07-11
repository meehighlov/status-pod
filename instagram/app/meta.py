from dataclasses import dataclass


@dataclass
class SubscriptionInfo:
    users_amount: int
    nicknames: set

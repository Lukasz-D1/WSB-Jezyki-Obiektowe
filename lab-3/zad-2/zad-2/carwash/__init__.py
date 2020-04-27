from .wash_body_strat import BodyHandWashStrategy, BodyContactlessStrategy
from .wash_wheels_strat import WheelsContactlessStrategy, WheelsHandWashStrategy
from .carwash import Wash

__all__ = [
    'BodyContactlessStrategy',
    'BodyHandWashStrategy',
    'WheelsContactlessStrategy',
    'WheelsHandWashStrategy',
    'Wash'
]
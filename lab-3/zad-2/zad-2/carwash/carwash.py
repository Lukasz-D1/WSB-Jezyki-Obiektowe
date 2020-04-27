class Wash:
    def __init__(self, wash_wheels_strategy, wash_body_strategy):
        self.__wash_wheels_strategy = wash_wheels_strategy
        self.__wash_body_strategy = wash_body_strategy

    def __call__(self, obj_to_wash):
        if obj_to_wash['wheels']:
            self.__wash_wheels_strategy.wash()
        if obj_to_wash['body']:
            self.__wash_body_strategy.wash()
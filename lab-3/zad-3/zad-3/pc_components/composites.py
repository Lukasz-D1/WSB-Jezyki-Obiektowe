from .component import Component


class PCB(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'pcb')
        self.__component_dict = dict()

    def add_component(self, component):
        if component.type == 'disk' or component.type == 'motherboard':
            self.__component_dict[component.id] = component
        else:
            print('Can\'t put {} on PCB.'.format(component.type))

    def remove_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def get_price(self):
        price = self._price
        for comp in self.__component_dict:
            price += self.__component_dict[comp].get_price()
        return price

    def print_price(self):
        print('Current PCB and it\'s components price: {}'.format(self.get_price()))


class Bus(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'bus')
        self.__component_dict = dict()

    def add_component(self, component):
        if component.type == 'card':
            self.__component_dict[component.id] = component
        else:
            print('Can\'t put {} on motherboard.'.format(component.type))

    def remove_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def get_price(self):
        price = self._price
        for comp in self.__component_dict:
            price += self.__component_dict[comp].get_price()
        return price

    def print_price(self):
        print('Current bus and it\'s components price: {}'.format(self.get_price()))


class Tower(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'bus')
        self.__component_dict = dict()

    def add_component(self, component):
        if component.type == 'pcb' or component.type == 'bus':
            self.__component_dict[component.id] = component
        else:
            print('Can\'t put {} in tower. Put it on one of the other components.'.format(component.type))

    def remove_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def get_price(self):
        price = self._price
        for comp in self.__component_dict:
            price += self.__component_dict[comp].get_price()
        return price

    def print_price(self):
        print('Current tower and it\'s components price: {}'.format(self.get_price()))

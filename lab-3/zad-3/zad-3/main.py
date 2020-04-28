from pc_components import *


def main():
    card1 = Card(1, 100)
    moth1 = Motherboard(2, 200)
    bus1 = Bus(3, 100)
    disk1 = Disk(4, 500)
    pcb1 = PCB(2, 300)

    pcb1.add_component(disk1)
    pcb1.add_component(moth1)
    bus1.add_component(card1)

    pcb1.print_price()
    bus1.print_price()

    tow1 = Tower(5, 1000)
    tow1.add_component(bus1)
    tow1.add_component(pcb1)
    tow1.add_component(disk1)
    tow1.print_price()


if __name__ == '__main__':
    main()

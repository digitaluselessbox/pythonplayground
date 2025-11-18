"""no module at all. Just testing a train class."""


class Train:
    """represent a train with stations"""

    def __init__(self, route, position) -> None:
        self.route = route
        self.position = position

    def show_station(self):
        """print the actual station name"""
        print(self.route[self.position])

    def move(self, steps=1):
        """ move the train forward """
        if self.position + steps >= len(self.route):
            print("Endstation! Alle aussteigen!")
            return

        self.position = self.position + steps

    def move_back(self, steps=1):
        """ move the train backwards """
        if self.position - steps < 0:
            print("Startstation, und noch ne Runde!")
            return

        self.position = self.position - steps

    def bypass_station(self, station_name):
        """ remove a station and reset train to start """
        self.route.remove(station_name)
        self.position = 0



orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()

print("----------------")

orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()

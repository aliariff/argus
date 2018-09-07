class LocationDetails:
    def __init__(self, locations, location):
        self.locations = locations
        self.location = self.locations.original[location]["labelShort"]
        self.meta = self.locations.original[location]

    def device(self):
        if "Android" in self.meta["group"] or "Apple" in self.meta["group"]:
            return self.meta["Label"]
        else:
            return "Machine"

    def city(self):
        return self.meta["group"]

    def country(self):
        return self.locations.fixed[self.location]["country"]

    def region(self):
        return self.locations.fixed[self.location]["city"]

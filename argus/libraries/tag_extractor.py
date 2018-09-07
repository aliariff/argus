from argus.libraries.fix_locations import FixLocations
from argus.libraries.locations_details import LocationDetails
import re
import urllib


class TagExtractor(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.locations = FixLocations()
        self.args = args
        self.kwargs = kwargs

    def extract(self):
        return {
            "browser": self.browser(),
            "city": self.city(),
            "connection": self.connection(),
            "country": self.country(),
            "device": self.device(),
            "region": self.region(),
            "website": self.website(),
        }

    def browser(self):
        return self.data["data"]["location"].split(":")[1]

    def city(self):
        return LocationDetails(self.data["data"]["location"].split(":")[0]).city()

    def connection(self):
        return self.data["data"]["connectivity"]

    def country(self):
        return LocationDetails(self.data["data"]["location"].split(":")[0]).country()

    def device(self):
        return LocationDetails(self.data["data"]["location"].split(":")[0]).device()

    def region(self):
        return LocationDetails(self.data["data"]["location"].split(":")[0]).region()

    def website(self):
        parsed_uri = urllib.parse.urlparse(self.data["data"]["url"])
        if parsed_uri.scheme != "":
            return "{uri.scheme}://{uri.netloc}".format(uri=parsed_uri).lower()
        else:
            return self.data["data"]["url"].rstrip("/").lower()

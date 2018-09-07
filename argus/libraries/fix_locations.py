import json
from geotext import GeoText


class FixLocations:
    with open('getLocations.json') as f:
        locations = json.load(f)

    def __init__(self):
        self.original = locations
        self.fixed = self.get_fixed_locations()

    def get_fixed_locations(self):
        mix = set(self.original[l]['labelShort'] for l in self.original)
        countries = set(GeoText(m).countries[0] for m in mix if GeoText(m).countries)
        cities = set(GeoText(m).cities[0] for m in mix if GeoText(m).cities)
        us_cities = ['California','Chicago','Clifton','Dallas','Denver','Dulles','Lincoln','Los Angeles','New York','Oregon','Orlando','Phoenix','San Francisco','Virginia']
        missing_cities=set(m.split(',')[0] for m in mix if m.split(',')[0] not in cities)-set(countries)
        fix={}
        for m in mix:
            fix[m] = {'city': None, 'country': None}
            d = GeoText(m)
            if d.cities:
                fix[m]['city'] = d.cities[0]
            if d.countries:
                fix[m]['country'] = d.countries[0]
        for f in fix:
            for c in missing_cities:
                if c in f: fix[f]['city']=c
            if 'UK' in f:fix[f]['country']='UK'
            if fix[f]['city'] == 'Amsterdam': fix[f]['country'] = 'Netherlands'
            if fix[f]['city'] == 'Brussels': fix[f]['country'] = 'Belgium'
            if fix[f]['city'] == 'Dubai': fix[f]['country'] = 'UAE'
            if fix[f]['city'] == 'Seoul': fix[f]['country'] = 'South Korea'
            if fix[f]['city'] == 'Virginia USA': fix[f]['city'] = 'Virginia'
            if fix[f]['country'] == 'Singapore': fix[f]['city'] = 'Singapore'
            if fix[f]['country'] == 'Hong Kong':
                fix[f]['city'] = 'Hong Kong'
                fix[f]['country'] = 'China'
            if fix[f]['city'] in us_cities: fix[f]['country'] = 'USA'
        return fix

import config_loader, re

__configurations = config_loader.ConfigurationLoader ()
__configurations.set_configsection ('Google_API')
google_api = __configurations.getconfig()

class DistanceRequest(object):

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def get_params(self):
        queryparams = google_api['google.maps.distance.queryparams']
        params = {}
        for param in queryparams.split (","):
            params.__setitem__ (param, '')
        params.__setitem__ ('origins', self.origin)
        params.__setitem__ ('destinations', self.destination)
        key = google_api['google.maps.distance.token']
        params.__setitem__ ('key', key)
        units = google_api['google.maps.distance.units']
        params.__setitem__ ('units', units)
        return params

    def get_url(self):
        url = google_api['google.maps.host']
        return url

    def get_api(self):
        api = google_api['google.maps.distance.api']
        return api

    def get_format(self):
        _format = google_api['google.maps.outputformat']
        return _format
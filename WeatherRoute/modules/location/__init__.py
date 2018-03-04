import httpclient as client, config_loader, errors


def getlocationurl():
    try:
        configLoader = config_loader.ConfigurationLoader()
        configLoader.set_configsection('Location_API')
        location_api = configLoader.getconfig()
        location_url = location_api['location.url']
        print(location_url)
        return location_url
    except TypeError as er:
        errors.Error("Exception while getting location url: ", er)


class Location (object):
    def __init__(self, url=None, params=None, lat=None, lon=None, state_name=None,
                 state_code=None, zip_code=None, country_code=None, city=None, country_name=None, time_zone=None):
        self.lat = lat
        self.lon = lon
        self.url = url
        self.params = params
        self.city = city
        self.state_name = state_name
        self.state_code = state_code
        self.zip_code = zip_code
        self.country_code = country_code
        self.country_name = country_name
        self.time_zone = time_zone


    def get_latitude(self):
        return self.latitude


    def set_latitude(self, lat):
        self.lat = lat


    def get_longitude(self):
        return self.lon


    def set_longitude(self, lon):
        self.lon = lon


    def get_cityname(self):
        return self.city


    def set_cityname(self, city):
        self.city = city


    def get_statename(self):
        return self.state_name


    def set_statename(self, state_name):
        self.state_name = state_name


    def get_statecode(self):
        return self.state_code


    def set_statecode(self, state_code):
        self.state_code = state_code


    def get_zipcode(self):
        return self.zip_code


    def set_zipcode(self, zip_code):
        self.zip_code = zip_code


    def get_countryname(self):
        return self.country_name


    def set_countryname(self, country_name):
        self.country_name = country_name


    def get_countrycode(self):
        return self.countrycode


    def set_countrycode(self, country_code):
        self.country_code = country_code


    def get_timezone(self):
        return self.timezone


    def set_timezone(self, time_zone):
        self.time_zone = time_zone

    def getlocation(self):
        try:
            self.url = getlocationurl()
            body = client.HttpClient(self.url).get_request()
            self.lat = body['latitude']
            self.lon = body['longitude']
            self.city = body['city']
            self.state_code = body['region_code']
            self.state_name = body['region_name']
            self.country_name = body['country_name']
            self.country_code = body['country_code']
            self.time_zone = body['time_zone']
            self.zip_code = body['zip_code']
            return self
        except TypeError as err:
            errors.Error("Location response could not be retrieved: ", err)
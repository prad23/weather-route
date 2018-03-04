class WeatherRequest(object):
    def __init__(self, url=None, city=None, state=None, format=None):
        self.url = url
        self.city = city
        self.state = state
        self.format = format

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

class WeatherResponse(object):

    def __init__(self, city_name=None, weather_string=None, temp_f=None, temp_string=None,
                    precip_today_metric=None, precip_1hr_metric=None, wind_string=None, wind_mph=None):

        self.city_name = city_name
        self.weather_string = weather_string
        self.temp_f = temp_f
        self.temp_string = temp_string
        self.precip_today_metric = precip_today_metric
        self.precip_1hr_metric = precip_1hr_metric
        self.wind_string = wind_string
        self.wind_mph = wind_mph

    def get_city(self):
        return self.city_name

    def set_city(self, city_name):
        self.city_name = city_name

    def get_weather(self):
        return self.weather_string

    def set_weather(self, weather_string):
        self.weather_string = weather_string

    def get_temperature_f(self):
        return self.temp_f

    def set_temperature_f(self, temp_f):
        self.temp_f = temp_f

    def get_temparature_string(self):
        return self.temp_string

    def set_temparature_string(self, temp_string):
        self.temp_string = temp_string

    def get_precip_today(self):
        return self.precip_today_metric

    def set_precip_today(self, precip_today_metric):
        self.precip_today_metric = precip_today_metric

    def get_precip_1hr(self):
        return self.precip_1hr_metric

    def set_precip_1hr(self, precip_1hr_metric):
        self.precip_1hr_metric = precip_1hr_metric

    def get_wind_name(self):
        return self.wind_string

    def set_wind_name(self, wind_string):
        self.wind_string = wind_string

    def get_wind_speed(self):
        return self.wind_mph

    def set_wind_speed(self, wind_mph):
        self.wind_mph = wind_mph
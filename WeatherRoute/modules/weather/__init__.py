import httpclient as client, config_loader, logging, errors, operator

log = logging.getLogger(__name__)

config = config_loader.ConfigurationLoader ()
config.set_configsection('Weather_API')
weather_api = config.getconfig()


def get_weatherurl():
    weather_host = weather_api['weather.host']
    weather_token = weather_api['weather.token']
    weather_query = weather_api['weather.query']
    return "%s%s%s" % (weather_host, weather_token, weather_query)


def get_weatheroutputformat():
    weather_outputformat = weather_api['weather.outputformat']
    return weather_outputformat

class Weather(object):
    def __init__(self, req, res):

        request_url = ("%s/%s/%s.%s" % (req.get_url(), req.get_state(), req.get_city(), req.get_format()))
        log.debug("Weather request url: %s" % request_url)
        body = client.HttpClient (request_url).get_request()
        if operator.contains(body['response'],'error'):
            raise errors.Error('Query did not return any response.','%s:: %s'
                               %(body['response']['error']['type'],body['response']['error']['description']))
        log.debug("Weather Response: " % (body['current_observation']))
        res.set_city(body['current_observation']['display_location']['city'])
        res.set_weather(body['current_observation']['weather'])
        res.set_temparature_string(body['current_observation']['temperature_string'])
        res.set_temperature_f(body['current_observation']['temp_f'])
        res.set_precip_today(body['current_observation']['precip_today_metric'])
        res.set_precip_1hr(body['current_observation']['precip_1hr_metric'])
        res.set_wind_name(body['current_observation']['wind_string'])
        res.set_wind_speed(body['current_observation']['wind_mph'])

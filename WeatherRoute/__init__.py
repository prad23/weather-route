import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"modules"))
print(sys.path)
import logging, location, weather, errors, distance
from distance import distance_request, distance_response
from weather import weather_request, weather_response

Format = '%(asctime)-15s:%(name)s:%(levelname)s--> %(message)s'
logging.basicConfig (format=Format, filename="weatherRoute.log", level="INFO", filemode="w")
log = logging.getLogger(__name__)

__destination_city__ = "San_Francisco"
__destination_state__ = "CA"


def _weatherResponse(weather_response):
    _weather_string = weather_response.get_weather()
    _city = weather_response.get_city()
    _temp_f = weather_response.get_temperature_f()
    _precip_today_metric = weather_response.get_precip_today()
    _wind_mph = weather_response.get_wind_speed()

    log.info(("Currently it is {} in {}. Temperature is around {} with precipitation {} and wind speed {}."
        .format(_weather_string, _city, _temp_f, _precip_today_metric, _wind_mph)))


def getlocation():
    location_url = location.getlocationurl()
    location_res = location.Location(location_url).getlocation()
    return location_res


def main():
    try:
        log.info("<--------------START----------------->")

        log.info("Get Address based on Latitude and Longitude.")
        location_res = getlocation()
        _places_list = []
        city = location_res.get_cityname()
        state = location_res.get_statecode()
        if not city or not state:
            raise (errors.InputError().message, errors.InputError().expression)
        log.info("Address extracted based on latitude and longitude => '%s,%s'" % (city, state))
        origin = ('%s %s' % (city, state))
        _places_list.append(origin)
        destination = ('%s %s' % (__destination_city__, __destination_state__))
        log.info("Now get the distance between %s and %s" % (origin, destination))
        dist_req = distance_request.DistanceRequest(origin, destination)
        dist_res = distance_response.DistanceResponse()
        distance.Distance(dist_req,dist_res)
        _distance = dist_res.get_distance()
        _duration = dist_res.get_duration()
        if not _distance or not _duration:
            raise errors.Error("Could not get distance or duration for the given destination.", "%s,%s" %(_distance,_duration))
        else:
            _places_list.append(destination)
        log.info(" Distance and duration between %s and %s is %s and %s" %(origin,destination,_distance,_duration))
        weather_url = weather.get_weatherurl()
        output_format = weather.get_weatheroutputformat()
        for place in _places_list:
            log.info("Invoke weather API for location %s" % (place.split(" ")[0]))
            weather_req = weather_request.WeatherRequest()
            weather_req.set_url(weather_url)
            weather_req.set_city(place.split(" ")[0])
            weather_req.set_state(place.split(" ")[1])
            weather_req.set_format(output_format)
            weather_res = weather_response.WeatherResponse()
            weather.Weather(weather_req, weather_res)
            _weatherResponse(weather_res)

        log.info ("<---------------END------------------>")
    except errors.Error as err:
        print("%s %s" % (err.message,err.expression))


if __name__ == "__main__":
    main ()

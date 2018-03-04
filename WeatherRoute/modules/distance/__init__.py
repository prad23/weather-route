import httpclient, errors, logging

log = logging.getLogger(__name__)


class Distance(object):

    def __init__(self, dist_req, dist_res):

        try:
            client = httpclient.HttpClient()
            client.set_params(dist_req.get_params())
            client.set_url("%s%s%s" % (dist_req.get_url(), dist_req.get_api(), dist_req.get_format()))
            response = client.get_request()
            log.debug("Response returned : %s" % response)
            if response['status'] != 'OK':
                raise errors.Error('Http status returned is not valid.', response['status'])
            dist_res.set_status(response['status'])
            for row in response['rows'][0]['elements']:
                if row['status'] != 'OK':
                    raise errors.Error("Origin-Destination pairing returned invalid status.", row['status'])
                dist_res.set_distance(row['distance']['text'])
                dist_res.set_duration(row['duration']['text'])
        except RuntimeError as err:
            raise errors.Error("Error while getting Remote response", err)

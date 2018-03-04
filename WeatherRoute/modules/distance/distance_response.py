
class DistanceResponse(object):
    def __init__(self, status=None, duration=None, duration_in_traffic=None, distance=None):

        self.status = status
        self.duration = duration
        self.duration_in_traffic = duration_in_traffic
        self.distance = distance

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_duration_in_traffic(self):
        return self.duration_in_traffic

    def set_duration_in_traffic(self, duration_in_traffic):
        self.getduration_in_traffic = duration_in_traffic

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

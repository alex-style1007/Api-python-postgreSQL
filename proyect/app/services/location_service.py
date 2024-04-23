from repository.location_repository import LocationRepository

class LocationService:
    def __init__(self):
        self.location_repository = LocationRepository()

    def get_all_countries(self):
        return self.location_repository.get_all_countries()

    def get_country_by_id(self, country_id):
        return self.location_repository.get_country_by_id(country_id)

    def get_reactors_by_country_id(self, country_id):
        return self.location_repository.get_reactors_by_country_id(country_id)

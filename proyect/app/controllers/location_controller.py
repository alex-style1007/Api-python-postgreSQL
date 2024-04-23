from services.location_service import LocationService

location_service = LocationService()

def get_all_countries():
    countries = location_service.get_all_countries()
    if countries:
        return countries
    else:
        return "Error al obtener los países"

def get_country_by_id(country_id):
    country = location_service.get_country_by_id(country_id)
    if country:
        return country
    else:
        return "Error al obtener el país por ID"

def get_reactors_by_country_id(country_id):
    reactors = location_service.get_reactors_by_country_id(country_id)
    if reactors:
        return reactors
    else:
        return "Error al obtener los reactores por país"

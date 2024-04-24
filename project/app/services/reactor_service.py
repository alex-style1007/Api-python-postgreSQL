from project.app.repositories.reactor_repository import ReactorRelationalRepository

class ReactorService:
    def __init__(self):
        self.repository = ReactorRelationalRepository()

    def get_all_reactors(self):
        return self.repository.get_all_reactors()
    
    def get_reactor_by_id(self, id: int):
        return self.repository.get_reactor_by_id(id)
    
    def get_all_reactor_types(self):
        return self.repository.get_all_reactor_types()

    def get_all_locations(self):
        return self.repository.get_all_locations()

    def get_reactors_with_same_reactor_type_by_id(self, reactor_id: int):
        return self.repository.get_reactors_with_same_reactor_type_by_id(reactor_id)
    
    def get_reactors_with_same_location_by_id(self, reactor_id:int):
        return self.repository.get_reactors_with_same_location_by_id(reactor_id)
    
    def get_reactors_by_location(self, country: str, city: str):
        return self.repository.get_reactors_by_location(country, city)
    
    def create_reactor(self, reactor: dict):
        return self.repository.create_reactor(reactor)
    
    def update_reactor(self, reactor: dict, reactor_id: int):
        return self.repository.update_reactor(reactor, reactor_id)
    
    def delete_reactor_by_id(self, reactor_id: int):
        return self.repository.delete_reactor_by_id(reactor_id)
    

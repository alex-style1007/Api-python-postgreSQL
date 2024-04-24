from project.app.repositories.reactor_repository import ReactorRelationalRepository

class ReactorService:
    def __init__(self):
        self.reactor_repository = ReactorRelationalRepository()

    # 1. Obtener reactores registrados
    def get_all_reactors(self):
        return self.reactor_repository.get_all_reactors()
    
    #
    def create_reactor(self, reactor):
        return self.reactor_repository.create_reactor(reactor)
    
    # 2. Obtener un reactor por Id
    def get_reactor_by_id(self, reactor_id):
        return self.reactor_repository.get_reactor_by_id(reactor_id)
    
    # 6. Obtener tipos de reactores registrados
    def get_all_reactor_types(self):
        return self.reactor_repository.get_all_reactor_types()
    
    #
    def get_reactors_by_type_id(self, reactor_id):
        return self.reactor_repository.get_reactors_by_type_id(reactor_id)
    
    # 5. Eliminar un reactor existente
    def delete_reactor_by_id(self, reactor_id):
        return self.reactor_repository.delete_reactor_by_id(reactor_id)
    
    # 
    def update_reactor(self, reactor):
        return self.reactor_repository.update_reactor(reactor)
    
    # 8. Obtener Ubicaciones Registradas
    def get_all_locations(self):
        return self.reactor_repository.get_all_locations()
    
    # 
    def get_locations_by_id(self):
        return self.reactor_repository.get_locations_by_id()
    
    #
    def get_reactor_by_location(self):
        return self.reactor_repository.get_reactor_by_location()
    

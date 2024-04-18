from repository.reactor_repository import ReactorRepository

class ReactorService:
    def __init__(self):
        self.reactor_repository = ReactorRepository()

    def get_all_reactors(self):
        return self.reactor_repository.get_all_reactors()
    def create_reactor(self, reactor):
        return self.reactor_repository.create_reactor(reactor)
    
    def get_reactor_by_id(self, reactor_id):
        return self.reactor_repository.reactor_by_id(reactor_id)
    
    def get_all_types_reactor(self):
        return self.reactor_repository.get_all_types_reactor()
    
    def get_reactors_by_type_id(self, reactor_id):
        return self.reactor_repository.get_reactors_by_type_id(reactor_id)
    
    def delete_reactor(self, reactor_id):
        return self.reactor_repository.delete_reactor(reactor_id)
    
    def update_reactor(self, reactor):
        return self.reactor_repository.update_reactor(reactor)
    

from repository.reactor_repository import ReactorRepository

class ReactorService:
    def __init__(self):
        self.reactor_repository = ReactorRepository()

    def get_all_reactors(self):
        return self.reactor_repository.get_all_reactors()
    def create_reactor(self, reactor):
        return self.reactor_repository.create_reactor(reactor)

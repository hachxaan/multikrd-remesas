



from src.remittances.infraestructure.microservices.solid.singleton import SolidOperationSingleton
from src.remittances.infraestructure.microservices.solid.solid_operation import SolidOperation


class SolidService:
    
    def transfer(self):
        solid = SolidOperation(instance=SolidOperationSingleton.instance)
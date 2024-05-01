class EntityNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Entity is not found."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        

class NewUserRoleNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="New user role is not found."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class ProductEntityNotFound(Exception):
    def __init__(self, status_code:int=400, message:str="Product is not found."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        
class RoleEntityNotFound(Exception):
    def __init__(self, status_code:int=400, message:str="Role is not found."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        
class UnauthorizedError(Exception):
    def __init__(self, status_code:int=401, message:str="User is unauthorized"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)     
        
class ServerInvalidError(Exception):
    def __init__(self, status_code:int=400, message:str="Invalid server type."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        
class  NotAcceptableError(Exception):
    def __init__(self, status_code:int=406, message:str="Not acceptable"):
        self.status_code = status_code
        self.message = message      
        super().__init__(self.message)
        
class AchknowledgementError(Exception):
    def __init__(self, message:str="Invalid Operation"):
        self.message = message
        super().__init__(self.message)  
        
class ImproperConfigurationError(Exception):
    def __init__(self, message:str="Problem with MongoDB environment variables") -> None:
        super().__init__(message)
        
# Error class with 403 status when more than one restaurant is created for local machine
class RestaurantAlreadyExistsError(Exception):
    def __init__(self, status_code:int=403, message:str="Restaurant already exists"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class ServiceProviderNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Service Provider ID does not exist."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class ProductNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Product Item does not exist."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class RecipeItemNotFoundError(Exception):
    def __init__(self, status_code:int=400, message:str="Can not take order. Recipe Item does not exist in the Inventory."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
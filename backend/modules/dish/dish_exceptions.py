from typing import Any

from shared.utils.app_exceptions import AppExceptionCase

class DishExceptions:
    class DishCreateException(AppExceptionCase):
        def __init__(self, msg:str =""):
            status_code = 500
            msg = "Error creando plato"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class DishNotFoundException(AppExceptionCase):

        def __init__(self, msg: str = ""):
            status_code = 404
            msg = "Id de plato no encontrado"
            AppExceptionCase.__init__(self,status_code,msg)
        
    class DishInvalidUpdateParamsException(AppExceptionCase):

        def __init__(self, msg: str = "", e: Any = None):
            error = e
            status_code = 422
            msg = f"Parametros de actualizacion invalidos: {str(error)}"
            AppExceptionCase.__init__(self,status_code,msg)

    class DishListsException(AppExceptionCase):

        def __init__(self, msg: str = ""):
            status_code = 500
            msg = " No se pudo recuperar la lista de platos"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class DishWithNoNameException(AppExceptionCase):
        """
        Dish with no name creation failed
        """
        def __init__(self, msg: str = ""):
            status_code = 422
            msg = "El plato debe tener un nombre"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class DishWithNoPriceException(AppExceptionCase):
        """
        Dish with no price creation failed
        """
        def __init__(self, msg: str =""):
            status_code = 422
            msg = "El plato debe tener un precio"
            AppExceptionCase.__init__(self,status_code, msg)

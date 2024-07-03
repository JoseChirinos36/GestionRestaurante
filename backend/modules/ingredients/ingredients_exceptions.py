from typing import Any

from shared.utils.app_exceptions import AppExceptionCase

class IngredientExceptions:
    class IngredientCreateException(AppExceptionCase):
        def __init__(self, msg:str =""):
            status_code = 500
            msg = "Error creando el ingrediente"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class IngredientNotFoundException(AppExceptionCase):

        def __init__(self, msg: str = ""):
            status_code = 404
            msg = "Id de ingrediente no encontrado"
            AppExceptionCase.__init__(self,status_code,msg)
        
    class IngredientInvalidUpdateParamsException(AppExceptionCase):

        def __init__(self, msg: str = "", e: Any = None):
            error = e
            status_code = 422
            msg = f"Parametros de actualizacion invalidos: {str(error)}"
            AppExceptionCase.__init__(self,status_code,msg)

    class IngredientListsException(AppExceptionCase):

        def __init__(self, msg: str = ""):
            status_code = 500
            msg = " No se pudo recuperar la lista de ingredientes"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class IngredientWithNoNameException(AppExceptionCase):
        """
        Ingredient with no name creation failed
        """
        def __init__(self, msg: str = ""):
            status_code = 422
            msg = "El ingrediente debe tener un nombre"
            AppExceptionCase.__init__(self,status_code,msg)
    
    class IngredientWithNoAmountException(AppExceptionCase):
        """
        Ingredient with no amount creation failed
        """
        def __init__(self, msg: str =""):
            status_code = 422
            msg = "El ingrediente debe tener una cantidad"
            AppExceptionCase.__init__(self,status_code, msg)

    class IngredientWithNoUnitException(AppExceptionCase):
        """
        Ingredient with no unit creation failed
        """
        def __init__(self, msg: str =""):
            status_code = 422
            msg = "El ingrediente debe tener una unidad de medida"
            AppExceptionCase.__init__(self,status_code, msg)

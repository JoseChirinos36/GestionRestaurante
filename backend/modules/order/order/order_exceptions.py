from typing import Any

from shared.utils.app_exceptions import AppExceptionCase

class OrderExceptions:
    class OrderCreateException(AppExceptionCase):
        def __init__(self, msg: str =""):
            status_code = 500
            msg = "Error creando pedido"
            AppExceptionCase.__init__(self, status_code, msg)

    
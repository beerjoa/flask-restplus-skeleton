class CustomError:
    def __init__(self):
        self.code = 'e000'
        self.message = 'default error'
        self.custom_msg = ''
        self.errors = {
            "e000": "default error",
            "e001": "error type1",
            "e002": "error type2",
            "e201": "error type2",
            "e400": "error type3",
            "e403": "error type4",
            "e500": "error type5",
        }

    def error_format(self, code='e000', custom_msg='default error'):
        self.code = code
        self.custom_msg = custom_msg
        return {"code": self.code, "message": self.errors[code], "custom_msg": self.custom_msg}

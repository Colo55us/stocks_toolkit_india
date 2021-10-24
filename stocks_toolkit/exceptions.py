class IllegalArgumentError(ValueError):
    pass

class DataNotFound(AttributeError):
    def __init__(self, message):
        self.message = message
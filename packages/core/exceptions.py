class InvalidTrafficDataError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class AnomalyDetectionError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
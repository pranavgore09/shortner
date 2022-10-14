class BaseCustomException(Exception):

    def __init__(self, message):
        self.message = message
        super(BaseCustomException, self).__init__(message)

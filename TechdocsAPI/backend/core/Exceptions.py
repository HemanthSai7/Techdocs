import json

from backend.models import GeneralResponse, TokenSchema


class InvalidCredentialsException(Exception):
    def __init__(self, token_result: GeneralResponse):
        self.token_result = token_result
        self.set_statuses()
        super(InvalidCredentialsException, self).__init__()

    def set_statuses(self):
        self.token_result.status = 'login_failed'

    def __repr__(self):
        return "exception.InvalidCredentialsException()"

class ExistingUserException(Exception):
    def __init__(self, response_result: GeneralResponse):
        self.response_result = response_result
        self.set_statuses()
        super(ExistingUserException, self).__init__()

    def set_statuses(self):
        self.response_result.status = f'failed'
        self.response_result.message.append(f'user with this AADHAR Number already has an account')
        self.response_result.message[0] = 'authenticated'

    def __repr__(self):
        return "exception.ExistingUserException()"
    
class InfoNotFoundException(Exception):
    def __init__(self, response_result: GeneralResponse, message: str):
        self.response_result = response_result
        self.message = message
        self.set_statuses()
        super(InfoNotFoundException, self).__init__(message)

    def set_statuses(self):
        self.response_result['status'] = 'abort'
        self.response_result['message'][0] = 'authenticated'
        self.response_result['message'].append(self.message)

    def __repr__(self):
        return "exception.InfoNotFoundException()"


class EmailNotVerifiedException(Exception):
    def __init__(self):
        self.set_statuses()
        super(EmailNotVerifiedException, self).__init__()

    def set_statuses(self):
        self.status = 'EmailNotVerifiedException'

    def __repr__(self):
        return "exception.EmailNotVerifiedException()"


class EmailNotSentException(Exception):
    def __init__(self):
        self.set_statuses()
        super(EmailNotSentException, self).__init__()

    def set_statuses(self):
        self.status = 'EmailNotSentException'

    def __repr__(self):
        return "exception.EmailNotSentException()"
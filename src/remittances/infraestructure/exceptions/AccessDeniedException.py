

from src.shared.ddd.domain.model.exceptions.DomainException import DomainException


class AccessDeniedException(DomainException):

    def __init__(self, message=None):
        super().__init__('NOT_AUTH', message)

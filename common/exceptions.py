"""
Exceptions used in overall project.
Feel free to add new ones as they fit.

Format of exception:
Kinda flexible as it must ALWAYS contain a relevant message to
ease debugging and fixing (or notifying coder about something).
You may put only the message or make initialization to put
some extra prefix to recognize class/method/any-relevant-object.
"""
from .utils import get_logger

logger = get_logger('mobi_exception')


class BaseException(Exception):
    """Global exception class for Movi."""

    def __init__(self, message=None):
        """Do something useful with extra params."""
        # Call the base class constructor with the parameters it needs
        logger.error("Exception raised: %s", message)
        super().__init__(message)
        self.message = message

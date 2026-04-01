"""Custom exception definitions for the application."""


class NewSystemError(Exception):
    """A general error has occurred in the application."""

    pass


class APIKeyError(NewSystemError):
    """An error has occurred related to API key issues."""

    pass
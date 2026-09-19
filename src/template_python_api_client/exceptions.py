"""Project-specific API client exceptions."""


class TemplatePythonApiClientError(Exception):
    """Base exception for API client failures."""


class ApiResponseError(TemplatePythonApiClientError):
    """Raised when an API response cannot be accepted."""

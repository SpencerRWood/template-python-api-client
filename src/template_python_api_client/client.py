"""HTTP client facade for the target API."""

from typing import Any


class ApiClient:
    """Placeholder API client."""

    def fetch_resource(self, _resource_id: str) -> dict[str, Any]:
        """Fetch one API resource."""
        # TODO: Implement HTTP request and response handling.
        raise NotImplementedError

    def fetch_page(self, _cursor: str | None = None) -> dict[str, Any]:
        """Fetch one paginated API response."""
        # TODO: Implement pagination handling.
        raise NotImplementedError

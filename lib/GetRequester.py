import json
import requests


class GetRequester:
    """Fetches data from a URL and returns the response body or parsed JSON."""

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to the URL and return the raw response body."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Return the response body parsed into Python data (list/dict)."""
        return json.loads(self.get_response_body())
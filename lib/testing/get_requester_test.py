from GetRequester import GetRequester

URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"


def test_get_response_body():
    """get_response_body returns the raw bytes from the URL."""
    requester = GetRequester(URL)
    body = requester.get_response_body()
    assert isinstance(body, bytes)
    assert b"Daniel" in body
    assert b"Joe" in body
    assert b"Avi" in body
    assert b"Howard" in body


def test_load_json():
    """load_json returns a list of dictionaries."""
    requester = GetRequester(URL)
    data = requester.load_json()
    assert isinstance(data, list)
    assert data[0]["name"] == "Daniel"
    assert data[0]["occupation"] == "LG Fridge Salesman"
    assert data[1]["name"] == "Joe"
    assert data[1]["occupation"] == "WiFi Fixer"
    assert data[2]["name"] == "Avi"
    assert data[2]["occupation"] == "DJ"
    assert data[3]["name"] == "Howard"
    assert data[3]["occupation"] == "Mountain Legend"
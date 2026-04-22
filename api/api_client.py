import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    return requests.get(f"{BASE_URL}/posts")

def create_post(title, body):
    return requests.post(f"{BASE_URL}/posts", json={
        "title": title,
        "body": body
    })
def test_response_structure():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()

    assert isinstance(data, list)
    assert "id" in data[0]
    assert "title" in data[0]
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    return requests.get(f"{BASE_URL}/posts")

def create_post(title, body):
    return requests.post(f"{BASE_URL}/posts", json={
        "title": title,
        "body": body
    })
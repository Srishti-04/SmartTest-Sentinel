import requests
from api.api_client import get_posts, create_post
from utils.logger import get_logger
logger = get_logger()

def test_get_posts():
    logger.info("Testing GET /posts API")
    
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    logger.info(f"Status Code: {response.status_code}")

    assert response.status_code == 200

def test_create_post():
    res = create_post("Test", "Body")
    assert res.status_code == 201
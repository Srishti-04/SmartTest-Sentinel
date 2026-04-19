from api.api_client import get_posts, create_post

def test_get_posts():
    res = get_posts()
    assert res.status_code == 200
    assert len(res.json()) > 0

def test_create_post():
    res = create_post("Test", "Body")
    assert res.status_code == 201
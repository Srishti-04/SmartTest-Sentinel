import requests
import time

def test_api_performance():
    url = "https://jsonplaceholder.typicode.com/posts"

    times = []

    for _ in range(10):
        start = time.time()
        response = requests.get(url)
        end = time.time()

        assert response.status_code == 200
        times.append(end - start)

    avg_time = sum(times) / len(times)

    print(f"Average Response Time: {avg_time}")

    assert avg_time < 1
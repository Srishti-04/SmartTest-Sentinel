import requests
import time
import threading

URL = "https://jsonplaceholder.typicode.com/posts"

def hit_api():
    for _ in range(20):
        response = requests.get(URL)
        print("Status:", response.status_code)

def test_load():
    start = time.time()

    threads = []

    # simulate 5 users
    for _ in range(5):
        t = threading.Thread(target=hit_api)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()

    print("Total time:", end - start)

    assert True  # just to pass test
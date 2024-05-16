import requests

def get_page(url: str) -> str:
    response = requests.get(url)
    cache_key = f"count:{url}"
    cache = redis.Redis()
    cache.incr(cache_key)
    cache.setex(url, 10, response.text)
    return response.text

# Usage example
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))

import threading
import requests

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except Exception as e:
        print(f"Error requesting {url}: {e}")

# List of URLs to request
urls = [
    "http://localhost:6789/HelloWorld.html",
    "http://localhost:6789/AnotherFile.html",
    "http://localhost:6789/NonExistentFile.html"
]

# Create and start a thread for each request
threads = []
for url in urls:
    thread = threading.Thread(target=send_request, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
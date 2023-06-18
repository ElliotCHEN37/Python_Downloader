import requests
from threading import Thread

def download():
    url = input("Paste your download link here: ")
    filename = input("Enter your file name here: ")
    proxy = input("Please enter your HTTPS Proxy server IP and port here (press Enter if not using a proxy): ")

    session = requests.Session()
    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}

    try:
        response = session.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024

        def download_thread():
            downloaded_size = 0
            with open(filename, 'wb') as f:
                for data in response.iter_content(block_size):
                    f.write(data)
                    downloaded_size += len(data)
                    progress = downloaded_size / total_size * 100
                    print("Downloading ({:.2f}%)".format(progress))

                print("Download complete")

        download_thread = Thread(target=download_thread)
        download_thread.start()

    except requests.exceptions.RequestException as e:
        print("Error:", e)

print("Python Downloader Multi-threaded Edition v1.2.3 - Command line version")
print("Author: Elliot")
print("Version: 1.2.3")
download()
webbrowser.open("https://sites.google.com/view/pydl/index")

import requests
from tqdm import tqdm

def download(url: str, file_name: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    head = requests.head(url, headers=headers)
    file_size = head.headers.get('Content-Length')
    if file_size is not None:
        file_size = int(file_size)
    response = requests.get(url, headers=headers, stream=True)
    chunk_size = 1024
    bar = tqdm(total=file_size, desc=f'下載 {file_name} 中/Downloading {file_name} | 進度/progress rate')
    with open(file_name, mode='wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
    bar.close()


if "__main__" == __name__:
    print(f"歡迎使用Python Downloader!/Thank you for choosing Python Downloader!")
    url = input("請輸入下載鏈接/Please paste the download link here：")
    file_name = input("請輸入完整檔案名/Please type your file name：")
    download(url, file_name)
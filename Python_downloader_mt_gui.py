import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
import requests
import json
import time


def check_update():
    json_url = "https://raw.githubusercontent.com/ElliotCHEN37/Python_Downloader/main/update.json"

    try:
        response = requests.get(json_url)
        response.raise_for_status()
        update_info = response.json()

        latest_version = update_info["version"]
        download_link = update_info["download_link"]

        if latest_version != "1.2.4":
            response = messagebox.askyesno("Update!", "New version is available, would you like to update?")
            if response == tk.YES:
                webbrowser.open(download_link)
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        messagebox.showerror("Error", str(e))

def download():
    url = url_entry.get()
    filename = filename_entry.get()
    proxy = proxy_entry.get()

    session = requests.Session()
    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}

    try:
        response = session.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024

        start_time = time.time()
        downloaded_size = 0
        with open(filename, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                downloaded_size += len(data)
                progress = downloaded_size / total_size * 100
                progress_bar["value"] = progress
                root.update()
                elapsed_time = time.time() - start_time
                download_speed = downloaded_size / (1024 * elapsed_time)  # Speed in KB/s
                remaining_size = total_size - downloaded_size
                remaining_time = remaining_size / (1024 * download_speed) / 60 if download_speed > 0 else 0  # Time in minutes
                complete_label.config(text="Downloading ({:.2f}%)\nSpeed: {:.2f} KB/s\nEstimated Time: {:.2f} minutes".format(progress, download_speed, remaining_time))

            complete_label.config(text="Download complete\nTotal Time: {:.2f} minutes".format((time.time() - start_time) / 60))

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))

def show_about():
    messagebox.showinfo("About", "Python Downloader\n\nAuthor: Elliot\nVersion: 1.2.4")

def open_link(event):
    webbrowser.open("https://sites.google.com/view/pydl/index")

def read_proxy_config():
    try:
        with open("config.json") as f:
            config = json.load(f)
            if "proxy" in config:
                proxy_config = config["proxy"]
                if "http" in proxy_config:
                    http_proxy = proxy_config["http"]
                    proxy_entry.insert(0, http_proxy)
                if "https" in proxy_config:
                    https_proxy = proxy_config["https"]
                    proxy_entry.insert(0, https_proxy)
    except FileNotFoundError:
        pass

def check_update():
    json_url = "https://example.com/update.json"

    try:
        response = requests.get(json_url)
        response.raise_for_status()
        update_info = response.json()

        latest_version = update_info["version"]
        download_link = update_info["download_link"]

        if latest_version != "v1.2.4":
            response = messagebox.askyesno("Update!", "New version is available, would you like to update?")
            if response == tk.YES:
                webbrowser.open(download_link)
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Python Downloader Multi-threaded Edition v1.2.4 - GUI version")
root.geometry("600x310")
root.iconbitmap("pydl.ico")

download_label = tk.Label(root, text="Paste your download link here:")
download_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

filename_label = tk.Label(root, text="Enter your file name here:")
filename_label.pack()

filename_entry = tk.Entry(root, width=50)
filename_entry.pack()

proxy_label = tk.Label(root, text="Please enter your HTTPS Proxy server IP and port here:")
proxy_label.pack()

proxy_label2 = tk.Label(root, text="(The program will automatically read the 'config.json file' if it is available.)")
proxy_label2.pack()

proxy_entry = tk.Entry(root, width=50)
proxy_entry.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack()

complete_label = tk.Label(root, text="", font=("Arial", 12))
complete_label.pack()

download_button = tk.Button(root, text="Download", command=download, cursor="hand2")
download_button.pack()

update_button = tk.Button(root, text="Check for update", command=check_update, cursor="hand2")
update_button.pack()

about_button = tk.Button(root, text="About", command=show_about, cursor="hand2")
about_button.pack()

link_label = tk.Label(root, text="Visit official site", cursor="hand2")
link_label.pack()
link_label.bind("<Button-1>", open_link)

read_proxy_config()

check_update()

root.mainloop()

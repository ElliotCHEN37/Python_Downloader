import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
import requests

win = tk.Tk()
win.title("Python Downloader Standard Edition v1.2.1 - GUI version")
win.geometry("600x300")
win.iconbitmap("pydl.ico")

ul = tk.Label(text="Paste your download link here:")
ul.pack()

url_entry = tk.Entry(win, width=50)
url_entry.pack()

fn = tk.Label(text="Enter your file name here:")
fn.pack()

filename_entry = tk.Entry(win, width=50)
filename_entry.pack()

progress_bar = ttk.Progressbar(win, orient="horizontal", length=400, mode="determinate")
progress_bar.pack()

complete_label = tk.Label(win, text="", font=("Arial", 12))
complete_label.pack()

def download():
    url = url_entry.get()
    filename = filename_entry.get()

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024

    with open(filename, 'wb') as f:
        downloaded_size = 0
        for data in response.iter_content(block_size):
            f.write(data)
            downloaded_size += len(data)
            progress = downloaded_size / total_size * 100
            progress_bar["value"] = progress
            win.update()

    complete_label.config(text="Download complete")

download_button = tk.Button(win, text="Download", command=download)
download_button.pack()

def show_about():
    messagebox.showinfo("About", "Python Downloader. \n\nAuthor: Elliot\nVersion: 1.2")

about_button = tk.Button(win, text="About", command=show_about)
about_button.pack()

def open_link(event):
    webbrowser.open("https://sites.google.com/view/pydl/index")

link_label = tk.Label(win, text="Visit official site", cursor="hand2")
link_label.pack()
link_label.bind("<Button-1>", open_link)

win.mainloop()

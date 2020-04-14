from bitlyshortener import Shortener
import tkinter as tk
import settings

tokens_pool = [settings.BITLY_TOKEN]
shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)

window = tk.Tk()
window.geometry('300x300')
window.title('URL shortener')

label = tk.Label(text='Enter URL ("https://***.***/") to shorten')
label.pack()

entry = tk.Entry()
entry.pack()


def shorten():
    d = entry.get()
    url = [d]
    global s
    s = shortener.shorten_urls(url)

    w = tk.Message(window, text=f'{d}: {s[0]}')
    w.config(width=300)
    w.pack()

    clipboard_button()

def clipboard_button():
    n = tk.Button(window,text='Copy to Clipboard', command=append_to_clipboard)
    n.pack()

def append_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(s)


b = tk.Button(window, text='Shorten', command=shorten)
b.pack()

window.mainloop()
import tkinter as tk
from tkinter import messagebox, filedialog
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

class WebAnalyzerApp:
    def __init__(self, root):
        self.root = root
       root.title("Web Analyzer")
self.create_widgets()
self.keywords = []
self.site_data = []
def create_widgets(self):
    # First Interface
    self.url_label = tk.Label(self.root, text="Enter URL:")
    self.url_label.pack()

    self.url_entry = tk.Entry(self.root, width=50)
    self.url_entry.pack()

    self.keywords_label = tk.Label(self.root, text="Enter Keywords (comma-separated):")
    self.keywords_label.pack()

    self.keywords_entry = tk.Entry(self.root, width=50)
    self.keywords_entry.pack()

    self.analyze_button = tk.Button(self.root, text="Analyze", command=self.analyze)
    self.analyze_button.pack()

def analyze(self):
    url = self.url_entry.get()
    self.keywords = [kw.strip() for kw in self.keywords_entry.get().split(',')]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            self.parse_page(response.text, url)
            self.show_results()
        else:
            messagebox.showerror("Error", "Failed to retrieve the webpage.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def parse_page(self, html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a', href=True)
    images = soup.find_all('img')

    # Calculate internal and external links
    internal_links = []
    external_links = []

    for anchor in anchors:
        href = anchor['href']
        full_url = urljoin(base_url, href)
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            internal_links.append(full_url)
        else:
            external_links.append(full_url)

    # Calculate percentage of images with alt tags
    images_with_alt = [img for img in images if img.get('alt')]
    images_alt_percentage = (len(images_with_alt) / len(images)) * 100 if images else 0

    # Keyword analysis (placeholder for actual implementation

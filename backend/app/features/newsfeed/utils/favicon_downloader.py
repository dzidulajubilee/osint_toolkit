import requests
from urllib.parse import urlparse, urljoin


class FaviconDownloader:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def get_favicon(self, url: str):
        """
        Return favicon URL if available, otherwise None
        """
        try:
            if not url.startswith(("http://", "https://")):
                url = "http://" + url

            parsed = urlparse(url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            favicon_url = urljoin(base_url, "/favicon.ico")

            response = requests.head(favicon_url, timeout=self.timeout)

            if response.status_code == 200:
                return favicon_url

            return None

        except Exception as e:
            print(f"[FaviconDownloader] Error: {e}")
            return None

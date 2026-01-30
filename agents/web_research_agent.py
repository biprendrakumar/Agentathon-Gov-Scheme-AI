import time
from collections import deque
from typing import List
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class WebResearchAgent:
    """Simple focused web crawler to find government policy pages.

    Notes:
    - This is a lightweight, opinionated crawler for demonstration only.
    - It does not follow robots.txt, rate-limiting is implemented via sleep.
    - For production use, respect robots.txt, add retries, backoff and error handling.
    """

    DEFAULT_SEEDS = [
        "https://www.india.gov.in/",
        "https://www.mygov.in/",
        "https://www.pmindia.gov.in/",
    ]

    KEYWORDS = [
        "policy",
        "scheme",
        "notification",
        "guidelines",
        "act",
        "regulation",
        "compliance",
    ]

    def __init__(self, allowed_domain_suffix="gov.in", max_pages=50, delay=1.0):
        self.allowed_domain_suffix = allowed_domain_suffix
        self.max_pages = max_pages
        self.delay = delay

    def _is_allowed(self, url: str) -> bool:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        return hostname.endswith(self.allowed_domain_suffix) or hostname.endswith("gov.in")

    def _fetch(self, url: str):
        headers = {"User-Agent": "Agentathon-WebResearch/1.0 (+https://example.com)"}
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            if resp.status_code == 200 and 'text/html' in resp.headers.get('Content-Type', ''):
                return resp.text
        except requests.RequestException:
            return None

    def _extract_links(self, html: str, base: str) -> List[str]:
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full = urljoin(base, href)
            if full.startswith("http"):
                links.append(full)
        return links

    def _extract_summary(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        p = soup.find("p")
        excerpt = p.get_text(strip=True) if p else ""
        return title, excerpt

    def find_policies(self, seeds: List[str] = None, max_results: int = 20):
        """Crawl seed pages and return discovered policy-like pages.

        Returns a list of dicts with `name`, `url`, and `summary`.
        """
        seeds = seeds or self.DEFAULT_SEEDS
        visited = set()
        q = deque(seeds)
        found = []

        while q and len(visited) < self.max_pages and len(found) < max_results:
            url = q.popleft()
            if url in visited:
                continue
            visited.add(url)

            if not self._is_allowed(url):
                continue

            html = self._fetch(url)
            time.sleep(self.delay)
            if not html:
                continue

            title, excerpt = self._extract_summary(html)
            text = (title + " " + excerpt).lower()
            if any(k in text for k in self.KEYWORDS):
                found.append({"name": title or url, "url": url, "summary": excerpt})

            # enqueue discovered links (same domain)
            for link in self._extract_links(html, url):
                if link not in visited and self._is_allowed(link):
                    q.append(link)

        return found

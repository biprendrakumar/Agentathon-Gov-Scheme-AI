# Agentathon Gov Scheme AI

Minimal demo showing a multi-agent pipeline that finds government schemes for a user.

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the demo script:

```bash
python main.py
```

3. For the Streamlit UI:

```bash
streamlit run app/streamlit_app.py
```

Run tests:

```bash
pytest -q
```

Purpose: small, easy-to-extend demo for searching and localizing scheme information.

Web research agent

You can augment local dataset results by crawling government websites for policy pages. Example usage from Python:

```py
from core.coordinator import CoordinatorAgent

user = {"age":22, "income":180000, "occupation":"student", "language":"en"}
agent = CoordinatorAgent()
results = agent.run_with_web(user, seeds=["https://www.india.gov.in/"], max_results=10)
for r in results:
	print(r["name"], '-', r.get("benefit") or r.get("summary"))
```

Notes:
- The web crawler uses `requests` + `beautifulsoup4` and limits to `gov.in` domains by default.
- The crawler is a simple demo; for production use, add `robots.txt` handling, retries, proxies and rate-limiting.

# Web Scraper Project

This is a simple Python web scraping project using `beautifulsoup4`, `requests`, and `lxml`. It uses `uv` as the package manager for fast installs and virtual environment management.

## Setup

### 1. Install `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

### 2. Install dependencies

```bash
uv pip install -r requirements.txt
```

Or with a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 3. ChromeDriver (Optional)

If your scraping target requires a browser (e.g., JS rendering), install ChromeDriver:

- Find your Chrome version at `chrome://settings/help`
- Download matching ChromeDriver from: https://sites.google.com/chromium.org/driver/
- Add it to your system `PATH` or the project directory

## Requirements

These were installed using `uv`:

- beautifulsoup4
- certifi
- charset-normalizer
- idna
- lxml
- requests
- soupsieve
- typing-extensions
- urllib3

## Project Structure

```
project-root/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── chromedriver (optional)
```

## .gitignore includes

- `.venv/`
- `__pycache__/`
- `.idea/`
- `.DS_Store`
- `chromedriver` (optional)

## Notes

- Respect `robots.txt` and site terms of service
- Add request delays to avoid IP bans
- Use headless browsers like Selenium for JavaScript-heavy content (not included here)

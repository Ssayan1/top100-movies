# 🎬 Top 100 Movies Scraper

This Python script scrapes the **Empire Online** list of the best movies and saves them into a `movie.txt` file in reverse order.

## 📌 Features
- Fetches HTML content from the Empire Online *Best Movies* page.
- Extracts movie titles using `BeautifulSoup`.
- Cleans unwanted text (e.g., "Starring:", "Director:").
- Saves the movie list in reverse order to a text file.

## 🛠 Requirements
Make sure you have Python installed, then install the required dependencies:

```bash
pip install requests beautifulsoup4
```
## ▶ Usage
1. Clone this repository or download the script.
2. Run the script:
```bash
python main.py
```
3. The script will create a file named movie.txt containing the list of movies.

## 📂 Output Example
```python-repl
The Godfather
The Shawshank Redemption
Pulp Fiction
...
```
## ⚠ Notes
- The script depends on the HTML structure of the Empire Online website. If the site changes, selectors may need updating.
- For personal/educational use only. Respect the target site's terms of service.

## 📜 License
```yml
---

If you want, I can also **add a nice banner and project badges** so your GitHub README looks more professional and eye-catching.  
Want me to make that version?
```


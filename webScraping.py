from bs4 import BeautifulSoup, Comment
import requests
import re

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = [a["href"] for a in soup.find_all("a", href=True)]
print("Enlaces encontrados:")
print(links)

comments = [str(comment) for comment in soup.find_all(
    string=lambda text: isinstance(text, Comment))]
print("\nComentarios encontrados:")
print(comments)

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, response.text)
print("\nCorreos electrónicos encontrados:")
print(emails)

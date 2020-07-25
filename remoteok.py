import requests
from bs4 import BeautifulSoup

HOMEPAGE = "https://remoteok.io/"
# https://remoteok.io/remote-dev+python-jobs

def extract_job(html):
  title = html.find("h2", {"itemprop": "title"}).text.strip()
  company = html.find("h3", {"itemprop": "name"}).text.strip()
  link = f'{HOMEPAGE}l/' + html['data-id']
  by = 'Remote OK'
  return {"title": title, "company": company, "link": link, 'by':by}

def extract_jobs(url):
  jobs = []
  print(f"Now scraping Remote OK")
  res = requests.get(url)
  soup = BeautifulSoup(res.text, "html.parser")
  ress = soup.find_all("tr", {"class": "job"})
  for res in ress:
    job = extract_job(res)
    jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)
  return jobs

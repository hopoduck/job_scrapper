import requests
from bs4 import BeautifulSoup

HOMEPAGE = "https://weworkremotely.com"
# https://weworkremotely.com/remote-jobs/search?term=python


def extract_job(html):
    title = html.find("span", {"class": "title"}).text.strip()
    company = html.find("span", {"class": "company"}).text.strip()
    link = HOMEPAGE + html.find("a", recursive=False)['href']
    by = 'WeWorkRemotely'
    return {"title": title, "company": company, "link": link, "by": by}


def extract_jobs(url):
    jobs = []
    print(f"Now scraping WeWorkRemotely page")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    ress = soup.find_all("li", {"class": "feature"})
    for res in ress:
        job = extract_job(res)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)
    return jobs

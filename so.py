# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

HOMEPAGE = "https://stackoverflow.com"
# https://stackoverflow.com/jobs?r=true&q=python


def get_last_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    pages = soup.find_all("a", {"class":  "s-pagination--item"})
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("a", {"class": "s-link"})['title']
    company = html.find("h3", {"class": "fc-black-700"}
                        ).find("span").get_text(strip=True)
    link = HOMEPAGE + html.find("a", {"class": "s-link"})['href']
    by = 'Stack Overflow'
    return {"title": title, "company": company, "link": link, 'by': by}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Now scraping Stackoverflow {page+1} page")
        res = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(res.text, "html.parser")
        ress = soup.find_all("div", {"class": "-job"})
        for res in ress:
            job = extract_job(res)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?r=true&q={word}"
    last_page = get_last_page(url)
    # last_page = 5
    jobs = extract_jobs(last_page, url)
    return jobs

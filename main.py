"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
import csv
import random
from bs4 import BeautifulSoup
from flask import Flask, request, redirect, render_template, flash
from so import get_jobs as so_get_jobs
from remoteok import get_jobs as remoteok_get_jobs
from wwr import get_jobs as wwr_get_jobs


db = {}


def listappend(*datalist):
    save_list = []
    for data in datalist:
        for d in data:
            save_list.append(d)
    return save_list


app = Flask('job scrapper')


@app.route('/')
def home():
    return render_template(
        'home.html',
    )


@app.route('/view')
def view():
    wannajob = request.args.get('wannajob')
    jobs = {}
    try:
        from_db = db.get(wannajob)
        if from_db:
            db[wannajob] = from_db
        else:
            jobs['so'] = so_get_jobs(wannajob)
            jobs['ro'] = remoteok_get_jobs(wannajob)
            jobs['wwr'] = wwr_get_jobs(wannajob)
            db[wannajob] = listappend(jobs['so'], jobs['ro'], jobs['wwr'])
            random.shuffle(db[wannajob])
        return render_template(
            'view.html',
            wannajob=wannajob,
            db=db
        )
    except:
        error = "Not found"
        return render_template(
            'view.html',
            error=error
        )


@app.route('/export')
def export():
    pass


app.run(host='127.0.0.1')

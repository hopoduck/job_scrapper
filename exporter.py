# -*- coding: utf-8 -*-
import csv


def export_file(db, wannajob):
    file_name = f"static/results/{wannajob}.csv"
    file = open(file_name, mode='w', encoding='utf-8', newline="")
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Website', 'Link'])
    for job in db:
        writer.writerow([job['title'], job['company'], job['by'], job['link']])
    file.close()
    return file_name

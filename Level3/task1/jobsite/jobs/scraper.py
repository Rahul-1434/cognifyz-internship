import requests
from bs4 import BeautifulSoup

def get_job_listings():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_cards = soup.find_all('div', class_='card-content')

    for job in job_cards:
        title = job.find('h2', class_='title').text.strip()
        company = job.find('h3', class_='company').text.strip()
        location = job.find('p', class_='location').text.strip()
        date = job.find('time')['datetime'] if job.find('time') else 'N/A'

        apply_tag = job.find('a', text='Apply')
        apply_link = apply_tag['href'] if apply_tag else '#'

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'date': date,
            'apply_link': apply_link
        })

    return jobs

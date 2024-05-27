import Functions.GetURLParams as gup
import Functions.Export_to_Excel as ex
from Functions.list_p import processed_strings as data
import requests
from bs4 import BeautifulSoup
import xlwt
import tempfile
import os
from collections import defaultdict
from multiprocessing import Pool
import time
start_time = time.time()
def scrape_profile(profile):
    try:
        URL = f'https://internshala.com/internships/{profile}-internship/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        max_pages = int(soup.find(id='total_pages').text.strip())
        print(f'Total Pages for {profile}: {max_pages}')
        temp_data = []
        for i in range(max_pages):
            page_url = URL + f'/page-{i+1}'
            page = requests.get(page_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            intern_titles = soup.find_all(class_='individual_internship')
            if len(intern_titles) == 0:
                continue
            print(f'--------------Scraping Page {i+1} for {profile} -----------------')
            for title in intern_titles:
                cta_container = title.find(class_='cta_container')
                if cta_container:
                    elem = cta_container.find('a', href=True)
                sub_URL = 'https://internshala.com' + str(elem['href'])
                sub_page = requests.get(sub_URL)
                sub_soup = BeautifulSoup(sub_page.content, 'html.parser')
                try:
                    title_raw = sub_soup.find(class_='heading_4_5 profile')
                    title1 = title_raw.text.strip()
                except (IndexError, AttributeError):
                    title1 = "N/A"
                try:
                    skills_raw = sub_soup.find_all(class_='round_tabs_container')[0]
                    skills = ', '.join([i.text.strip() for i in skills_raw.find_all(class_='round_tabs')])
                except (IndexError, AttributeError):
                    skills = "N/A"
                try:
                    perks_raw = sub_soup.find_all(class_='round_tabs_container')[1]
                    perks = ', '.join([i.text.strip() for i in perks_raw.find_all(class_='round_tabs')])
                except (IndexError, AttributeError):
                    perks = "N/A"
                try:
                    internship_details = sub_soup.find(class_='internship_details')
                    text_containers = internship_details.find_all(class_='text-container')
                    valid_text_containers = []
                    for container in text_containers:
                        text = container.text.strip()
                        if text.replace(" ", "").isdigit():
                            valid_text_containers.append(text)
                    if valid_text_containers:
                        openings = valid_text_containers[-1]
                    else:
                        openings = "N/A"
                except IndexError as e:
                    print(f"Error extracting openings: {e}")
                    openings = "N/A"
                temp_data.append({
                    'internship_title': title1,
                    'company': '',
                    'location': '',
                    'start by': '',
                    'apply by': '',
                    'duration': '',
                    'stipend': '',
                    'applicants': '',
                    'skills': skills,
                    'perks': perks,
                    'openings': openings,
                    'link': sub_URL,
                    'profile': profile
                })
                try:
                    company = sub_soup.find(class_='heading_6 company_name').text.strip()
                except (AttributeError, TypeError) as e:
                    print(f"Error extracting company: {e}")
                else:
                    temp_data[-1]['company'] = company
                try:
                    location = sub_soup.find(id='location_names').find('a').text.strip()
                except (AttributeError, TypeError) as e:
                    print(f"Error extracting location: {e}")
                else:
                    temp_data[-1]['location'] = location
                try:
                    start_by = sub_soup.find(class_='item_body').find_next(class_='start_immediately_desktop').text.strip()
                except (AttributeError, TypeError) as e:
                    print(f"Error extracting start by date: {e}")
                else:
                    temp_data[-1]['start by'] = start_by
                try:
                    apply_by = sub_soup.find(class_='apply_by').find_next(class_='item_body').text.strip()
                    temp_data[-1]['apply by'] = apply_by
                except AttributeError:
                    try:
                        apply_by = sub_soup.find(class_='internship_other_details_container').find_next(class_='item_body').text.strip()
                    except (AttributeError, TypeError) as e:
                        print(f"Error extracting apply by date: {e}")
                    else:
                        temp_data[-1]['apply by'] = apply_by
                try:
                    duration = sub_soup.find_all(class_='item_body')[1].text.strip()
                except (IndexError, AttributeError) as e:
                    print(f"Error extracting duration: {e}")
                else:
                    temp_data[-1]['duration'] = duration
                try:
                    stipend = sub_soup.find_all(class_='item_body')[2].text.strip()
                except (IndexError, AttributeError) as e:
                    print(f"Error extracting stipend: {e}")
                else:
                    temp_data[-1]['stipend'] = stipend
                try:
                    applicants = sub_soup.find(class_='applications_message').text.strip()
                except (AttributeError, TypeError) as e:
                    print(f"Error extracting applicants: {e}")
                else:
                    temp_data[-1]['applicants'] = applicants
        return temp_data
    except Exception as e:
        print(f"Error scraping {profile}: {e}")
        return []
num_profiles_to_scrape = 10
if __name__ == '__main__':
    with Pool(processes=num_profiles_to_scrape) as pool:
        results = pool.map(scrape_profile, data)
    flattened_results = [item for sublist in results for item in sublist]
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Internship Data')
    ex.write_header(sheet)
    for index, data_row in enumerate(flattened_results, start=1):
        ex.write_body(sheet, index, data_row)
    end_time = time.time()
    execution_time = end_time - start_time
    minutes, seconds = divmod(execution_time, 60)
    minutes = int(minutes)
    seconds = int(seconds)
    time_format = "{:02d}min {:02d}sec".format(minutes, seconds)
    workbook.save('aaj_wali_25_5.xls')
    print("Task completed")
    print("Total execution time:", time_format)
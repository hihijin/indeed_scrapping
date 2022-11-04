from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from requests import get

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def get_page_count(keyword):
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    navigation = soup.find("nav", role = "navigation")
    if navigation == None :
        return 1
    pages = navigation.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5 :
        return 5
    else :
        return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(5) :
        driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get(f"https://kr.indeed.com/jobs?q={keyword}")
        print("Requesting", f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            anchor = job.select_one("h2 a")
            title_anchor = job.select_one("h2 a span")
            company_anchor = job.find("span", class_="companyName")
            region_anchor = job.find("div", class_="companyLocation")
            if company_anchor is not None:
                company = str(company_anchor.string)
            if region_anchor is not None:
                region = str(region_anchor.string)
            if title_anchor is not None:
                title = str(title_anchor.string)
            job_data = {
            'company': company.replace(","," "),
            'region': region.replace(","," "),
            'position' : title.replace(","," ")
            }
            results.append(job_data)
    return results
                

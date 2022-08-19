from imports import *

# Code to install webdriver if it's not installed
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

def login(driver, password):
    '''
    This function takes in selenium driver and linkedin password to login
    '''
    url =  'https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    wait = WebDriverWait(driver, 10)
    driver.get(url)
  
    driver.find_element("xpath",'/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys('wang.meredith09@gmail.com')
    driver.find_element("xpath",'/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(password)
    driver.find_element("xpath",'/html/body/div/main/div[2]/div[1]/form/div[3]').click()


def search(driver):
    '''
    This function takes in the driver and redirect the driver to the query link
    '''
    time.sleep(5)
    driver.get("https://www.linkedin.com/jobs/search/?keywords=data%20science")

def get_n_results(driver):
    '''
    This function takes in the driver and grab the number of results that were fetched
    '''
    time.sleep(10)
    results_div = driver.find_element("xpath",'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/header/div[1]/small')
    n_string = results_div.text
    n = int(n_string.split()[0].replace(',',""))
    return n 


def get_jobs(driver):
    '''
    This function takes in the driver and find jobs ul div
    '''
    ul_div = driver.find_element("xpath",'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul')
    return ul_div


def scroll_down(driver):
    '''
    This function takes in the driver and scroll to the bottom to properly load page
    '''
    for i in np.linspace(0,1,10):
        time.sleep(2)
        # Excute JavaScript
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight*{i})")


def get_job_urls(jobs,driver,job_urls = {}):
    '''
    This function takes in the driver and an empty dictionary to get each job's url, role name, company, and location
    '''
    i = 1
    while True: 
        try:

            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]')))
            url = jobs.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a').get_attribute("href")
            role = jobs.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a').text
            company = jobs.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[2]/a').text
            location = driver.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[3]/ul/li').text
            job_urls.update({url:{'company':company,'location':location,'role':role}})
            i+=1
        except:
            return job_urls


def load_next_page(driver):
    '''
    This function takes in the driver and click on the button to go to the next page
    '''
    curr= driver.find_element("xpath",'//*[@aria-current="true"]').text
    next = driver.find_element("xpath",f'//*[@aria-label="Page {int(curr)+1}"]')
    next.click()

def get_description(driver,job_dict):
    '''
    This function takes in the driver and the dictionary,
    it uses the urls to further get job's description
    '''
    good = []
    fail = []
  #Iterate through the url list to scrape the descriptions
    for url in list(job_dict.keys()):
        if url not in good:
            try:
                driver.get(url)
                time.sleep(3)
                if driver.current_url != url:
                    print(f'failed at {url}')
                    #remove broken urls
                    job_dict.pop(url)
                #scrape
                driver.find_element("xpath",'//*[@aria-label="Click to see more description"]').click()
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[2]/article/div/div[1]')))
                description = driver.find_element("xpath",'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[2]/article/div/div[1]').text
                education = driver.find_element("xpath", '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[6]/div/div[1]/div[3]/div[2]/ul').text

                # time.sleep(3)
                job_dict.get(url).update({"description":description})
                job_dict.get(url).update({"education": education})
                time.sleep(6)
                good.append(url)

            except:
                #keep going if there is a random error in which a div did not load properly but check where we failed
                print(f"fail {job_dict.get(url)}")
                fail.append(url)
    return job_dict

def get_skills(driver,job_dict):
    '''
    Get job's applicants' most have skills in the Linkedin premium insight
    It will return the skills depending on if the user is Linkedin premium
    This function is not used in the final main function
    '''
    good = []
    fail = []
    # Iterate through the url list to scrape the descriptions
    for url in list(job_dict.keys()):
        if url not in good:
            try:
                driver.get(url)
                time.sleep(2)
                if driver.current_url != url:
                    print(f'failed at {url}')
                    #remove broken urls
                    job_dict.pop(url)
                # Scrape
                skill_list = driver.find_element("xpath", '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[6]/div/div[1]/div[2]/div[2]/ul')
                skills = skill_list.find_elements(By.TAG_NAME, "li")
                # if len(skills) > 0:
                # i = 1
                skill = []
                # while True:
                #     try:
                #         # WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[6]/div/div[1]/div[2]/div[2]/ul/li[{i}]')))
                #         skillname = driver.find_element("xpath",f'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[6]/div/div[1]/div[2]/div[2]/ul/li[{i}]/p').text
                #         job_dict.get(url).update({"skills":skillname})
                #         i+=1
                #         good.append(url)
                #     except:
                #         return job_dict
                for i in skills:
                    skill = i.find_elements("xpath", f'//*[@id="ember95"]/div/div[1]/div[2]/div[2]/ul/li[{i}]/p').text
                    job_dict.get(url).update({"skills":skill})
                    good.append(url)
                return job_dict
            except:
                #keep going if there is a random error in which a div did not load properly but check where we failed
                print(f"fail{job_dict.get(url)}")
                fail.append(url)

def main(driver,password):
    '''
    This functions combine all the steps above to accomplish data acquisition
    '''
    login(driver, password)
    search(driver)
    n = get_n_results(driver)
    job_dict = {}
    #iterate through the amount of pages given
    for i in range(39):
        jobs = get_jobs(driver)
        scroll_down(driver)
        get_job_urls(jobs,driver,job_urls = job_dict)
        time.sleep(1)
        load_next_page(driver)
    get_description(driver,job_dict)
    df = pd.DataFrame(job_dict)
    # return get_description(driver,job_dict,good)
    return df

def get_data():
    '''
    This function spit out the csv file that is stored from
    running main function and manually filled in nulls
    Detialed fill null method please reference preparation notebook
    '''
    df = pd.read_csv('data_science.csv')
    return df
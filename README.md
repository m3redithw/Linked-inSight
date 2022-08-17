![logo](https://user-images.githubusercontent.com/105242871/185154594-0e60bd92-b70c-4d5a-a3b6-3c3b00c2b7bf.png)

# Linkedin Data Science
by **Meredith Wang**

<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-013243.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-2a4d69.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-8DF9C1.svg?logo=matplotlib&logoColor=white"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-65A9A8.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="plotly" src="https://img.shields.io/badge/plotly-adcbe3.svg?logo=plotly&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-4b86b4.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=white"></a>
<a href="#"><img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-1faecf.svg?logo=python-geopandas&logoColor=white"></a>


## :globe_with_meridians:   Project Description
**Job hunting** is a tedious and stressful process. Stacked paragraphs of description and long list of requirement from the job listings are only adding fuel to the flame. This project aims to help me and other aspiring **data science** professionals get a clear insight on the role they're pursuing, and to provide a better understanding on the education level of their competitors.
## :star2:  Project Goals
Our goal is to predict the candidates' **education level** of job postings using **Natural Language Processing** techniques to analyze data-science job postings on Linkedin.

Education level is classified into two categories:
- Bachelor (candidate whose highest education level is a Bachelor degree)
- Higher (candidate whose highest education level is Master/PhD)
## :memo:   Initial Questions
▪ Is role dependent on the education level of candidates?

▪ Is job level dependent on the education level of candidates?


## :open_file_folder:   Data Dictionary
| **Variable** | **Value**                    | **Meaning**                                                     |
|:-------------|:-----------------------------|:----------------------------------------------------------------|
| Link         | String                       | The url of the job posting                                      |
| Company      | String                       | The company name of the job posting                             |
| Mode         | On-Site; Remote; Hybrid      | The working environment of the job posting                      |
| Type         | Full-time; Contract          | The contract type of the job posting                            |
| Level        | Entry; Associate; Mid-Senior | The job level of the job posting                                |
| Requirements | String                       | The requirements in the description section of the job posting  |
| Edu Level    | Int                          | Percentage of education level of candidates of the job position |
| Skills       | String                       | The top 10 skills from candidates of job posting                |


## :compass:    Outline/Planning
#### 1️⃣  Data Acquisition
<details>
<summary> Gather data from Linkedin using Selenium</summary>

- Install Selenium web driver

- Create function to guide driver to automate job search

- Store data locally to a .csv file

</details>

[Acquisition](acquisition.ipynb)

#### 2️⃣  Data Preparation
<details>
<summary> Missing Values</summary>

- When job posting does not have enough candidates to generate insight, the **education level** and **skills** will be missing

- Missing values are manually filled by going to URL of job posting, and find another positng with the same job level, role, and company

- Dummy Variables

</details>

[Preparation](preparation.ipynb)

#### :three: Data Exploration
[Exploration](exploration.ipynb)
#### :four: Modeling

#### :five:    Modeling Evaluation

## :repeat:   Steps to Reproduce

## :key:    Key Findings

## :high_brightness:    Recommendations

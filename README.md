![logo](https://user-images.githubusercontent.com/105242871/185154594-0e60bd92-b70c-4d5a-a3b6-3c3b00c2b7bf.png)

# [Linked inSight](https://www.canva.com/design/DAFJozqrh6w/7KibP6_xsjhb679nryBVNg/view?utm_content=DAFJozqrh6w&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
by **Meredith Wang**

<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-003F5D.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-00527C.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-00609C.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=white"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-006DB2.svg?logo=python-matplotlib&logoColor=white"></a>
<a href="#"><img alt="Selenium" src="https://img.shields.io/badge/Selenium-1faecf.svg?logo=selenium&logoColor=white"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-4E97D1.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="plotly" src="https://img.shields.io/badge/plotly-7BB4E3.svg?logo=plotly&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-A3CEEF.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="NLTK" src="https://img.shields.io/badge/NLTK-C5D4EB.svg?logo=python-nltk&logoColor=white"></a>
## :globe_with_meridians:   Project Description
**Job hunting** is a tedious and stressful process. Stacked paragraphs of description and long list of requirement from the job listings are only adding fuel to the flame. This project aims to help me and other aspiring **data science** professionals get a clear insight on the role they're pursuing, and to provide a better understanding on the education level of their competitors.
## :star2:  Project Goals
Our goal is to predict the candidates' **education level** of job postings using **Natural Language Processing** techniques to analyze data-science job postings on Linkedin.

Education level is classified into two categories:
- Undergraduate (candidate whose highest education level is a Bachelor degree, and those who have 'other' degrees)
- Graduate (candidate whose highest education level is Master/PhD)
## :memo:   Initial Questions
▪ What does overall candidate's education distribution look like?

▪ Is role dependent on the education level of candidates?

▪ Is job level dependent on the education level of candidates?

▪ Is job description different for graduate vs. undergraduate group?



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

![selenium](https://user-images.githubusercontent.com/105242871/185518199-8de21772-c250-419b-a40f-524235f647c7.gif)

#### 2️⃣  Data Preparation
<details>
<summary> Missing Values</summary>

- When job posting does not have enough candidates to generate insight, the **education level** and **skills** will be missing

- Missing values are manually filled by going to URL of job posting, and find another positng with the same job level, role, and company

</details>

<details>
<summary> Dummy Variables</summary>

Categorical features (e.g. `role`, `level`) are turned into dummy variables to quantify the features, so we can use them in the models.

</details>

<details>
<summary> Initial Text Cleaning</summary>

Job role names vary from companies. For example, for data scientist position, there are names like "Data Scientist II", "Data Scientist, Charging Data and Modeling", "Data Scientist - Credit Card", etc... For the purpose of analyzing the general category's relationship with the target variable, all roles are generalized to 4 categories: **Data Scientist, Data Analyst, Data Engineer, Managerial Roles**.

</details>

<details>
<summary> Parsing Text</summary>

- Convert text to all lower case for normalcy
	
- Remove any accented characters, non-ASCII characters
	
- Remove special characters
	
- Lemmatization
	
- Remove stopwords
	
- Store the clean text and the original text for use in future notebooks

</details>

[Preparation](preparation.ipynb)

#### :three: Data Exploration
- Address initial questions to find what are the key features that are associated with undragudate and graduate group

- Explore each feature's correlation with education distribution

- Use visualizations to better understand the relationship between features and target variable

#### :four:    Statistical Testing & Modeling	
- Conduct T-Test for categorical variable vs. numerical variable
	
- Conduct Chi^2 Test for categorical variable vs. categorical variable

- Conclude hypothesis and address the initial questions

[Exploration](exploration.ipynb)

#### :five: Modeling
- Create decision tree classifer and fit train dataset

- Find the max depth for the best performing decision tree classifer (evaluated using classification report, accuracy score)

- Create random forest classifier and fit train dataset

- Find the max depth for the best performing random forest classifier (evaluated using classification report, accuracy score)

- Create logistic regression model and fit train dataset

- Find the parameter C for the best performing logistic regression model (evaluated using classification report, accuracy score)

- Create XGBoost classifier and fit train dataset

- Pick the top 3 models among all the models and evaluate performance on validate dataset

- Pick the model with highest accuracy and evaluate on test dataset

[Modeling](modeling.ipynb)
## :repeat:   Steps to Reproduce
- [x] You will need to have a Linkedin Premium account. Store your password locally in a secret text file.
- [x] You will need to install Selenium webdrive. Please follow documentation and steps in **acquisition** notebook.
- [x] Clone my repo (including **imports.py**, **prepare.py**) 
- [x] Libraries used are pandas, matplotlib, seaborn, plotly, sklearn, scipy, selenium, nltk
- [x] Follow instructions in each notebook throughout the pipeline (**preparation**, **exploration**, **modeling**)and README file
- [x] Good to run workbook and read through white paper :smile_cat:
## :key:    Key Findings

<img width="952" alt="overall_distribution" src="https://user-images.githubusercontent.com/105242871/185520569-11aa7c4f-9ad1-4045-8848-54dca2f9afb3.png">

- **Less than 1/4** of data science job posting's candidate's highest education level is Bachelor degree.

- Candidate's education distribution is dependent on role (scientist, analyst, engineer, managerial roles)

- Candidate's education distribution is independent with job level (entry, associate, mid-senior)

- For entry level positions, the amount of candidates with graduate degrees is **significantly more** than those with undergrad degrees.

- Top phrases mentioned in data science job descriptions are: **Data Analytics, no. of years experience, SQL, Python, Master Degree, Business** 

- Top skills among data science candidates: **SQL, Python, Machine Learning, Data Analysis, R, C/C++, Tableau, Data Visualization**

- Final model decision tree is expected to predict with 87% accuracy on future unseen data.

<img width="1120" alt="model_evaluation" src="https://user-images.githubusercontent.com/105242871/185520556-54470d3f-b583-4a23-8a10-cfb18b691978.png">


##  🔜    Next Steps
- For the purpose of completing a MVP, I was only able to gather 243 observations. That is one of the reason there's a class imbalance in our dataset, and why the model is failing to converge and having a higher accuracy. Therefore, gathering more data would be important.

- This project is solely focused on Data Science related job positions in the United States. We can expand the field to other areas in tech (e.g. web development, cloud administration, etc.) and compare the education distribution across fields. We can also expand countries to see if such a master-degree dominant poll is solely in the United States.

- There are extensive amount of master programs, and there is no indicator of the quality of the program itself. For further study, I would like to include parameters that distinguish different levels of degree accomplished.

## :high_brightness:    Recommendations/Further Questions
- For candidates who don't have a graduate degree, or a bachelor degree in STEM, I suggest you focus on mastering the "top skills" that we concluded in the explore section.

- What exactly is the difference between candidates who acquire the skills on their own, and those who went through a graduate program that cost $50k on average? How small is the chance for someone without a desired degree to "survive" the sea of resumes?

from imports import *
from prepare import prep_data, basic_clean, lemmatize, remove_stopwords, split, clean, clean_skills
def overall_distribution(train):
    '''
    This function plot the overall candidate education distribution accross all jobs
    '''
    y = [train.edu_bachelor.sum(),train.edu_master.sum(), train.edu_phd.sum(), train.edu_other.sum()]
    plt.figure(figsize=(16,12))
    mylabels = ["Bachelor", "Master", 'PhD', 'Other']
    myexplode = [0.2, 0, 0, 0]
    mycolors = ['#45818e', '#783f04', '#e7dbcd', '#5b5b5b' ]
    textprops = {"fontsize":15}
    plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors, textprops=textprops, autopct='%.1f%%')
    plt.legend()
    plt.title('Candidate Education Distribution',fontsize=18)
    plt.show()

def role(train):
    '''
    This functions plot the education distribution per role
    '''
    pct = [['Data Scientist', 'bachelor', 22.333333],['Data Scientist', 'master', 58.888889],['Data Scientist', 'phd', 15.022222], ['Data Scientist', 'other', 3.266667],
          ['Data Analyst', 'bachelor', 26.685714],['Data Analyst', 'master', 64.257143],['Data Analyst', 'phd', 5.942857],['Data Analyst', 'other',  3.914286],
          ['Data Engineer','bachelor',28.342105],['Data Engineer', 'master', 62.421053],['Data Engineer', 'phd', 6.421053], ['Data Engineer', 'other', 2.710526],
           ['Managerial Roles', 'bachelor', 13.882353], ['Managerial Roles', 'master',59.294118], ['Managerial Roles','phd', 22.117647], ['Managerial Roles', 'other', 4.529412]
         ]
    roledf = pd.DataFrame(pct, columns = ['Role', 'Highest Education Level', 'Percentage'])
    plt.figure(figsize = (20,8))
    sns.barplot(x='Role', y='Percentage',hue = 'Highest Education Level', data =roledf, palette = ['#45818e', '#783f04', '#e7dbcd', '#5b5b5b'])
    # plt.ylim = (0.7,1)
    plt.xlabel("Role", fontsize = 16)
    plt.ylabel("Percentage", fontsize = 16)
    plt.title("Education Distribution per Role", fontsize = 20)

def level(train):
    '''
    This functions plot the education distribution per level
    '''
    plt.figure(figsize = (16,8))
    sns.countplot(x='level', hue='label', data=train, palette= ['#783f04','#45818e'])
    plt.title('Education Distribution per Level', fontsize = 20)
    plt.xlabel('Job Level', fontsize = 16)
    plt.ylabel('Count', fontsize = 16)

def requirements(train):
    '''
    This function visualize the top 20 most frequent words in requirement
    Detailed steps please reference explore.ipynb
    '''
    all_text = ' '.join(train.requirements)
    u_text = ' '.join(train[train.label == 'u'].requirements)
    g_text = ' '.join(train[train.label == 'g'].requirements)
    all_text = clean(all_text)
    u_text = clean(u_text)
    g_text = clean(g_text)
    all_freq = pd.Series(all_text.split()).value_counts()
    u_freq = pd.Series(u_text.split()).value_counts()
    g_freq = pd.Series(g_text.split()).value_counts()
    word_counts = pd.concat([all_freq, u_freq, g_freq], sort=True, axis=1)
    word_counts.columns = ['all', 'u', 'g']
    word_counts = word_counts.fillna(0).apply(lambda s: s.astype(int))
    word_counts.assign(p_u=word_counts.u / word_counts['all'],p_g=word_counts.g / word_counts['all'])\
    .sort_values(by='all')\
    .tail(20)\
    [['u', 'g']]\
    .sort_values(by='g')\
    .plot.barh(stacked=True, figsize = (16,10), color = ['#45818e', '#783f04'])

def g_bigrams(train):
    '''
    This function plot the wordcloud for top bigrams in the requirements for graduate degree category
    '''
    g_text = ' '.join(train[train.label == 'g'].requirements)
    g_text = clean(g_text)
    top_20_g_bigrams = (pd.Series(nltk.ngrams(g_text.split(), 2))
                      .value_counts()
                      .head(20))
    data = {k[0] + ' ' + k[1]: v for k, v in top_20_g_bigrams.to_dict().items()}
    img = WordCloud(background_color='white', width=800, height=400, colormap = 'YlOrBr_r').generate_from_frequencies(data)
    plt.figure(figsize=(8, 4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def u_bigrams(train):
    '''
    This function plot the wordcloud for top bigrams in the requirements for undergraduate degree category
    '''

    u_text = ' '.join(train[train.label == 'u'].requirements)
    u_text = clean(u_text)
    top_20_u_bigrams = (pd.Series(nltk.ngrams(u_text.split(), 2))
                      .value_counts()
                      .head(20))
    data = {k[0] + ' ' + k[1]: v for k, v in top_20_u_bigrams.to_dict().items()}
    colors = ['#194569', '#5F84A2', '#91AEC4', '#B7D0E1', '#CADEED', '#DBECF4']
    img = WordCloud(background_color='white', width=800, height=400, colormap='Blues_r').generate_from_frequencies(data)
    plt.figure(figsize=(8, 4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()



def g_skills(train):
    '''
    This function generates the wordcounts for top skills for graduate degree
    '''
    # Separating skills into Series
    g_skills = ' '.join(train[train.label == 'g'].skills)
    g_skills = clean_skills(g_skills)
    top_20_g_skill_bigrams = (pd.Series(nltk.ngrams(g_skills.split(), 2))
                      .value_counts()
                      .head(20))
    data = {k[0] + ' ' + k[1]: v for k, v in top_20_g_skill_bigrams.to_dict().items()}
    img = WordCloud(background_color='white', width=800, height=400, colormap='YlOrBr_r').generate_from_frequencies(data)
    plt.figure(figsize=(8, 4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def u_skills(train):
    
    '''
    This function generates the wordcounts for top skills for undergraduate degree
    '''
    # Separating skills into Series
    u_skills = ' '.join(train[train.label == 'u'].skills)
    u_skills = clean_skills(u_skills)

    top_20_u_skill_bigrams = (pd.Series(nltk.ngrams(u_skills.split(), 2))
                      .value_counts()
                      .head(20))
    data = {k[0] + ' ' + k[1]: v for k, v in top_20_u_skill_bigrams.to_dict().items()}
    img = WordCloud(background_color='white', width=800, height=400,  colormap='Blues_r').generate_from_frequencies(data)
    plt.figure(figsize=(8, 4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
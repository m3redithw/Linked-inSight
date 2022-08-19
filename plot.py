from imports import *
def overall_distribution():
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

def role():
    '''
    This functions plot the education distribution per role
    '''
    plt.figure(figsize = (16,8))
    sns.countplot(x='role', hue='label', data=train, palette= ['#783f04','#45818e'])
    plt.title('Education Distribution per Role', fontsize = 20)
    plt.xlabel('Role', fontsize = 16)
    plt.ylabel('Count', fontsize = 16)

def level():
    '''
    This functions plot the education distribution per level
    '''
    plt.figure(figsize = (16,8))
    sns.countplot(x='level', hue='label', data=train, palette= ['#783f04','#45818e'])
    plt.title('Education Distribution per Level', fontsize = 20)
    plt.xlabel('Job Level', fontsize = 16)
    plt.ylabel('Count', fontsize = 16)

def requirements():
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

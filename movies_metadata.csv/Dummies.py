import pandas as pd
df=pd.read_csv('movies_metadata.csv')
df=df.drop(index=[29503,19730,35687])
df.at[19574,'original_language']='en'
df.at[21602,'original_language']='en'
df.at[22832,'original_language']='en'
df.at[32141,'original_language']='en'
df.at[37407,'original_language']='cs'
df.at[41047,'original_language']='ur'
df.at[41872,'original_language']='xx'
df.at[44057,'original_language']='fr'
df.at[44410,'original_language']='sv'
df.at[44576,'original_language']='de'
df.at[44655,'original_language']='xx'
df=df[df['status'].isin(['Released','Post Production'])]
df=df.loc[df['vote_count']>=df['vote_count'].quantile(0.2)]
df=df.dropna(subset=['release_date'])
df=df.drop_duplicates()






lanlist=pd.get_dummies(df[['original_language']],columns=["original_language"],drop_first=True)
lanlist=list(lanlist.columns)
languages= pd.DataFrame(columns = lanlist)
def selectdummyLanguage(InputLanguage):
    InputLanguage='original_language_'+InputLanguage
    global languages,lanlist
    for lan in lanlist:
        if str(InputLanguage)==lan:
            languages.loc[0,lan]=1
        else:
            languages.loc[0,lan]=0
    return list(languages.loc[0].values)
            
        
        
        
from ast import literal_eval
df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in literal_eval(x)])
from sklearn.preprocessing import MultiLabelBinarizer
mlb=MultiLabelBinarizer()
x=mlb.fit_transform(df['genres'])
cols=["genre_{}".format(c) for c in mlb.classes_]
df2=pd.DataFrame(data=x,columns=cols)




genlist=list(df2.columns)
genres= pd.DataFrame(columns = genlist)
def selectdummyGenre(InputGenre):
    global genres,genlist
    InputGenre='genre_'+InputGenre
    for gen in genlist:
        if str(InputGenre)==gen:
            genres.loc[0,gen]=1
        elif genres.loc[0,gen]==1:
             genres.loc[0,gen]=1
        else:
            genres.loc[0,gen]=0
    return list(genres.loc[0].values)


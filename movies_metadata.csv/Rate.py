import pandas as pd
df=pd.read_csv('movies_metadata.csv')
c= df['vote_average'].mean()
m= df['vote_count'].quantile(0.2)
def rate(x,z):
    rate=round((x/(x+m)*z) + (m/(m+x)*c),1)
    return rate
import numpy as np
import pandas as pd

df = pd.read_csv('BL-Flickr-Images-Book-truncated50.csv')
df.head()

to_drop = ['Identifier','Edition Statement','Contributors','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Flickr URL','Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)

df['Place of Publication'].head(10)
pub = df['Place of Publication']
london = df[pub.str.contains("London")]

Place = london.loc[df['Place of Publication'] == 'London']

print(Place)

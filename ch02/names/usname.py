import pandas as pd
names1880 = pd.read_csv('yob1880.txt', names=['name', 'sex', 'births'])

years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]

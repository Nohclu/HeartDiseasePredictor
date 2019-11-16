import pandas

df = pandas.read_csv("../dirtyHeart.csv")
df = pandas.DataFrame(df)

caTracker = {
    1:0,
    0:0
}
nanIndex = []

# Dictionary will go in order of 1(heart disease), 0(no heart disease) 
classOccurences = df.iloc[:,-1].value_counts()

for row, clmn  in df.iterrows():
    if clmn['ca'] == 4:
        nanIndex.append(row)
    else:
        caTracker[clmn['target']] += clmn['ca']

for i in nanIndex:
    nanRow = df.iloc[i]
    mean = caTracker[nanRow['target']] // classOccurences[nanRow['target']]
    df.at[i,'ca'] = mean

df.to_csv("./nanRemoved.csv")
import pandas

CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

df = pandas.read_csv("../nanRemoved.csv")
df = pandas.DataFrame(df)

s = len(df.index)
binSize = 0
binTotal = 0
# numberOfBins = 0

for i in range(2, s//2):
    if s % i == 0:
        binSize = i
        numberOfBins = s // i
        break
print(df)
print("---------------------------------------------------------------")
for h in CONTINUOUS_HEADERS:
    df = df.sort_values(by=[h])
    smoothedData = {h : []}
    tracker = 0
    for index, row in df.iterrows():
        binTotal += row[h]
        tracker += 1
        if tracker == binSize:
            tracker = 0
            for i in range(binSize):
                smoothedData[h].append(binTotal / binSize)
            binTotal = 0
    df.update(pandas.DataFrame(data=smoothedData))
print(df)
df.to_csv("../binByMean.csv")
print("Created '../binByMean.csv'")
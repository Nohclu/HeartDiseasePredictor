import math, pandas, numpy

def classifyAPoint(points, p, k=3):

    distance = []
    for group in points:
        for attr in points[group]:
            euclidean_distance = numpy.linalg.norm(attr - p)
            distance.append((euclidean_distance, group))

    distance = sorted(distance)[:k]

    freq1 = 0
    freq2 = 0

    for d in distance:
        if d[1] == 0:
            freq1 += 1
        elif d[1] == 1:
            freq2 += 1

    return 0 if freq1 > freq2 else 1

def main():
    points = {
        0: [],
        1: []}
    
    test = {
        0: [],
        1: []
    }

# 160 1's
# 136 0's
    df = pandas.read_csv('./datamining.csv', skiprows=[0, 1])
    df = df.sample(frac=1)
    hasHeartDisease = df["target"]
    df = ((df - df.min()) / (df.max() - df.min()))
    df["target"] = hasHeartDisease

    print(df)  
    for row_index, row in df.iterrows():
        if row_index < 250:
            if (row["target"] == 0):
                points[0].append(numpy.array(df.iloc[row_index, 0:13]))
            elif (row["target"] == 1):
                points[1].append(numpy.array(df.iloc[row_index, 0:13]))
        else:
            if (row["target"] == 0):
                test[0].append(numpy.array(df.iloc[row_index, 0:13]))
            elif (row["target"] == 1):
                test[1].append(numpy.array(df.iloc[row_index, 0:13]))

    totalTestValues = len(test[0]) + len(test[1])
    testPass = 0
    k = 9

    for t in test[0]:
        if classifyAPoint(points, t, k) == 0:
            testPass += 1
    for t in test[1]:
        if classifyAPoint(points, t, k) == 1:
            testPass += 1

    print("Pass: "+str(testPass) + "\nTotal: "+ str(totalTestValues))    


if __name__ == '__main__':
    main()
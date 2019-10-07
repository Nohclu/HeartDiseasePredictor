import pandas, math


def classifyPoint(trainingData, testPoint, k):
    distance = []
    for i, r in trainingData.iterrows():
        euclidean_distance = math.sqrt((r["age"] - testPoint["age"])**2 + (r["sex"] - testPoint["sex"])**2 + (r["chest pain"] - testPoint["chest pain"])**2 + (r["trestbps"] - testPoint["trestbps"])**2 + (r["chol"] - testPoint["chol"])**2 + (r["fbs"] - testPoint["fbs"])**2 + (r["restecg"] - testPoint["restecg"])**2 + (r["thalach"] - testPoint["thalach"])**2 + (r["exang"] - testPoint["exang"])**2 + (r["oldpeak"] - testPoint["oldpeak"])**2 + (r[" slope of the peak exercise ST segment"] - testPoint[" slope of the peak exercise ST segment"])**2 + (r["ca"] - testPoint["ca"])**2 + (r["thal"] - testPoint["thal"])**2)
        distance.append((euclidean_distance, r["target"]))
    
    distance = sorted(distance)[:k] 
  
    freq1 = 0 
    freq2 = 0 
  
    for d in distance: 
        if d[1] == 0: 
            freq1 += 1
        elif d[1] == 1: 
            freq2 += 1
  
    if freq1 >= freq2:
        if testPoint["target"] == 0:
            return 1
        else:
            return 0
    elif freq2 > freq1:
        if testPoint["target"] == 1:
            return 1
        else:
            return 0
    else:
        return 0

def main():
    df = pandas.read_csv('./datamining.csv', skiprows=[0, 1])
    df = df.sample(frac=1)

    normalizedDataFrame = (df - df.min())/(df.max()-df.min())
    normalizedDataFrame["target"] = df["target"]
    dataSplitRatio = round(len(normalizedDataFrame.index)*.8)

    trainDF, testDF = normalizedDataFrame[:dataSplitRatio], normalizedDataFrame[dataSplitRatio:]

    acc = 0
    for i,r in testDF.iterrows():
        acc += classifyPoint(trainDF, r, 11)
    print(acc / len(testDF.index)*100)

if __name__ == '__main__':
    main()

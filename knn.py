import math, pandas, numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# def classifyAPoint(points, p, k=3):

def main():
    df = pandas.read_csv('./datamining.csv', skiprows=[0, 1])
    #  Randomize order of rows
    df = df.sample(frac=1)

    attr = df.iloc[:,:-1].values
    classes = df.iloc[:,13].values

    # Split data 80% 20%
    X_train, X_test, y_train, y_test = train_test_split(attr, classes, test_size=0.20)
    scaler = StandardScaler().fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors=7)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    print(classification_report(y_test, y_pred))


    


if __name__ == '__main__':
    main()
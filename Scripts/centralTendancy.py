import pandas
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

# def median(df, df_col):
#     sortedCol = list(df[df_col].sort_values())
#     dfLen = len(df)
#     if ((dfLen % 2) == 1):
#         return (sortedCol[dfLen//2])
#     else:
#         return (sortedCol[dfLen//2], sortedCol[(dfLen//2)+1])

# def main():
#     df = pandas.read_csv('../dirtyHeart.csv')
#     df = pandas.DataFrame(df)

#     mean = df.sum(axis=0)/len(df)

#     CATEGORICAL_HEADERS = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target']
#     CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
#     ALL_HEADERS = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target','age', 'trestbps', 'chol', 'thalach', 'oldpeak']

#     print("Continuous data\n---------------")
#     for header in CONTINUOUS_HEADERS:
#         print(header, 'Median: ' + str(median(df, header))+'\n       Mean: ' + str(mean[header]))

#     print('\n')

#     print("Categorical data\n----------------")
#     for header in ALL_HEADERS:
#         print(header, 'Median: ' + str(median(df, header))+'\n       Mean: ' + str(mean[header]))
#         dic = {}
#         for i, r in df.iterrows():
#             if (r[header] in dic):
#                 dic[r[header]] += 1
#             else:
#                 dic[r[header]] = 1
#         objects = []
#         performance = []
#         for k,v in dic.items():
#             objects.append(k)
#             performance.append(v)
#         y_pos = np.arange(len(objects))

#         plt.bar(y_pos, sorted(performance), align='center', alpha=0.5)
#         plt.xticks(y_pos, objects)
#         plt.ylabel('Frequncy')
#         plt.title(header)

#         min_ylim, max_ylim = plt.ylim()
#         plt.axvline(mean[header], color='k', linestyle='dashed', linewidth=1)
#         plt.text(mean[header]*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(mean[header]))

#         plt.show()


df = pandas.read_csv('../dirtyHeart.csv')
df = pandas.DataFrame(df)

fontMean = {'color':  'darkred',
        'size': 10,
        }
fontMedian = {'color':  'blue',
        'size': 10,
        }


CATEGORICAL_HEADERS = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target']
CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']

for col in CONTINUOUS_HEADERS:
    bins = len(df[col].unique())
    plt.ylabel('Frequency')
    plt.xlabel(col)
    y,x,_ = plt.hist(df[col], bins, color="lightgrey", edgecolor='black')
    plt.axvline(df[col].mean(), color='darkred', linestyle='dashed', linewidth=2)
    plt.text(df[col].mean()*1.1, plt.ylim()[1]*0.9, 'Mean: {:.2f}'.format(df[col].mean()), fontdict=fontMean)
    plt.axvline(df[col].median(), color='blue', linestyle='dashed', linewidth=2)
    plt.text(df[col].median(), plt.ylim()[1]*0.8, 'Median: {}'.format(df[col].median()), fontdict=fontMedian)
    plt.show()

for col in CATEGORICAL_HEADERS:
    values = sorted(df[col].value_counts())
    y_pos = np.arange(len(values))
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, range(0,len(values)))
    plt.ylabel('Frequency')
    plt.title(col)
    plt.show()
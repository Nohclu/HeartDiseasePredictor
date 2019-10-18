import pandas
import numpy as np
import matplotlib.pyplot as plt

def median(df, df_col):
    sortedCol = list(df[df_col].sort_values())
    dfLen = len(df)
    if ((dfLen % 2) == 1):
        return (sortedCol[dfLen//2])
    else:
        return (sortedCol[dfLen//2], sortedCol[(dfLen//2)+1])

def main():
    df = pandas.read_csv('./dirtyHeart.csv')
    df = pandas.DataFrame(df)

# Displaying the mode for each header
    for header in df:
        print(header, median(df, header))
        dic = {}
        for i, r in df.iterrows():
            if (r[header] in dic):
                dic[r[header]] += 1
            else:
                dic[r[header]] = 1
        objects = []
        performance = []
        for k,v in dic.items():
            objects.append(k)
            performance.append(v)
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Frequncy')
        plt.title(header)

        plt.show()


if __name__ == "__main__":
    main()
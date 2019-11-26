import pandas
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv('../dirtyHeart.csv')
df = pandas.DataFrame(df)

CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']

for col in CONTINUOUS_HEADERS:
    df.boxplot(column=[col], return_type='axes')
    # plt.savefig("..//DataDistribution//box"+col+".png")
    plt.show()
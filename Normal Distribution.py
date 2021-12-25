from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.normal(size=5)
sns.distplot(x,hist=False)
print(x)
plt.show()

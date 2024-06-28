import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('RESULT.xlsx')
x = file['Company']
y = file['ROI']
plt.figure(figsize=(15, 5))
plt.bar(x,y)
plt.show()
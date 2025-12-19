#The Python code uses seaborn’s FacetGrid to show the three histograms:

import pandas as pd
import seaborn as sns
sample_data = pd.DataFrame({
'income': loans_income.sample(1000),
'type': 'Data',
})

sample_mean_05 = pd.DataFrame({
'income': [loans_income.sample(5).mean() for _ in range(1000)],
'type': 'Mean of 5',
})

sample_mean_20 = pd.DataFrame({
'income': [loans_income.sample(20).mean() for _ in range(1000)],
'type': 'Mean of 20',
})

results = pd.concat([sample_data, sample_mean_05, sample_mean_20])

g = sns.FacetGrid(results, col='type', col_wrap=1, height=2, aspect=2)

g.map(plt.hist, 'income', range=[0, 200000], bins=40)

g.set_axis_labels('Income', 'Count')

g.set_titles('{col_name}')
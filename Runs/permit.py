import pandas as pd

d= {'0': ['Bev', 'stone', 'evy'], 'BC123': ['Y', 'N', 'Y'],'BC111': ['N', 'Y', 'N']}

df = pd.DataFrame(d).set_index('0')

print(df['BC123']['Bev'])


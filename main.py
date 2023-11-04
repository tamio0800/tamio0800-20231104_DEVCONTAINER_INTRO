import pandas as pd

df = pd.read_feather('BTCUSDT.feather')
print(df.shape)
print(df.head(10))
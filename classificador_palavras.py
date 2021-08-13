import pandas as pd
df = pd.read_csv('resultado_part-00000', low_memory=False, delimiter="'" )
print(df.head(9))

import pandas as pd
from opencc import OpenCC

cc = OpenCC('s2tw')
df = pd.read_csv("case_498.csv")
df['original_text'] = df['original_text'].astype(str)
df['original_text_converted'] = df['original_text'].apply(lambda x: cc.convert(x))

df.to_csv("converted_case_498.csv")
import pandas as pd 
df_hungarian = pd.read_fwf('hungarian.data', header=None, sep=',').stack().reset_index(drop=True)
df_switzerland = pd.read_fwf('switzerland.data', header=None, sep=',').stack().reset_index(drop=True)
df_long_beach_va = pd.read_fwf('long-beach-va.data', header=None, sep=',').stack().reset_index(drop=True)

first_filter = []
final_data = []
tokens = []

for line in df_hungarian:
    tokens.append(line.split(' '))

for val in tokens:
    for v in val:
        first_filter.append(v)
        if v == "name":
            final_data.append(first_filter)
            first_filter = []
            continue

df_hungarian = pd.DataFrame(final_data)
cols = [2, 3, 8, 9, 11, 15, 18, 31, 37, 39, 40, 43, 50, 57]
df = df_hungarian[cols]
print("Hungarian Data")
print(df.head(10))

final_data.clear()
tokens.clear()

for line in df_switzerland:
    tokens.append(line.split(' '))

for val in tokens:
    for v in val:
        first_filter.append(v)
        if v == "name":
            final_data.append(first_filter)
            first_filter = []
            continue
df_switzerland = pd.DataFrame(final_data)
df_switzerland = df_switzerland[cols]
print("Switzerland Data")
print(df_switzerland.head(10))


final_data.clear()
tokens.clear()

for line in df_long_beach_va:
    tokens.append(line.split(' '))

for val in tokens:
    for v in val:
        first_filter.append(v)
        if v == "name":
            final_data.append(first_filter)
            first_filter = []
            continue    

df_long_beach_va = pd.DataFrame(final_data)
df_long_beach_va = df_long_beach_va[cols]
print("Long Beach VA Data")
print(df_long_beach_va.head(10))        

df_hungarian.to_csv('./data/hungarian.csv', index=False)
df_switzerland.to_csv('./data/switzerland.csv', index=False)
df_long_beach_va.to_csv('./data/long_beach_va.csv', index=False)

df._append(df_switzerland)._append(df_long_beach_va).to_csv('./data/final_data.csv', index=False)

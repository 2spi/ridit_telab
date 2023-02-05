import pandas as pd

df = pd.read_table('survey.txt',
    sep = ' ',
    header = 0,
    index_col = 0,
    na_values = ['-']
)

df_tg = pd.read_table('treatment.txt',
    sep = ' ',
    header = 0,
    index_col = 0,
    na_values = ['-']
)

n = 0
c_freq = 0

for i in range(1, 6):
    n += int(df.loc[[i], 'frequency'])

for i in range(1, 6):
    half_f = df.loc[[i], 'frequency'] / 2.0
    df.loc[[i], 'hf'] = half_f
    df.loc[[i], 'cf'] = c_freq
    control_ridit = (half_f + c_freq) / n
    df.loc[[i], 'c_ridits'] = control_ridit

    c_freq = c_freq + int(df.loc[[i], 'frequency'])

ridit_sum = 0
for i in range(1, 6):
    c_r = df.loc[[i], 'c_ridits']
    df_tg.loc[[i], 'c_ridits'] = c_r
    product = float(c_r * df_tg.loc[[i], 'frequency'])
    df_tg.loc[[i], 'c_ridits*frequency'] = product
    ridit_sum += product


print("CONTROL GROUP: \n",df)
print("\nTREATMENT GROUP: \n", df_tg)
print("Mean ridit = ", ridit_sum/n)
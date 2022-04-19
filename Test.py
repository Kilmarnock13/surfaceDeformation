import pandas as pd
df_main = pd.DataFrame()
for ind in range(1, 81):
    ds = pd.read_csv('TwoRes/' + str(ind) + '.csv', index_col=False)

    df = pd.DataFrame(ds)
    try:
        df = df.drop(columns=['с'], axis=1)
    except:
        df = df.drop(columns=['c'], axis=1)

    #df = df.drop(df.index[960], axis=0)


    #df.index = range(0, len(df.index))

    df_main = pd.concat([df_main, df], axis=1, ignore_index=True)

df_main = df_main.transpose()
#df_main = df_main.dropna(axis=1)
#df_main = df_main.drop(columns=['с'], axis=1)
#print(df_main.columns)
#df_main = df_main.drop(df.columns[2], axis=1)
print(df_main)
df_main.to_csv('Amplitude1.csv')
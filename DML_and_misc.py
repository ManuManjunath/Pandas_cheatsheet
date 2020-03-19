# insert into df
df.append({'col_1': 'value', 'col_2': 'value'}, ignore_index=True)

# Insert using series
df.append(pd.Series((['Col_1_value', 'Col_2_value'], index=df.columns), ignore_index=True))

# Insert from another df -
df.append(df2, ignore_index=True)

# Insert specific row from another def -
df.append(df2.loc[10], ignore_index=True)

# update df set col_1 = col_1 * 5 where col_1 < 2
df.loc[df['col_1'] < 2, 'col_1'] *= 5

# delete from df where col_1 > 10
df = df.loc[df['col_1'] <= 10]

# To drop columns
df.drop(['col_1', 'col_2'], axis=1)
# To rename columns
df.rename(columns={'col_1': 'column_1', 'col_2': 'column_2'})

# More
# serialize object to file
df.to_pickle(file.pkl)
# Read from pickle
pd.read_pickle(file.pkl)
# To HDFS
df.to_hdf('data.h5', key='df', mode='w')
# Read from HDFS
pd.read_hdf('data.h5', 'df')
# To CSV
df.to_csv(index=False)

# To check the memory occupied by your Data Frame
def mem(df):
    print("{0:2f} MiB".format(
        df.memory_usage().sum() / (1024 * 1024)
    ))

mem(your_df)


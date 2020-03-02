# Filters
# select * from df where col_1 > 100
df[df.col_1 > 100]
# Get row with max col_1
df[df.col_1 == df['col_1'].max()]
# select count(col_1) where col_1 = 'this'
df['two'].value_counts()['this']
# select count(col_2) where col_1 = 'this'
df2 = df[df['col_1'] == 'this']
df2['col_2'].value_counts()

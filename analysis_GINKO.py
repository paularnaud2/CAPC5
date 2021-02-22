# Analyses points collectifs et individuels dans GINKO et SIG

import pandas as pd
import numpy as np
import glob

"""
# concatenate SIG files and change format file
def read_concatenate(path):

    xlsx_files = glob.glob(path)
    print(xlsx_files)

    frames = [pd.read_excel(file, engine="openpyxl") for file in xlsx_files]
    df = pd.concat(frames)
    return(df)

df_sig_indiv = read_concatenate('C:/Users/JBCDA5BN/Desktop/SIG/sig_indiv\\*.xlsx')
df_sig_indiv.to_csv('C:/Users/JBCDA5BN/Desktop/export_SIG_indiv_20210218.csv', sep=';')

print(df_sig_indiv.head())
print(df_sig_indiv.shape)

#SIG_df.to_csv('C:/Users/JBCDA5BN/Desktop/export_SIG_20210218.csv', sep=';')
SIG_df = pd.read_csv('C:/Users/JBCDA5BN/Desktop/export_SIG_collec_20210218.csv', sep=';')
print(SIG_df.shape)
"""
#---------------------------------------------------------------------------

# read GINKO and SIG files
GINKO_df = pd.read_csv('C:/Py/OUT/export_SQL_GINKO_20210218.csv', sep=';')
SIG_collec = pd.read_csv('C:/Users/JBCDA5BN/Desktop/export_SIG_collec_20210218.csv', sep=';', index_col=0)
SIG_indiv = pd.read_csv('C:/Users/JBCDA5BN/Desktop/export_SIG_indiv_20210218.csv', sep=';', index_col=0)

SIG_collec['TYPE_POINT'] = 'COLLECTIF'
SIG_indiv['TYPE_POINT'] = 'INDIVIDUEL'

SIG_collec.drop(['Unnamed: 0.1', 'NUMB'], axis=1, inplace=True)
SIG_indiv.drop('Unnamed: 0.1', axis=1, inplace=True)

SIG_df = pd.concat([SIG_collec, SIG_indiv], axis=0)

SIG_df.rename(columns={'ID_PRM': 'POINT'}, inplace=True)

SIG_df.POINT = SIG_df.POINT.astype(str)
GINKO_df.POINT = GINKO_df.POINT.astype(str)


SIG_df.drop_duplicates(['POINT', 'TYPE_POINT'], inplace=True)
"""
duplicateRowsDF = SIG_df[SIG_df.duplicated(['POINT'])]
print("Duplicate Rows SIG :")
print(duplicateRowsDF)
"""
GINKO_df.drop_duplicates(['POINT', 'TYPE_POINT'], inplace=True)


"""
duplicateRowsDF = GINKO_df[GINKO_df.duplicated(['POINT'])]
print("Duplicate Rows GINKO :")
print(duplicateRowsDF)
"""
# merge GINKO_collec and SIG_collec
merger = pd.merge(GINKO_df, SIG_df, on=['POINT'], how='outer', indicator=True, suffixes=('_GINKO', '_SIG'))
#print(merger.head())
"""
print(merger[merger._merge == 'both'].nunique())
print(merger[merger._merge == 'left_only'].nunique())
print(merger[merger._merge == 'right_only'].nunique())
"""
"""
left_only = merger[merger['_merge'] == 'left_only']
the_S = left_only[left_only.POINT.str.contains('S')]
print(the_S.shape)
right_only = merger[merger['_merge'] == 'right_only']
print(right_only.head())
right_only['len'] = right_only.POINT.apply(lambda x : x.startswith('0'))
left_only['len'] = left_only.POINT.apply(lambda x : x.startswith('0'))
print(right_only.len.value_counts())
print(left_only.len.value_counts())

"""

merger['VALIDATION_TYPE_POINT'] = np.where(merger['TYPE_POINT_GINKO'] == merger['TYPE_POINT_SIG'], 'OK', 'KO')
#print(merger.VALIDATION_TYPE_POINT.value_counts())
#print(merger.head())

df_merger_agg = merger.groupby(['SITE', 'VALIDATION_TYPE_POINT'], as_index=False).POINT.nunique()
print(df_merger_agg)

df_merger_agg = merger.groupby(['SITE'], as_index=False).POINT.nunique()
print(df_merger_agg)

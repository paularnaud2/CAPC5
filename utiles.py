import pandas as pd
import numpy as np


GINKO_df = pd.read_csv('C:/Py/OUT/export_SQL_GINKO_20210216.csv', sep=';')
SGE_df = pd.read_csv('C:/Py/OUT/export_SQL_SGE_20210217.csv', sep=';')
SGE_FRN = pd.read_excel('C:/Users/JBCDA5BN/Desktop/QDD/3. Documents reçus/Arnaud MEIGNE/export_FRN.xlsx')

GINKO_df = GINKO_df[GINKO_df.ETAT_PRM == 'en service']
#print(GINKO_df.POINT.dtype)

SGE_df['NATURE'] = SGE_df['SEGMENT_CONTRACT'].apply(lambda x : 'consommation' if x.startswith('C') 
                                                   else 'production' if x.startswith('P') else x)
SGE_df['ETAT_PRM'] = SGE_df['ETAT_SITUATION_CONTRAT'].apply(lambda x : 'en service' if x == 'SERVC' else x)

SGE_df.drop(['ETAT_CONTRACTUEL', 'ETAT_SITUATION_CONTRAT'], axis=1, inplace=True)

SGE_df = SGE_df[SGE_df.ETAT_PRM == 'en service']

matched_SGE = pd.merge(SGE_df, SGE_FRN, left_on=["FOURNISSEUR"], right_on=["CTR_NUMERO"], how='left')
matched_SGE.drop(['ACM_CODE','ROM_CODE_EIC', 'PRS_NOM_COMMERCIAL'], axis=1, inplace=True)
print(matched_SGE.POINT.dtype)

#matched_SGE['POINT'] = matched_SGE['POINT'].astype(np.int64)

merger = pd.merge(GINKO_df, matched_SGE, on=['POINT'], how='outer', indicator=True, suffixes=('_GINKO', '_SGE'))

print(merger.head())
#merger['COMPARAISON_SEGMENT'] = ['OK' if merger[(merger['CAT_CLIENT_x'] == merger['CAT_CLIENT_y']) & (merger['_merge'] == 'both')] else 'KO']
#merger['COMPARAISON_PUISSANCE'] = ['OK' if merger[(merger['PUISSANCE_SOUSCRITE_VALEUR'] == merger['PUISSANCE_SOUSCRITES']) & (merger['_merge'] == 'both')] else 'KO']
#merger['COMPARAISON_ETAT'] = ['OK' if merger[(merger['ETAT_PRM_GINKO'] == merger['ETAT_PRM_SGE']) & (merger['_merge'] == 'both')] else 'KO']
#merger['COMPARAISON_NATURE'] = ['OK' if merger[(merger['NATURE_GINKO'] == merger['NATURE_SGE']) & (merger['_merge'] == 'both')] else 'KO']


#print(merger['_merge'].value_counts())

#merger.to_excel('C:/Py/OUT/merger.xlsx')



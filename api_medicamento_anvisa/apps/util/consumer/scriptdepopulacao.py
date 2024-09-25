import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(
    dbname='medicacao_anvisa',
    user='postgres',
    password='root',
    host='db',
    port='5432'
)
cursor = conn.cursor()

file_path = r'api_medicamento_anvisa/apps/util/consumer/xls_conformidade_site_20240903_144255507.xls'
df = pd.read_excel(file_path, sheet_name='Planilha1', skiprows=41)

if 'EAN 3' in df.columns:
    df.drop(columns=['EAN 3'], inplace=True)

numeric_columns = [
    'PF Sem Impostos', 'PF 0%', 'PF 12%', 'PF 12% ALC', 'PF 17%', 'PF 17% ALC',
    'PF 17,5%', 'PF 17,5% ALC', 'PF 18%', 'PF 18% ALC', 'PF 19%', 'PF 19% ALC',
    'PF 19,5%', 'PF 19,5% ALC', 'PF 20%', 'PF 20% ALC', 'PF 20,5%', 'PF 21%',
    'PF 21% ALC', 'PF 22%', 'PF 22% ALC', 'PMC Sem Imposto', 'PMC 0%', 'PMC 12%',
    'PMC 12% ALC', 'PMC 17%', 'PMC 17% ALC', 'PMC 17,5%', 'PMC 17,5% ALC',
    'PMC 18%', 'PMC 18% ALC', 'PMC 19%', 'PMC 19% ALC', 'PMC 19,5%', 'PMC 19,5% ALC',
    'PMC 20%', 'PMC 20% ALC', 'PMC 20,5%', 'PMC 21%', 'PMC 21% ALC', 'PMC 22%',
    'PMC 22% ALC'
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('*', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')


inserts = []
max_length = 255
for index, row in df.iterrows():
    row = [str(x)[:max_length] if isinstance(x, str) and len(x) > max_length else x for x in row]
    inserts.append(tuple(row))

sql = '''
    INSERT INTO public.medicamento_medicacao (
        substancia, cnpj, laboratorio, codigo_ggrem, registro, ean_1, ean_2, produto, apresentacao, 
        classe_terapeutica, tipo_produto, regime_preco, pf_sem_impostos, pf_0, pf_12, pf_12_alc, 
        pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, pf_19, pf_19_alc, pf_19_5, 
        pf_19_5_alc, pf_20, pf_20_alc, pf_20_5, pf_21, pf_21_alc, pf_22, pf_22_alc, pmc_sem_imposto, 
        pmc_0, pmc_12, pmc_12_alc, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, pmc_18, pmc_18_alc, 
        pmc_19, pmc_19_alc, pmc_19_5, pmc_19_5_alc, pmc_20, pmc_20_alc, pmc_20_5, pmc_21, pmc_21_alc, 
        pmc_22, pmc_22_alc, restricao_hospitalar, cap, confaz_87, icms_0, analise_recursal, lista_concessao_credito, 
        comercializacao_2022, tarja, destinacao_comercial
    ) VALUES %s
'''

try:
    execute_values(cursor, sql, inserts)
except psycopg2.errors.StringDataRightTruncation as e:
    print("Erro ao inserir dados:", e)
    for insert in inserts:
        try:
            cursor.execute(sql, [insert])
        except psycopg2.errors.StringDataRightTruncation as inner_e:
            print(f"Erro na inserção: {insert}, erro: {inner_e}")

conn.commit()
cursor.close()
conn.close()

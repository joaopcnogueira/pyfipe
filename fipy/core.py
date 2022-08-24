# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['ConsultaFipe']

# %% ../nbs/00_core.ipynb 4
import os
import json
import requests
import pandas as pd

class ConsultaFipe:
    def __init__(self, mes: str = 'agosto/2022', codigo_tipo_veiculo: str = '1'):
        self.mes = mes
        self.codigo_tipo_veiculo = codigo_tipo_veiculo
        self._base_url = "http://veiculos.fipe.org.br/api/veiculos/"
        os.makedirs('datasets', exist_ok=True)

    def save_tables(self):
        mes2 = self.mes.replace('/', '_')
        if not os.path.exists(f'datasets/tabela_referencia_{mes2}.csv'):
            print("Consultando tabela de referência...")
            self.tabela_referencia = self.consulta_tabela_referencia()
            self.tabela_referencia.to_csv(f'datasets/tabela_referencia_{mes2}.csv', index=False)
            print("Tabela de referência salva!")
        else:
            self.tabela_referencia = pd.read_csv(f'datasets/tabela_referencia_{mes2}.csv')
            print(f"Tabela de referência já existe: tabela_referencia_{mes2}.csv")

        if not os.path.exists(f'datasets/tabela_marcas_{mes2}.csv'):
            print("Consultando tabela de marcas...")
            self.tabela_marcas = self.consulta_tabela_marcas()
            self.tabela_marcas.to_csv(f'datasets/tabela_marcas_{mes2}.csv', index=False)
            print("Tabela de marcas salva com sucesso!")
        else:
            self.tabela_marcas = pd.read_csv(f'datasets/tabela_marcas_{mes2}.csv')
            print(f"Tabela de marcas já existe: tabela_marcas_{mes2}.csv")

        if not os.path.exists(f'datasets/tabela_modelos_{mes2}.csv'):
            print('Consultando tabela de modelos...')
            self.tabela_modelos = self.consulta_tabela_modelos()
            self.tabela_modelos.to_csv(f'datasets/tabela_modelos_{mes2}.csv', index=False)
            print('Tabela de modelos salva com sucesso!')
        else:
            self.tabela_modelos = pd.read_csv(f'datasets/tabela_modelos_{mes2}.csv')
            print(f"Tabela de modelos já existe: tabela_modelos_{mes2}.csv")

        if not os.path.exists(f'datasets/tabela_ano_modelo_{mes2}.csv'):
            print("Consultando tabela de ano modelo...")
            self.tabela_ano_modelo = self.consulta_tabela_ano_modelo()
            self.tabela_ano_modelo.to_csv(f'datasets/tabela_ano_modelo_{mes2}.csv', index=False)
            print('Tabela de ano modelo salva com sucesso!')
        else:
            self.tabela_ano_modelo = pd.read_csv(f'datasets/tabela_ano_modelo_{mes2}.csv')
            print(f"Tabela de ano modelo já existe: tabela_ano_modelo_{mes2}.csv")

    def consulta_tabela_referencia(self):
        url = f"{self._base_url}/ConsultarTabelaDeReferencia"
        req = requests.post(url)
        req_text = req.text
        req_json = json.loads(req_text)
        df = pd.DataFrame(req_json)
        df.columns = ['codigo_mes', 'mes']
        df['mes'] = df['mes'].str.strip()

        return df

    def consulta_tabela_marcas(self):
        url = f"{self._base_url}/ConsultarMarcas"
        codigo_tabela_referencia = self.tabela_referencia.query(f"mes == '{self.mes}'").loc[:,'codigo_mes'][0]
        body = {"codigoTabelaReferencia": codigo_tabela_referencia, "codigoTipoVeiculo": self.codigo_tipo_veiculo}
        req = requests.post(url, data=body)
        req_text = req.text
        req_json = json.loads(req_text)
        df = pd.DataFrame(req_json).rename(columns={'Label': 'marca', 'Value': 'codigo_marca'})
        df['mes'] = self.mes
        return df

    def consulta_tabela_modelos(self):
        url = f"{self._base_url}/ConsultarModelos"
        codigo_tabela_referencia = self.tabela_referencia.query(f"mes == '{self.mes}'").loc[:,'codigo_mes'][0]
        df = pd.DataFrame()
        for codigo_marca in self.tabela_marcas['codigo_marca']:
            body = {"codigoTabelaReferencia": codigo_tabela_referencia, "codigoTipoVeiculo": self.codigo_tipo_veiculo, "codigoMarca": codigo_marca}
            req = requests.post(url, data=body)
            req_text = req.text
            req_json = json.loads(req_text)
            df_temp = pd.DataFrame(req_json['Modelos']).rename(columns={'Label': 'modelo', 'Value': 'codigo_modelo'})
            df_temp['codigo_marca'] = codigo_marca
            df = pd.concat([df, df_temp])
        df['mes'] = self.mes
        return df

    def consulta_tabela_ano_modelo(self):
        url = f"{self._base_url}/ConsultarAnoModelo"
        codigo_tabela_referencia = self.tabela_referencia.query(f"mes == '{self.mes}'").loc[:,'codigo_mes'][0]
        df = pd.DataFrame()
        for codigo_marca in self.tabela_marcas['codigo_marca']:
            for codigo_modelo in self.tabela_modelos.query(f"codigo_marca == '{codigo_marca}'").loc[:,'codigo_modelo']:
                body = {"codigoTabelaReferencia": codigo_tabela_referencia, "codigoTipoVeiculo": self.codigo_tipo_veiculo, "codigoMarca": codigo_marca, "codigoModelo": codigo_modelo}
                req = requests.post(url, data=body)
                print(req.status_code)
                req_text = req.text
                req_json = json.loads(req_text)
                df_temp = pd.DataFrame(req_json).rename(columns={'Label': 'combustivel', 'Value': 'ano'})
                df_temp['codigo_marca'] = codigo_marca
                df_temp['codigo_modelo'] = codigo_modelo
                df = pd.concat([df, df_temp])
        df['mes'] = self.mes
        return df

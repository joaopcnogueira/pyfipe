pyfipe
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install pyfipe
```

## How to use

``` python
import pandas as pd
```

``` python
from pyfipe.core import ConsultaFipe
from pyfipe.tabelas import consulta_tabela_referencia, consulta_tabela_marcas, consulta_tabela_modelos
```

``` python
fipe = ConsultaFipe(
    mes = 'agosto/2022',
    tipo_veiculo = 'carro',
    marca = 'VW - VolksWagen',
    modelo = 'T-Cross Sense 1.0 TSI Flex 5p Aut.',
    ano_modelo = 2021,
    combustivel = 'Gasolina'
)
```

``` python
fipe.preco()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Valor</th>
      <th>Marca</th>
      <th>Modelo</th>
      <th>AnoModelo</th>
      <th>Combustivel</th>
      <th>CodigoFipe</th>
      <th>MesReferencia</th>
      <th>Autenticacao</th>
      <th>TipoVeiculo</th>
      <th>SiglaCombustivel</th>
      <th>DataConsulta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>R$ 101.120,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>agosto de 2022</td>
      <td>f4wq6m4pj4djf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
  </tbody>
</table>
</div>

``` python
meses = ['janeiro/2022', 'fevereiro/2022', 'março/2022', 'abril/2022', 'maio/2022', 'junho/2022', 'julho/2022', 'agosto/2022']

df = pd.DataFrame()
for mes in meses:
    fipe.mes = mes
    fipe.update_codigo_tabela_referencia()
    df = pd.concat([df, fipe.preco()])

df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Valor</th>
      <th>Marca</th>
      <th>Modelo</th>
      <th>AnoModelo</th>
      <th>Combustivel</th>
      <th>CodigoFipe</th>
      <th>MesReferencia</th>
      <th>Autenticacao</th>
      <th>TipoVeiculo</th>
      <th>SiglaCombustivel</th>
      <th>DataConsulta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>R$ 94.854,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>janeiro de 2022</td>
      <td>cg6gzjs2n29fx</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 97.518,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>fevereiro de 2022</td>
      <td>ch6p797h88mfx</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 101.478,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>março de 2022</td>
      <td>f49rk6kznldjf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 102.808,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>abril de 2022</td>
      <td>f6v25c4673djf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 101.988,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>maio de 2022</td>
      <td>f5w868197ydjf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 101.854,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>junho de 2022</td>
      <td>f5rd7r84hvdjf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 102.021,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>julho de 2022</td>
      <td>f5yhd01kc3djf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
    <tr>
      <th>0</th>
      <td>R$ 101.120,00</td>
      <td>VW - VolksWagen</td>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>2021</td>
      <td>Gasolina</td>
      <td>005520-4</td>
      <td>agosto de 2022</td>
      <td>f4wq6m4pj4djf</td>
      <td>1</td>
      <td>G</td>
      <td>quarta-feira, 24 de agosto de 2022 12:04</td>
    </tr>
  </tbody>
</table>
</div>

Caso queira consultar apenas a tabela de referência da fipe:

``` python
consulta_tabela_referencia()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>codigo_mes</th>
      <th>mes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>288</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>1</th>
      <td>287</td>
      <td>julho/2022</td>
    </tr>
    <tr>
      <th>2</th>
      <td>286</td>
      <td>junho/2022</td>
    </tr>
    <tr>
      <th>3</th>
      <td>285</td>
      <td>maio/2022</td>
    </tr>
    <tr>
      <th>4</th>
      <td>284</td>
      <td>abril/2022</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>255</th>
      <td>69</td>
      <td>maio/2001</td>
    </tr>
    <tr>
      <th>256</th>
      <td>68</td>
      <td>abril/2001</td>
    </tr>
    <tr>
      <th>257</th>
      <td>67</td>
      <td>março/2001</td>
    </tr>
    <tr>
      <th>258</th>
      <td>63</td>
      <td>fevereiro/2001</td>
    </tr>
    <tr>
      <th>259</th>
      <td>62</td>
      <td>janeiro/2001</td>
    </tr>
  </tbody>
</table>
<p>260 rows × 2 columns</p>
</div>

Caso não saiba qual o código da marca do seu carro, poderá fazer uma
busca na tabela de marcas:

``` python
tabela_marcas = consulta_tabela_marcas(mes='agosto/2022', tipo_veiculo='carro')
tabela_marcas
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>marca</th>
      <th>codigo_marca</th>
      <th>mes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>1</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Agrale</td>
      <td>2</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alfa Romeo</td>
      <td>3</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AM Gen</td>
      <td>4</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Asia Motors</td>
      <td>5</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Troller</td>
      <td>57</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Volvo</td>
      <td>58</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>89</th>
      <td>VW - VolksWagen</td>
      <td>59</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Wake</td>
      <td>163</td>
      <td>agosto/2022</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Walk</td>
      <td>120</td>
      <td>agosto/2022</td>
    </tr>
  </tbody>
</table>
<p>92 rows × 3 columns</p>
</div>

``` python
tabela_marcas[fipe.tabela_marcas['marca'].str.contains('vw', case=False)]
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>marca</th>
      <th>codigo_marca</th>
      <th>mes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>89</th>
      <td>VW - VolksWagen</td>
      <td>59</td>
      <td>agosto/2022</td>
    </tr>
  </tbody>
</table>
</div>

Caso não saiba qual o código e descrição do seu modelo, pode consultar
na tabela de modelos

``` python
tabela_modelos = consulta_tabela_modelos(mes='agosto/2022', tipo_veiculo='carro', codigo_marca=59)
tabela_modelos
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>modelo</th>
      <th>codigo_modelo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AMAROK CD2.0 16V/S CD2.0 16V TDI 4x2 Die</td>
      <td>5585</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AMAROK CD2.0 16V/S CD2.0 16V TDI 4x4 Die</td>
      <td>5586</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AMAROK Comfor. 3.0 V6 TDI 4x4 Dies. Aut.</td>
      <td>9895</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AMAROK Comfor. CD 2.0 TDI 4x4 Dies. Aut.</td>
      <td>8531</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AMAROK CS2.0 16V/S2.0 16V TDI 4x2 Diesel</td>
      <td>5748</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>516</th>
      <td>VOYAGE SELEÇÃO 1.6 I MOTION T.Flex 8V 4p</td>
      <td>6672</td>
    </tr>
    <tr>
      <th>517</th>
      <td>VOYAGE SELEÇÃO 1.6 Total Flex 8V 4p</td>
      <td>6673</td>
    </tr>
    <tr>
      <th>518</th>
      <td>VOYAGE TREND 1.6 Mi Total Flex 8V 4p</td>
      <td>4755</td>
    </tr>
    <tr>
      <th>519</th>
      <td>VOYAGE Trendline 1.0 T.Flex 12V 4p</td>
      <td>7524</td>
    </tr>
    <tr>
      <th>520</th>
      <td>VOYAGE Trendline 1.6 T.Flex 8V 4p</td>
      <td>6809</td>
    </tr>
  </tbody>
</table>
<p>521 rows × 2 columns</p>
</div>

``` python
tabela_modelos[tabela_modelos['modelo'].str.contains('t-cross', case=False)]
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>modelo</th>
      <th>codigo_modelo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>450</th>
      <td>T-Cross 1.0 TSI Flex 12V 5p Aut.</td>
      <td>8641</td>
    </tr>
    <tr>
      <th>451</th>
      <td>T-Cross 1.0 TSI Flex 12V 5p Mec.</td>
      <td>8642</td>
    </tr>
    <tr>
      <th>452</th>
      <td>T-Cross Comfortline 1.0 TSI Flex 5p Aut.</td>
      <td>8643</td>
    </tr>
    <tr>
      <th>453</th>
      <td>T-Cross Highline 1.4 TSI Flex 16V 5p Aut</td>
      <td>8644</td>
    </tr>
    <tr>
      <th>454</th>
      <td>T-Cross Sense 1.0 TSI Flex 5p Aut.</td>
      <td>9564</td>
    </tr>
  </tbody>
</table>
</div>

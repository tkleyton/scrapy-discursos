# Discursos da câmara
Extrai os discursos proferidos pelos deputados nas sessões da câmara de forma automatizada diretamente do [website da câmara](https://www.camara.leg.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp?txIndexacao=&CurrentPage=1&BasePesq=plenario&txOrador=&txPartido=&dtInicio=01/01/2019&dtFim=31/12/2019&txUF=&txSessao=&listaTipoSessao=&listaTipoInterv=&inFalaPres=&listaTipoFala=&listaFaseSessao=&txAparteante=&listaEtapa=&CampoOrdenacao=dtSessao&TipoOrdenacao=DESC&PageSize=50&txTexto=&txSumario=).

## Instalação
```
$ git clone https://github.com/tkleyton/scrapy-discursos
$ cd camara
$ pip install -r requirements.txt
$ scrapy crawl camara
```

## Modificando
As datas de início e fim da pesquisa estão no endereço na variável `start_urls` no arquivo [`camara/spiders/camara_2020.py`](camara/spiders/camara_2020.py)

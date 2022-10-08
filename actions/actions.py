# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import datetime

import requests


class ActionCotacaoDolar(Action):

    def name(self) -> Text:
        return "cotacao_dolar"

    def cotacao_dolar(self):
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

        cotacao = requisicao.json()

        moeda = cotacao['USD']['name']
        data = cotacao['USD']['create_date']
        valor = "%.2f" % float(cotacao['USD']['bid'])

        texto = f'''
        Cotação do Dólar - >
        Moeda: {moeda}
        Data:  {data} 
        Valor atual: R${valor} 
        '''
        return texto

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=self.cotacao_dolar())

        return []


class ActionCotacaoEuro(Action):

    def name(self) -> Text:
        return "cotacao_euro"

    def cotacao_euro(self):
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')

        cotacao = requisicao.json()

        moeda = cotacao['EUR']['name']
        data = cotacao['EUR']['create_date']
        valor = "%.2f" % float(cotacao['EUR']['bid'])

        texto = f'''
        Cotação do Euro - >
        Moeda: {moeda}
        Data:  {data} 
        Valor atual: R${valor} 
        '''
        return texto

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=self.cotacao_euro())

        return []


class ActionDataHora(Action):

    def name(self) -> Text:
        return "data_hora"

    def data_hora(self):
        texto = str(datetime.datetime.now())
        return texto

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=self.data_hora())

        return []


class ActionCEP(Action):

    def name(self) -> Text:
        return "pesquisar_cep"

    def pesquisar_cep(self, tracker=Tracker):

        cep = tracker.get_slot("cep")

        requisicao = requests.get(f'https://cdn.apicep.com/file/apicep/{cep}.json')

        cep_pesquisado = requisicao.json()

        estado = cep_pesquisado['state']
        cidade = cep_pesquisado['city']
        distrito = cep_pesquisado['district']
        rua = cep_pesquisado['address']

        texto = f'''
        CEP Pesquisado -> {cep}
        ----------------------------------
        ESTADO: {estado}
        CIDADE: {cidade}
        DISTRITO: {distrito}
        RUA: {rua}
        ----------------------------------
        '''

        ret = {"text": texto}

        return ret

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=self.pesquisar_cep())

        return []

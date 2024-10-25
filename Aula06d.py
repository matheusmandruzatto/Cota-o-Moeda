from kivy.app import App
from kivy.lang import Builder
import requests

class MeuAplicativo(App):
    def build(self):
        return Builder.load_file("Aula06d_tela.kv")

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        try:
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
            return cotacao
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"erro ao pegar a cotação: {e}")
            return "erro"

    def mostrar_cotacao(self, moeda):
        cotacao = self.pegar_cotacao(moeda)
        self.root.ids['resultado'].text = f"{moeda}: R${cotacao}"

if __name__ == '__main__':
    MeuAplicativo().run()

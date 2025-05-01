import requests
import webbrowser
from googletrans import Translator

# a chave que eu recebi
API_KEY = "b1e03343"

# função pra buscar as informações dados do filme
def buscar_filme(nome):
    url = f"http://www.omdbapi.com/?t={nome}&apikey={API_KEY}"
    try:
        resp = requests.get(url)
        dados = resp.json()

        if dados.get("Response") == "True":
            return dados
        else:
            print("ERRO! Filme não encontrado")
            return None
    except Exception as e:
        print(f"Erro ao consultar a API: {e}")
        return None 
    
def traduzir_texto(texto, para="pt"):
    try:
        translator = Translator()
        resultado = translator.translate(texto, dest=para)
        return resultado.text
    except Exception as e:
        print(f"ERRO! Tradução com Google Translate indisponível: {e}")
        return "(tradução indisponível)"

# entrada
print("🎬 Buscador de Filmes - OMDb API\n")
nome_filme = input("Digite o nome do filme: ")

filme = buscar_filme(nome_filme)

# resultado
if filme:
    print("\nDetalhes do filme:")
    print(f"Título: {filme['Title']}")
    print(f"Ano: {filme['Year']}")
    print(f"Diretor: {filme['Director']}")
    print(f"⭐  Nota IMDb: {filme['imdbRating']}")
    print(f"Gênero: {filme['Genre']}")
    sinopse_original = filme["Plot"]
    sinopse_traduzida = traduzir_texto(sinopse_original)
    print(f"📝 Sinopse: {sinopse_traduzida}")
    print(f"Poster: {filme['Poster']}")
    abrir = input("\n🔗 Deseja abrir o pôster no navegador? (s/n): ").lower()
    if abrir == "s":
        webbrowser.open(filme["Poster"])
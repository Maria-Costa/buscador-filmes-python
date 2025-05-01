## Buscador de Filmes com Python

Este é um projeto simples feito em Python que permite buscar informações de filmes através da **OMDb API**. 
Além de mostrar os dados do filme, também traduz automaticamente a sinopse para português através do 'googletrans' e oferece a opção de abrir o pôster no próprio navegador.

---

## Informações importantes

- `requests` → para consumir a OMDb API
- `googletrans` → para tradução automática via Google Translate
- `webbrowser` → para abrir o pôster no navegador

---

## Para utilizar

1. Garanta que o Python está instalado na sua máquina
2. Clone este repositório ou baixe os arquivos
2. Instale as dependências com:

```bash
pip install requests googletrans==4.0.0-rc1

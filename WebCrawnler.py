import requests
from bs4 import BeautifulSoup

def get_meta_tags(soup):
    meta_tags = soup.find_all('meta')
    return meta_tags

def get_body_content(soup):
    return soup.body

def remove_repeated_items(list_links):
    return list(set(list_links))

def filter_https_links(list_links):
    filtered_links = []
    for link in list_links:
        if link.startswith('https://'):
            filtered_links.append(link)
    return filtered_links

def get_links(url, profundidade, contador, lista):  

    try:
        #captura todos os dados da página e joga no banco de dados
        response = requests.get(url, timeout=1).content
        soup = BeautifulSoup(response, 'html.parser')
        print('/n',contador, url)       

        listaTemp = dict()
        listaTemp['url'] = url
        listaTemp['meta_tags'] = get_meta_tags(soup)
        listaTemp['body'] = get_body_content(soup)

        lista.append(listaTemp)

        # após essa página for capturada verifica se ela é a ultima, se sim ele retorna se não pega todos os links dela 
        if profundidade == contador:
            print('chegou na profundidade\n')
            return
    
        contador+=1
        
        list_links = []
        for tag_a in soup.find_all('a'):
            link = tag_a.get('href')
            if link:
                list_links.append(link)    

        # tratando links
        list_links = remove_repeated_items(list_links)
        list_links = filter_https_links(list_links)

        #acessando links recursivamente
        for link in list_links:
            get_links(link, profundidade, contador, lista)

    except requests.exceptions.Timeout:
        print("Timeout de conexão. ", url)
        return
    
    except Exception as e:
        print("Ocorreu um erro:", e, url)
        return

lista = []
get_links("https://olhardigital.com.br/", 1, 0, lista)

with open("database.json", "w") as f:
    f.write(str(lista))


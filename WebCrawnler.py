import requests
from bs4 import BeautifulSoup


#firebase - firebase.FirebaseApplication('https://')

def get_meta_tags(soup):
    meta_tags = soup.find_all('meta')
    return meta_tags

def get_body_content(soup):
    body = soup.body
    body_content = body.get_text()
    return body_content

def remove_repeated_items(list_links):
    return list(set(list_links))

def filter_https_links(list_links):
    filtered_links = []
    for link in list_links:
        if link.startswith('https://'):
            filtered_links.append(link)
    return filtered_links

def get_links(url, profundidade, contador):  
    if profundidade == contador:
        return
    
    contador+=1

    print(contador, url)

    try:
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'html.parser')

        list_links = []
        for tag_a in soup.find_all('a'):
            link = tag_a.get('href')
            if link:
                list_links.append(link)    

        list_links = remove_repeated_items(list_links)
        list_links = filter_https_links(list_links)

        for link in list_links:
            get_links(link, profundidade, contador) 
    except:
        print("esse deu erro")

    

get_links("https://olhardigital.com.br/", 2, 0) 




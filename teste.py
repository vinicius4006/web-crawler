import requests
from bs4 import BeautifulSoup
import threading

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

    print(url)

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
            thread = threading.Thread(target=get_links, args=(link, profundidade, contador))
            thread.start()
    except:
        print("esse deu erro")

def get_links_thread(url, profundidade):
    thread = threading.Thread(target=get_links, args=(url, profundidade, 0))
    thread.start()

get_links_thread("https://g1.globo.com/", 2)

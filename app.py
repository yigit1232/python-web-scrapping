from bs4 import BeautifulSoup as bs
import requests

def get_post():
    url = "https://www.webtekno.com/"
    request = requests.get(url)
    html = bs(request.text,'html.parser')
    content = html.find_all('div',{'class':'content-timeline__item'})
    for i in content:
        try:
            title = i.find('h3',{'class':'content-timeline__detail__title'})
            category = i.find('h5',{'class':'content-timeline__detail__category'})
            author = i.find('a',{'class':'content-timeline__detail__author hide-phone'})
            time = i.find('span',{'class':'content-timeline__time__timeago'})
            url = i.find('a',{'class':'content-timeline__link clearfix'})
            url = url.get('href')
            print(f"""
            Kategori: {category.text}
            Başlık: {title.text}
            Yazar: {author.text}
            Zaman: {time.text}
            Link: {url}
            """)
        except AttributeError:
            print(f"""
            Kategori: {category.text}
            Başlık: {title.text}
            Yazar: Yazar yok.
            Zaman: {time.text}
            Link: {url}
            """)

def get_popular():
    url = "https://www.webtekno.com/"
    request = requests.get(url)
    html = bs(request.text, 'html.parser')
    content = html.find_all('div', {'class': 'sidebar-mosts__item__body'})
    print("""
            Bugün En Çok Okunanlar
            ----------------------
    """)
    for i in content:
        title = i.find('h3',{'class':'sidebar-mosts__item__title'})
        count = i.find('span',{'class':'sidebar-mosts__item__count'})
        print(f"""
            Başlık: {title.text}
            Görüntülenme Sayısı: {count.text}
                
            *********************************
        """)

get_post()
get_popular()
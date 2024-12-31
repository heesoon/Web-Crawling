import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://crawler-test.com/'

    response = requests.get(url)
    if response.status_code == 200:
        print('success to access web site %s' % url)
    else:
        print('fail to access web site: %s' % url)
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. HTML 문서의 타이틀 (head -> title)
    print("\n Web Site title:")
    title = soup.title
    if title:
        print(title.get_text())
    else:
        print("No title")
    
    # 2. 모든 링크 (a 태그)
    print("\n Link Colleciton:")
    links = soup.find_all('a')
    for link in links[:10]:
        href = link.get('href')
        text = link.get_text()
        print(f"Link Text: {text}, Link Address: {href}")
    
    # 3. 모든 이미지 (img 태그)
    print("\n All Images:")
    images = soup.find_all('img')
    for img in images[:5]:
        img_src = img.get('src')
        img_alt = img.get('alt')
        print(f"Image Source: {img_src}, ALT text: {img_alt}")
    
    # 4. 웹사이트의 메타 태그 정보 (head -> meta)
    print("\n All Meta Information:")
    metas = soup.find_all('meta')
    for meta in metas:
        meta_name = meta.get('name')
        meta_content = meta.get('content')
        print(f"Meta Name: {meta_name}, Meta Content: {meta_content}")
    
    # 5. 웹사이트의 주요 콘텐츠 (예: h1, h2, p 태그)
    print("\n Web Site Main Contents:")
    headings = soup.find_all(['h1', 'h2', 'p'])
    for heading in headings[:5]:
        print(f"{heading.name}: {heading.get_text()}")

if __name__ == '__main__':
    main()



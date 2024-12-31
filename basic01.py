import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.w3.org/standards/'

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

    # 6. 비디오 파일 URL 추출 및 다운로드 (video 태그 또는 a 태그에서 비디오 파일 링크 찾기)
    print("\n Video Files:")
    video_urls = []
    for video in soup.find_all('video'):
        sources = video.find_all('source')
        for source in sources:
            video_url = source.get('src')
            if video_url:
                video_urls.append(video_url)
    
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href.endswith(('mp4', 'webm', 'avi', 'mov')):
            video_urls.append(href)
    
    if video_urls:
        for idx, video_url in enumerate(video_urls):
            if not video_url.startswith('http'):
                video_url = url + video_url
            
            try:
                video_response = requests.get(video_url, stream=True)
                if video_response.status_code == 200:
                    video_filename = f"video_{idx+1}.mp4"
                    with open(video_filename, 'wb') as f:
                        for chunk in video_response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    print(f"video download completed: {video_filename}")
                else:
                    print(f"video download falied: {video_url}")
            except requests.exceptions.RequestException as e:
                print(f"error during video downloading: {video_url} - {e}")
    else:
        print(f"No video file in the website")

if __name__ == '__main__':
    main()



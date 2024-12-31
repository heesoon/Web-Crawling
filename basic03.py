import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO
import cairosvg  # SVG를 PNG로 변환하는 라이브러리

# 웹 페이지 URL
url = 'https://www.w3.org/standards/'  # 원하는 웹사이트 URL로 변경

# 웹 페이지 요청
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    print("웹 페이지를 성공적으로 가져왔습니다.")
else:
    print(f"웹 페이지 가져오기 실패. 상태 코드: {response.status_code}")
    exit()

# 웹 페이지 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 텍스트 추출 (예: <h1>, <p> 태그)
text = ""
for paragraph in soup.find_all(['h1', 'h2', 'p']):
    text += paragraph.get_text() + "\n"

# PDF 파일 생성
pdf_filename = "D:\Project\Web-Crawling\output_with_images.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter

# 텍스트를 PDF에 추가
y_position = height - 40  # PDF 상단에서 시작하는 y 위치
line_height = 14  # 한 줄의 높이

for line in text.splitlines():
    if y_position < 40:  # 페이지 끝에 다다르면 새 페이지 추가
        c.showPage()
        y_position = height - 40
    c.drawString(40, y_position, line)
    y_position -= line_height

# 이미지 추출 및 PDF에 추가
for img_tag in soup.find_all('img'):
    img_url = img_tag.get('src')
    if img_url:
        # 이미지 URL이 절대 경로가 아닐 경우
        if not img_url.startswith('http'):
            img_url = url + img_url

        try:
            # 이미지 다운로드
            img_response = requests.get(img_url)

            # 이미지 응답이 성공적이고 이미지 형식이 유효한지 확인
            if img_response.status_code == 200:
                # SVG 형식인 경우 PNG로 변환
                if img_url.endswith('.svg'):
                    # cairosvg를 사용하여 SVG를 PNG로 변환
                    png_image = cairosvg.svg2png(bytestring=img_response.content)

                    # 변환된 PNG 이미지를 PIL로 열기
                    img = Image.open(BytesIO(png_image))
                else:
                    # 다른 형식의 이미지 (예: PNG, JPEG)
                    img = Image.open(BytesIO(img_response.content))
                
                # 이미지를 PDF에 삽입
                img_path = "temp_image.jpg"
                img.save(img_path)  # 임시 파일로 저장
                c.drawImage(img_path, 40, y_position - 100, width=500, height=100)
                y_position -= 120  # 이미지가 들어갔으므로 공간을 줄여줌

        except (requests.exceptions.RequestException, IOError) as e:
            print(f"이미지 다운로드 실패 또는 형식 오류: {img_url} - {e}")

# PDF 저장
c.save()
print(f"PDF 파일이 '{pdf_filename}'로 저장되었습니다.")

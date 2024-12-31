import requests
import io
import PyPDF2  # 또는 pdfplumber

# PDF 파일 URL (W3C 사이트의 WCAG Quick Reference PDF)
pdf_url = 'https://www.w3.org/WAI/WCAG21/quickref/pdf/quickref.pdf'

# PDF 파일을 메모리로 로드
response = requests.get(pdf_url)

# HTTP 요청이 성공했는지 확인
if response.status_code == 200:
    print("PDF 파일을 성공적으로 다운로드했습니다.")
else:
    print(f"PDF 파일 다운로드 실패. 상태 코드: {response.status_code}")
    exit()

# 메모리에서 PDF 파일 처리
pdf_file = io.BytesIO(response.content)

# PyPDF2를 사용하여 PDF 읽기
reader = PyPDF2.PdfReader(pdf_file)

# 첫 페이지 텍스트 추출
first_page = reader.pages[0]
text = first_page.extract_text()

# 첫 페이지 텍스트 출력
print("첫 페이지 텍스트:")
print(text)

# pdfplumber를 사용하여 더 정교하게 텍스트를 추출하고 싶다면 아래와 같이 사용
# pdf_file.seek(0)  # pdfplumber는 파일 포인터를 처음으로 돌려줘야 합니다.
# with pdfplumber.open(pdf_file) as pdf:
#     first_page = pdf.pages[0]
#     text = first_page.extract_text()
#     print(text)

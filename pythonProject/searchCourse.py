import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
url = "https://www.neti.go.kr/homepage/educourse/eduCourseList.go"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
data_rows = soup.find("table", attrs={"class":"board_list table_txt_center"}).find("tbody").find_all("tr")
#print(data_rows[0])
for row in data_rows:
    columns = row.find_all("td")
    for column in columns:
        data = column.get_text().strip()
        print(data)
    #data = [column.get_text().strip() for column in columns]
    #print(data)

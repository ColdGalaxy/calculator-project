import requests
from bs4 import BeautifulSoup

response = requests.get("https://my.numworks.com/python/alexanderdouglas1311",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
#print(response.headers)
if response.status_code == 200:
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    code = [(c["script-name"],c["script-content"]) for c in soup.find_all("send-to-calculator")]
    print(code)
else:
    raise Exception("Error while fetching site:",response.status_code)

for name,src in code:
    with open("Numworks/"+name,"w",encoding="utf-8") as file:
        file.write(src)

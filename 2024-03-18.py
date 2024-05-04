import requests
import re
from openpyxl import load_workbook
from openpyxl import Workbook

email_string = """
abc@example.com
adc@example.com
abc@example.com
aqc@example.com
adkfqnkrl@odd.kr
dt.fc
dki
do
@e.com
"""

url = "http://thormarket.kro.kr"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-type': 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers)

result_1 = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
print(result_1)

results = re.findall(r'[\w\.-]+@[\w\.-]+', email_string)
results = list(set(results))
print(results)
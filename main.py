from bs4 import BeautifulSoup
import json 

question = {}
key, value = [], []

file_path = 'Kiểm tra kiến thức Chương 8 Attempt review.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

qtext_elements = soup.find_all(class_='qtext')


for element in qtext_elements:
    text = element.get_text()  
    key.append(text)
    
checked_inputs = soup.find_all('input', {'checked': 'checked'})
checked_texts = []

for input_tag in checked_inputs:
    div_next = input_tag.find_next('div', {'class': 'flex-fill ml-1'})
    if div_next:
        text = div_next.get_text(strip=True)
        checked_texts.append(text)

for text in checked_texts:
    value.append(text)
    
for i in range(len(key)):
    question[key[i]] = value[i]
    
with open('chuong_8.json', 'w') as json_file:
    json.dump(question, json_file)


#creating file with tmnote extension
with open("hello.tmnote",'w') as my_file:
    my_file.write("Example of tmnote working")

# Extracting bold italic fonts

from bs4 import BeautifulSoup

file_path = r"D:\dads\Telegram Web.mhtml"
HtmlFile = open(file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read()
html = BeautifulSoup(source_code, 'html.parser')
page_body = html.find('div', class_='history')
messages_3 = page_body.find('div', id="message3927")
messages_4 = messages_3.find('div', class_="text")
strong_tag = messages_4.find('strong')
italic_tag = messages_4.find('i')
quote_tag = messages_4.find('em')
underline_tag = messages_4.find('u')
strikethough_tag = messages_4.find('del')
if strong_tag:
    strong_text = strong_tag.text
    print("**"+strong_text+"**")
elif italic_tag:
    italic_text = italic_tag.text
    print("*" + italic_text + "*")
elif strikethough_tag:
    strikethough_text = strikethough_tag.text
    print("~~" + strikethough_text + "~~")


print(messages_4)
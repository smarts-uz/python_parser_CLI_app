from bs4 import BeautifulSoup


class Pars:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_html(self):
        HtmlFile = open(self.file_path, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        soup = BeautifulSoup(source_code, 'html.parser')
        return soup

    def parsing(self):
        soup = self.get_html()
        history = soup.find('div', class_="history")
        main_messages = history.find_all('div',class_='message default clearfix')

        # print(len(main_messages))
        for main_message in main_messages[0:1]:
            message_body = main_message.find('div',class_='body')
            date = message_body.find('div', class_='pull_right date details').get_text(strip=True)
            from_name = message_body.find('div',class_='from_name').get_text(strip=True)
            content = message_body.find('div',class_='text').get_text(strip=True)
            print(content)
        # return main_messages

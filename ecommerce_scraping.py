import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
import bs4 as bs
from urllib2 import urlopen


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = 'https://www.deliveryextra.com.br/busca?w=cerveja&qt=12&p=2&gt=list'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
beer_list = soup.findAll('div', class_='panel-product')
for beer in beer_list:
    name = beer['produto-nome']
    preco = beer['produto-preco']
    if name and preco:
        print('Name: %s' % (name))
        print('Name: %s\n' % (preco))

import re
import requests
from bs4 import BeautifulSoup
from abc import abstractmethod, ABCMeta
from fake_useragent import UserAgent
# from datetime import datetime


class Crowler:

    ####################################################################################################

    class Site(metaclass=ABCMeta):

        @abstractmethod
        def get_beautifulsoup(self):
            pass

        @abstractmethod
        def get_board(self):
            pass

        @abstractmethod
        def get_post(self):
            pass

    class NATEPANN(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'https://pann.nate.com/talk/c20030', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip()
                      for title in soup.select('.subject') if title.a.text.strip() != '[웃긴썰]']
            links = ['https://pann.nate.com' + link.a['href']
                     for link in soup.select('.subject') if link.a['href'].endswith('1')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' :.*', '', soup.head.title.text)
            content = soup.find(id='contentArea')
            return title, content

    class DCINSIDE(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            header['Content-Type'] = 'application/json; charset=utf-8'
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'https://gall.dcinside.com/board/lists?id=issuezoom', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip()
                      for title in soup.select('.gall_tit')][1:]
            links = ['https://gall.dcinside.com' + link.a['href']
                     for link in soup.select('.gall_tit')][1:]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' - .*', '', soup.find(name='title').text)
            content = soup.find(style='overflow:hidden;')
            return title, content

    class RULIWEB(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'https://bbs.ruliweb.com/best/humor/hit?orderby=readcount&range=24h', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip()
                      for title in soup.select('.subject')[1:]]
            links = [link.a['href'] for link in soup.select('.subject')[1:]]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' \|.*', '', soup.title.text)
            content = soup.select('.view_content')[0]
            return title, content

    class PPOMPPU(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'http://www.ppomppu.co.kr/zboard/zboard.php?id=humor', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.text.strip()
                      for title in soup.select('.list_title')[1:]]
            links = ['http://www.ppomppu.co.kr/zboard/' + link.parent['href']
                     for link in soup.select('.list_title')[1:]]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = soup.find(property='og:title')['content']
            content = soup.select('.pic_bg')[2]
            return title, content

    class FMKOREA(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'https://www.fmkorea.com/index.php?mid=humor&sort_index=pop&order_type=desc&listStyle=list&page=1', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip()
                      for title in soup.select('.title.hotdeal_var8')]
            links = ["https://www.fmkorea.com/" + link.a['href']
                     for link in soup.select('.title.hotdeal_var8')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' - .*', '', soup.find('title').text)
            content = soup.article.div
            return title, content

    class TODAYHUMOR(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=1', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip()
                      for title in soup.select('.subject')]
            links = ["http://www.todayhumor.co.kr" + link.a['href']
                     for link in soup.select('.subject')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = soup.find(property='og:title').text
            content = soup.select('.viewContent')[0]
            return title, content

    class YGOSU(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'https://www.ygosu.com/community/real_article', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip() for title in soup.select('.tit')]
            links = [link.a['href'] for link in soup.select('.tit')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = soup.find(name='title').text
            content = soup.select('.container')[0]
            return title, content

    class HUMORUNIV(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header)
            else:
                html_text = requests.get(
                    'http://web.humoruniv.com/board/humor/list.html?table=pick', headers=header)
            html_text.encoding = 'euc-kr'
            html_text = html_text.text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.text.strip() for title in soup.select('.li_sbj')]
            titles = [re.sub(r'(?ms)\r.*', '', title) for title in titles]
            links = ['http://web.humoruniv.com/board/humor/' +
                     link.a['href'] for link in soup.select('.li_sbj')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' ::.*', '', soup.head.title.text)
            content = soup.find(id='cnts')
            return title, content

    class ETOLAND(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'http://www.etoland.co.kr/bbs/board.php?bo_table=etohumor03&sfl=top_n&stx=day&sst=wr_hit&sod=desc', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.a.next_sibling.next_sibling.next_sibling.next_sibling.span.text for title in soup.select(
                '.mw_basic_list_subject')]
            links = ["http://www.etoland.co.kr/" + link.a.next_sibling.next_sibling.next_sibling.next_sibling['href'][2:]
                     for link in soup.select('.mw_basic_list_subject')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = soup.find(name='title').text
            content = soup.find(id='view11_content')
            return title, content

    class INVEN(Site):

        def get_beautifulsoup(self, link=None):
            header = Crowler.get_random_header()
            if link:
                html_text = requests.get(link, headers=header).text
            else:
                html_text = requests.get(
                    'http://www.inven.co.kr/board/webzine/2097?my=chu&category=%EC%9C%A0%EB%A8%B8&sort=PID&iskin=webzine', headers=header).text
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup

        def get_board(self):
            soup = self.get_beautifulsoup()
            titles = [title.text.strip()[5:]
                      for title in soup.select('.sj_ln')]
            links = [link['href'] for link in soup.select('.sj_ln')]
            return titles, links

        def get_post(self, link):
            soup = self.get_beautifulsoup(link)
            title = re.sub(r' - .*', '', soup.find(name='title').text)
            content = soup.find(id='powerbbsContent')
            return title, content

    ####################################################################################################

    site_list = sorted(['NATEPANN', 'DCINSIDE', 'RULIWEB', 'PPOMPPU',
                        'FMKOREA', 'TODAYHUMOR', 'YGOSU', 'HUMORUNIV', 'ETOLAND', 'INVEN'])

    def __init__(self):
        self._site = None

    @staticmethod
    def get_random_header():
        user_agent = UserAgent(verify_ssl=False).random
        # user_agent = "Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
        header = {'User-Agent': user_agent}
        return header

    def get_site_list(self):
        return self.__class__.site_list

    def site(self, site_factory):
        self._site = self.__class__.__dict__[site_factory]()
        return self._site

    ####################################################################################################


if __name__ == "__main__":

    # Crowler의 dict에 팩토리 클래스가 보이지 않도록 하는 좋은 방법이 없을까?

    # 크롤링 객체를 생성한다.
    cro = Crowler()

    # 사이트 리스트를 출력한다.
    # print(cro.get_site_list())
    # ['DCINSIDE', 'ETOLAND', 'FMKOREA', 'HUMORUNIV', 'INVEN', 'NATEPANN', 'PPOMPPU', 'RULIWEB', 'TODAYHUMOR', 'YGOSU']

    # # 해당 사이트의 게시판을 크롤링한다.
    # data = cro.site('NATEPANN').get_board()
    # print(data)

    # # 해당 사이트의 게시물을 크롤링한다.
    # # 네이트판 = https://pann.nate.com/talk/352201801?page=1
    # # 디씨 = https://gall.dcinside.com/board/view/?id=issuezoom&no=8409&_rk=unp&page=1
    # # 루리웹 = https://bbs.ruliweb.com/best/board/300143/read/47511668
    # # 뽐뿌 = http://www.ppomppu.co.kr/zboard/view.php?id=humor&page=1&divpage=70&no=389801
    # # 에펨 = https://www.fmkorea.com/index.php?mid=humor&sort_index=pop&order_type=desc&listStyle=list&document_srl=2943294021
    # # 오유 = http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=427021&s_no=427021&page=1
    # # 와고 = https://www.ygosu.com/community/real_article/food/63635/?page=0&frombest=Y
    # # 웃대 = http://web.humoruniv.com/board/humor/read.html?table=pick&pg=0&number=969032
    # # 이토랜드 = http://www.etoland.co.kr/bbs/board.php?bo_table=etohumor03&wr_id=630073&sfl=top_n&stx=day&sst=wr_hit&sod=desc
    # # 인벤 = http://www.inven.co.kr/board/webzine/2097/1432455?my=chu&category=%EC%9C%A0%EB%A8%B8&iskin=webzine
    # print(data)

    import os

    cnt = cro.site('INVEN').get_post(
        'http://www.inven.co.kr/board/webzine/2097/1442305?my=chu&category=%EC%9C%A0%EB%A8%B8&iskin=webzine')[1]

    # 게시물 크롤링으로 반환된 값들중 src형식의 값들을 가져온다.
    img_tags = cnt.select('*[src]')

    # 해당 이미지들 중에서 html의 타입과 링크만을 추출한다.
    f = [(link.name, link['src'])
         for link in img_tags if any(link['src'].endswith(ext) for ext in ('jpg', 'jpeg', 'png', 'mp4', 'webm', 'gif', 'mp4?d', 'WEBP'))]

    for tag, link in f:
        print(tag, link)
        print(os.path.basename(link))
        if link.endswith('?d'):
            file_name = os.path.basename(link)[:-2]
        else:
            file_name = os.path.basename(link)
        # 네이트판 = 링크 그대로 받으면 된다.
        # 디씨 = 파일의 확장자를 알아낼 방법이 지나치게 복잡하다. 포기.
        # 루리웹 = "https:{}".format(link[:2])
        # 뽐뿌 = 'https:{}'.format(link)
        # 에펨 = 'https:{}'.format(link)
        # 뽐뿌 = 링크 그대로 받으면 된다.
        # 와고 = 링크 그대로 받으면 된다.
        # 웃대 = 파일 링크 형식이 이상하다. gif, mp4, 몇몇 이미지가 클릭해야만 본래 파일로 들어가지는 형식. 해결 가능하려나?
        # 이토렌드 = "http://www.etoland.co.kr{}".format(link)
        r = requests.get("{}".format(link), allow_redirects=True)
        open(file_name, 'wb').write(r.content)

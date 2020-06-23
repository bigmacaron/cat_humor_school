NATEPANN = {
    'post_title':None, 
    'post_cnt':None,
    'board_link':'https://m.pann.nate.com/talk/c20030',
    'board_titles':None, 
    'board_links':None
    }

DCINSIDE = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'https://m.dcinside.com/board/issuezoom',
    'board_titles':None, 
    'board_links':None
    }

RULIWEB = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'https://m.ruliweb.com/best/humor/hit?range=24h&orderby=regdate',
    'board_titles':None, 
    'board_links':None
    }

PPOMPPU = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'http://m.ppomppu.co.kr/new/bbs_list.php?id=humor',
    'board_titles':None, 
    'board_links':None
    }

FMKOREA = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'https://m.fmkorea.com/index.php?mid=humor&sort_index=pop&order_type=desc&listStyle=list&page=1',
    'board_titles':None, 
    'board_links':None
    }

TODAYHUMER = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'http://m.todayhumor.co.kr/list.php?table=bestofbest&page=1',
    'board_titles':None, 
    'board_links':None
    }

YGOSU = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'https://m.ygosu.com/board/real_article',
    'board_titles':None, 
    'board_links':None
    }

HUMORUNIV = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'http://m.humoruniv.com/board/list.html?table=pick',
    'board_titles':None, 
    'board_links':None
    }

ETOLAND = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'http://www.etoland.co.kr/plugin/mobile/board.php?bo_table=etohumor03&sfl=top_n&stx=day&sst=wr_hot&sod=desc',
    'board_titles':None, 
    'board_links':None
    }

INVEN = {
    'post_title':None, 
    'post_cnt':None, 
    'board_link':'http://m.inven.co.kr/board/webzine/2097?iskin=webzine&category=%EC%9C%A0%EB%A8%B8&my=chu',
    'board_titles':None, 
    'board_links':None
    }

if __name__ == '__main__':

    import requests
    from bs4 import BeautifulSoup

    user_agent = "Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"

    def html(site):
        return requests.get(site['board_link'], headers={'User-Agent':user_agent}).text

    # [ board ]

    # # INVEN
    # soup = BeautifulSoup(html(INVEN), features='html.parser')
    # titles = [tag.strong.next_sibling.strip() for tag in soup.select('.subject > .title')]
    # print(titles)
    # links = [tag['href'] for tag in soup.select('.subject')]

    # # ETOLAND
    # soup = BeautifulSoup(html(ETOLAND), features='html.parser')
    # titles = [tag.a.div.font.next_sibling.strip() for tag in soup.select('.subject')]
    # links = [tag['href'] for tag in soup.select('.subject > a')]

    # # HUMORUNIV
    # def html2(site):
    #     html = requests.get(site['board_link'], headers={'User-Agent':user_agent})
    #     html.encoding = 'euc-kr'
    #     return html.text
    # soup = BeautifulSoup(html2(HUMORUNIV), features='html.parser')
    # titles = [tag.text for tag in soup.select('span[id*="title_chk_pds"]')]
    # links = [tag['href'] for tag in soup.select('.list_body_href')]

    # # YGOSU
    # soup = BeautifulSoup(html(YGOSU), features='html.parser')
    # titles = [tag.next_sibling.strip() for tag in soup.select('.category')]
    # links = [tag['href'] for tag in soup.select('.li2 > li > a')]
import requests
import urllib

if __name__ == "__main__":

    # 확인된 사항은 DC만 이미지 다운로드시 opener를 설정해줄 필요가 있다는 사실.

    url = 'https://gall.dcinside.com/board/view/?id=issuezoom&no=8573&_rk=96k&page=1'
    opener = urllib.request.build_opener()
    opener.addheaders = [("Referer", url)]
    urllib.request.install_opener(opener)

    f = 'https://dcimg4.dcinside.co.kr/viewimage.php?id=25bcde31edd33da769b3d3a629df212a&no=24b0d769e1d32ca73ced8efa11d02831dd2ecabb386674d2cf3d2b24d2c3634e5da57ac61c6c658c06eddde4a73eb97a37d95f83ca17297a02c8403c18862332745edccf191bac16fd7a03'
    urllib.request.urlretrieve(f, 'test.jpg')
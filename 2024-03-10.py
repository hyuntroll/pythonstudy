import qrcode


file_path = 'webs.txt'
url_list = []
qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

with open(file_path, 'rt', encoding='utf8') as f:
    url_list = f.readlines()
    url_list = [line.strip() for line in url_list] #strip()는 각 줄의 양쪽 끝에 있는 공백문자 삭제 \n 그거를 url_list만큼 반복해서 line을 저장

for i in url_list:
    qr_img = qrcode.make(i)
    if '/' in i:
        i = i.replace('/', '_') # /문자를 _로 변환 이름에 /가 들어갈 수 없기 때문 
    save_path = 'img\\' + i + '.png'
    print(type(i), qr_img, save_path, type(qr_img), type(save_path)) #타입 확인
    qr_img.save(save_path) #qr img를 저장

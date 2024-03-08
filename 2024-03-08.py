from gtts import gTTS
from playsound import playsound
import os

#tts.save(r"mp3\nice_to_meet_you.mp3")
#r""에 r은 파이썬에서 특별한 명령어로 해석하지 않게 해준다. (원래 문자열에 경로를 나타낼 땐 \\라 해줘야 한다.)

#경로를 .py파일의 실행경로로 이동( 현재 경로로 이동 )
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = 'test.txt'

s_str ="안녕하세요 여러분 반갑습니다 저는 매우 잘생긴 "

f = open("test.txt", 'r')
#f = open("파일 이름", '모드') r: 읽기, w: 쓰기, a: 추가 ( 파일 마지막에 새로운 내용을 추가할 때 사용 )
with open(file_path, 'rt', encoding='utf8') as f: #파일을 rt모드, f라는 이름으로 오픈
    read_file = f.read()


def tts(string_file, name):
    tts = gTTS(text=string_file, lang="ko") #s_str의 문자열을 한글로 변환하여 tts변수에
    tts.save(name) 
    playsound(name)

tts(s_str, "nice_to_meet_you.mp3")
tts(read_file, "sorry.mp3")
import googletrans
translator = googletrans.Translator()


languages = googletrans.LANGUAGES

str_1 = "hello nice to meet you  /// 很高兴见到你"
result_1 = translator.translate(str_1, dest= 'ko', src='auto')
print(result_1.text)

str_2 = "안녕하세요 만나서 반갑습니다."
result_2 = translator.translate(str_2, dest= 'ja', src='ko')
print(result_2.text)

r_file_path = 'txt/phrase.txt'
w_file_path = 'txt/result_1.txt'

with open(r_file_path, 'r') as f:
    r_lines = f.readlines()

for lines in r_lines:
    result = translator.translate(lines, dest = 'ko')
    print(result.text)
    with open(w_file_path, 'a', encoding='UTF-8') as f: # mode=a는 마지막 줄에 추가
        f.write(result.text + '\n')


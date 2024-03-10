import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len + 1):
        #password_string을 len길이 만큼 가능한 모든 조합을 생성
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            password = ''.join(attempt) #튜플을 문자열로 변환
            print(password, attempt)
            try:
                zFile.extractall(pwd = password.encode()) #압축해제 암호는 바이트 형식(원래 파이썬 str형식은 유니코드)으로 제공되야 해서 encode()
                print(f"password is {password}", password.encode())
                return 1 
            except:
                pass


password_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
zFile = zipfile.ZipFile('히히.zip')

if (un_zip(password_string, 1, 6, zFile) == 1):
    print("압축을 성공적으로 풀었습니다.")
else:
    print("압축풀기에 실패하였습니다.")
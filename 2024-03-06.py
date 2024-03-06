import random

random_number = random.randint(0, 100) #0~100까지의 값을 랜덤으로 집어넣음

game_count = 1 

while True:
    try: 
        my_number = int(input("0 ~ 100 사이의 수를 입력하세요: ")) #사용자에게 정수값을 입력받음
        if random_number == my_number: #랜덤 값이 사용자가 입력한 값이 맞다면
            print(f"정답입니다! {game_count}회 만에 맞추셨습니다.")
            break #반복문을 빠져나옴
        elif random_number > my_number: #랜덤숫자가 사용자가 입력한 값보다 크다면
            print("업")
        elif random_number < my_number: #랜덤숫자가 사용자가 입력한 값보다 작다면
            print("다운")
        
        game_count +=1
    except: #input에 이상한 값이 들어가 오류가 날 때 예외처리
        print("에러가 발생했습니다. 숫자를 입력하세요.")
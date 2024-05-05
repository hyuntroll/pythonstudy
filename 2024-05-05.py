#5단어
#6번의 기회
#단어가 들어있기만 한다면 노란색, 위치 까지 맞다면 초록색으로 표시

chance = 0
Today_Word = 'apple'
correct = False


for i in range(6):
    chance += 1
    inp = input().lower()
    #print(inp, inp.find('a'))
    for f in range(len(inp)):
        if inp[f] == Today_Word[f]:
            print('\033[32m' + inp[f] + '\033[0m', end='')
        elif Today_Word.find(inp[f]) != -1:
            print('\033[33m' + inp[f] + '\033[0m', end='')
        else:
            print(inp[f] , end='')
    print('')

    if inp == Today_Word:
        correct = True
        break 

if correct == True:
    print("ㅊㅊ")
else:
    print("븅신 ㅋ")
a, b, c = map(int, input().split(' '))
list = [a, b, c]
list.sort(reverse=True) #큰값부터 나열
money = 0
if (a == b== c): #1번 경우
    money = 10000 + a  * 1000
elif (a != b and b != c and c != a): #3번째 경우
    money = list[0] * 100
else: #2번째 경우  큰값부터 나열되기 때문에 둘만 같은 경우 4 2 2, 4 4 2 이런식으로 중앙에 있는 값은 항상 둘 다 같은 눈 성립
    money = 1000 + list[1] * 100

print(money)
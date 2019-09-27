# myNumber.py
# 함수를 직접 만들어 써봅시다.

import random

# 숫자를 골라봅시다.
computer_number=random.randint(0,100)

# is_same() 함수를 만듭니다.
def is_same(target,number):
    if target==number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
        return result
# 게임을 시작합니다.
user_name=input("당신의 이름은 무엇입니까?")
user_nickname=input("게임에서 사용할 닉네임을 입력해 주세요.")
print(user_nickname,"(",user_name,")님,안녕하세요!\n난 0부터 100 중 숫자 하나를 골랐어요.")

# 사용자가 추측한 숫자를 인수로 받아옵니다. 
guess= int(input("뭔지 쓰고 엔터 키를 누르세요."))

# is_same() 함수를 사용합니다.
higher_or_lower=is_same(computer_number,guess)

#사용자가 맞출 때까지 게임을 합니다.
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess=int(input("그것보단 높습니다. 다시 생각해보세요."))
    else:
        guess=int(input("그것보단 낮습니다. 다시 생각해보세요."))

    higher_or_lower=is_same(computer_number,guess)

#게임을 끝냅니다.
print(user_nickname,"(",user_name,")님,잘했어요!")
input("\n\n\n마치려면 Enter 키를 누르세요.")

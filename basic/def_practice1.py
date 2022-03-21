def making_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("입금되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print("출금되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금불가입니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 500
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 5000)
balance = withdraw(balance, 3000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원입니다.".format(commission, balance))

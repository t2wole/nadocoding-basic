gun = 100

def checkpoint(soldiers):
    global gun
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 10)
print("남은 총 : {0}".format(gun))

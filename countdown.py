#sleep: 일정한 시간동안 실행 후 프로그램을 멈추는 함수

import time

# time.sleep(3)
# print("3초가 지남")

# for x in reversed(range(0,10, 2)):  /2를 더 넣으면 이는 간격이됨
#     print(x)


#00:01:10  / 70을 입력하면
# for : sleep(1) /1초마다 반복됨
# seconds =70 % 60
# minutes = (70//60)%60
# print(seconds)
# print(minutes)



my_time = input("초단위 시간을 입력해주세요")

try:
    my_time = int(my_time)
except ValueError:
    print("just numbers")

# for x in reversed(range(0, my_time)):
for x in range(my_time,0,-1):  #10부터
    seconds = x % 60
    minutes = (x//60)%60

    #02d: 2자리 숫자로 표현하되 1자리면 앞에 0이 온다.
    print(f"{minutes:02d}: {seconds:02d}")

    time.sleep(1)
print("time is over")


a, b = input('시간을 설정하세요:').split()

time = int(a)
minute = int(b)
set_minute = minute - 45
if set_minute < 0 :
    set_minute = 60 + set_minute
    set_time = time - 1
    if set_time < 0 :
        set_time = 24 + set_time
else :
    set_time = time

print(set_time, set_minute)

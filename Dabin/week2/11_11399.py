people = int(input())
time_per_person = list(map(int, input().split()))
time_per_person = sorted(time_per_person)
time_accumulate = 0
total_time = 0
for i in time_per_person:
    time_accumulate += i
    total_time += time_accumulate

print(total_time)
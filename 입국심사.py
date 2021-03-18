def solution(n,times):
    answer = 0

    times.sort()

    min = 0
    max = times[-1] * n
    mid = 0

    while min <= max:
        mid = (min + max) // 2
        people = 0

        for time in times:
            people = people + (mid // time)

        if people >= n:
            max = mid -1
        else:
            min = mid + 1

    return min
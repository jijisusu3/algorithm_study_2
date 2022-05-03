def solution(fees, records):
    answer = []
    car_now = []
    car_done = {}
    for i in records:
        time, car, status = i.split()
        hour, minute = map(int, time.split(':'))

        if status == 'IN':
            car_now.append([[hour, minute], car, status])

        else:  # OUT 일 때
            for x in range(len(car_now)):
                car_in = car_now.pop(0)
                if car_in[1] == car:
                    time = (hour - car_in[0][0]) * 60 + minute - car_in[0][1]
                    car_done[int(car)] = time
                else:
                    car_now.append(car_in)
    if car_now:
        for i in car_now:
            time = (23 - i[0][0]) * 60 + 59 - i[0][1]
            if int(i[1]) in car_done:
                car_done[int(i[1])] += time
            else:
                car_done[(i[1])] = time
    result = sorted(car_done.items())

    for key, times in result:
        pay = fees[1]
        left = times - fees[0]
        if left > 0:
            if left % fees[2] == 0:
                pay += int((left/fees[2]) * fees[3])
            else:
                pay += int((left//fees[2] + 1) * (fees[3]))
        answer.append(pay)

    return answer

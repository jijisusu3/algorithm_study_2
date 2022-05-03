fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


def m_time(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def olim(n):
    if n == int(n):
        return int(n)
    else:
        return int(n) + 1

def solution(fees, records):
    answer = []
    
    b_time, b_fee, u_time, u_fee = fees
    
    car = {}
    fee_all = []
    for i in records:
        time, num, io = i.split()
        if io == 'IN':
            a = m_time(time)
            car[num] = a
        elif io == 'OUT':
            b = m_time(time)
            t = b - car[num]
            fee_all.append([num, t])
            del car[num]
    
    b = m_time('23:59')
    for num in car.keys():
        t = b - car[num]
        fee_all.append([num, t])
    fee_all.sort()
    check = []
    t_parking = []
    for i in range(len(fee_all)):
        if fee_all[i][0] not in check:
            check.append(fee_all[i][0])
            t_parking.append(fee_all[i][1])
        else:
            t_parking[-1] += fee_all[i][1]
    
    for i in t_parking:
        if i > b_time:
            k = olim(((i - b_time) / u_time))
            ans = b_fee + k * u_fee
            answer.append(ans)
        else:
            answer.append(b_fee)
    
    return answer

print(solution(fees, records))
#records를 split하고 차량 번호를 key로 시간을 value로 하는 dict로 저장 
#dict value를 for문으로 돌리면서 시간 계산 
from collections import defaultdict
from datetime import datetime
import math
def solution(fees, records):
    d = defaultdict(list)
    answer = []
    for rec in records:
        rec = rec.split(" ")
        d[rec[1]].append(rec[0])
    
    #주차시간 계산 
    #dict for문 짝수로 돌리기 
    #만약 i가 마지막 번호(value가 홀수 번)이면 23:59으로 빼기 
    #time이 기본 시간 이상이면 계산하고 이하면 기본 요금 출력 
    #차량 번호 오름차순 
    for k in sorted(d.keys()):
        print(d[k])
        time =0
        for i in range(0,len(d[k]),2):
            if i+1< len(d[k]):
                in_time = datetime.strptime(d[k][i], "%H:%M")
                out_time = datetime.strptime(d[k][i+1], '%H:%M')
                time_gap = out_time - in_time
                time += (time_gap.seconds)/60
                # print(time)
            else: 
                in_time = datetime.strptime(d[k][i], '%H:%M')
                out_time = datetime.strptime("23:59",'%H:%M')
                time_gap = out_time - in_time
                time += (time_gap.seconds)/60
                # print(in_time)
        print(time)    
        if time <= fees[0]:
            answer.append(fees[1])
        else: 
            time = time-fees[0]
            time_fee = math.ceil(time/fees[2])*fees[3]
            cost = fees[1] + time_fee
            answer.append(cost)
            
    
    return answer

# datetime 모듈 사용하는 방법 
'''
datetime.strptime("23:44",'%H,%M')
timedelta는 days랑 seconds 제공 
'''

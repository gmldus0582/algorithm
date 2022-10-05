#find_minintensity 함수=> gate들을 heap에 넣고 visited 리스트로 체크하면서 
#graph 돌아다님 그리고 마지막에 visited[summit] 최소 값 구하기 
#path를 출발 노드를 index로 하고 도착 노드와 시간을 값으로 가지는 graph로 변경
from heapq import heappush, heappop
from collections import defaultdict
def find_minintensity(n,gates,graph,summits,set_summits):
    #node와 intensity 저장
    pq =[]
    visited=[10000001]*(n+1)
    answer = [0,10000001]
    for gate in gates:
        heappush(pq,(gate,0))
        visited[gate] =0
    while pq:
        node,intensity = heappop(pq)
        #node가 산봉우리인 경우, visited[node]가 intensity 작으면 pass 그리고 gate인 경우도 pass 
        if node in set_summits or visited[node] < intensity :
            continue
        #graph 돌아가면서 다음 노드의 intensity 값을 visited에 넣어주기 
        for next_node, cost in graph[node]:
            new_intensity = max(cost,intensity)
            if new_intensity < visited[next_node]: 
                visited[next_node] =  new_intensity
                heappush(pq,(next_node, new_intensity))
    # summit 최소 값 구해야해서 summits 리스트로 찾기 
    for summit in summits: 
        if answer[1] > visited[summit]:
            answer[0]= summit
            answer[1] = visited[summit]
    
    return answer
            
def solution(n, paths, gates, summits):
    
    graph =defaultdict(list)
    for i,k,cost in paths:
        graph[i].append([k,cost])
        graph[k].append([i,cost])
    summits.sort()
    #set은 O(1) list는 O(n)이라서 set이 더 빠르다
    set_summits = set(summits)
      
    return find_minintensity(n,gates,graph,summits,set_summits)
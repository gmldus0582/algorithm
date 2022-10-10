from heapq import heappop, heappush
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
graph=[]
num=1
INF=int(1e9)

def dijkstra(num,graph,x,y):
    distance =[[INF]*(num) for i in range(num)]
    q= []
    heappush(q,(x,y,0))
    distance[0][0] = 0
    dx =[1,-1,0,0]
    dy = [0,0,1,-1]
    

    while q:
        x,y,cost = heappop(q)
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0 >nx or nx >=num or ny<0 or ny >= num:
                continue
            cost = distance[x][y]+ graph[nx][ny]
            if cost <distance[nx][ny]:
                distance[nx][ny] =cost
                heappush(q,(nx,ny,cost))
    return distance[num-1][num-1]

for test_case in range(1, T + 1):
    num= int(input())
    graph =[]
    # distance =[[INF]*(test_case) for i in range(test_case)] 
    for _ in range(num):
        str = list(input())
        num_str = list(map(int,str))
        graph.append(num_str)
    # dijkstra(test_case,graph,0,0)
    print("#",test_case,"",dijkstra(num,graph,0,0))



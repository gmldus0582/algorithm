#bfs로 해야겠다!
#필드를 정함 근데 필드가 인접해서 잘못된 길을 찾을 수 있음으로 2배로 크기 키우기 
#rectangle 안에 좌표에서 좌표 안쪽이면 0을 주고 좌표값 즉 테두리면 1을 준다 
#방문하지 않고 테두리인 경우만 visited에 체크 => 경로 값 넣기 
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    #필드를 만들기
    field =[[-1]*102 for i in range(102)]
    
    #필드 안에서 직사각형 그리기 => 내부와 테두리 구분 
    for r in rectangle: 
        x1,y1,x2,y2 = map(lambda x: x*2,r)
        
        for i in range(x1,x2+1):
            for j in range(y1, y2+1):
                if x1<i<x2 and y1<j<y2:
                    field[i][j] = 0
                elif field[i][j] !=0:
                    field[i][j] =1
    #방향 
    dx =[1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append([characterX*2, characterY*2])
    visited =[[1]*102 for i in range(102)]
    
    while queue:
        x,y =  queue.popleft()
        if x== itemX*2 and y==itemY*2:
            answer = visited[x][y]//2
            break
        #방향 정하기
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            #테두리에 있는지 확인 그리고 방문 확인 
            if field[nx][ny] ==1 and visited[nx][ny] ==1:
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1
            
    return answer
    
#https://school.programmers.co.kr/learn/courses/30/lessons/87694
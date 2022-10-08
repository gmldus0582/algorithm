#dfs => 한 컴퓨터에서 최대한 갈 수 있는 컴퓨터 체크 
#dfs를 컴퓨터 수만큼 for문 돌리고 이때 visited가 0 경우에는 dfs로 찾기
def dfs(n,computers,visited,num):
    visited[num] = 1
    for i in range(n):
        if num!= i and computers[num][i] ==1:
            if visited[i] == 0:
                dfs(n,computers,visited,i)
            
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for num in range(n):
        if visited[num] == 0:
            dfs(n,computers,visited,num)
            answer+=1
            
    return answer

    #https://school.programmers.co.kr/learn/courses/30/lessons/43162
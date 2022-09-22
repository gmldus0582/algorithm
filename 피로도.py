#dfs를 이용하여 완전탐색 
answer =0
visited =[]
def dfs(k, cnt, dungeons):
    #answer을 최고 값으로 
    global answer
    if answer < cnt:
        answer = cnt
    for i in range(len(dungeons)):
        if k>= dungeons[i][0] and not visited[i]:
            visited[i]=1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] =0
    
def solution(k, dungeons):
    global visited 
    visited= len(dungeons)*[0]
    dfs(k,0,dungeons)
    return answer
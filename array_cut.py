#n*n list 만들기 => left와 right만큼 자름
#list index를 q= l/n, d =l%n 인 q와 d의 max+1한 값을 넣기 
def solution(n, left, right):
    answer = []
    # index_list =[0]*(n*n)
    
    for i in range(left,(right+1)):
        q = int(i/n)
        d = i%n
        num = max(q,d)+1
        answer.append(num)
    
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/87390
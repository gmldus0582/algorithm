#SWEA 3752 가능한 시험 점수 d4
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tsize = int(input())
    scoreList = list(map(int,(input().split(" "))))
    #방문처리와 score간의 sum 값을 저장한다.
    visited=[1]+[0]*sum(scoreList)
    sum_score=[0]
    for score in scoreList:
        #각 원소들은 sum_score의 원소들과 덧셈을 하고 이 값이 방문 되었는지 확인한다.
        for i in range(len(sum_score)):
            #방문되지 않은 값들은 방문 처리를 해주고 더한 값은 sum_score에 저장한다. 
            if visited[sum_score[i]+score]==0:
                visited[sum_score[i]+score]=1
                sum_score.append(sum_score[i]+score)

    print(f'#{test_case} {len(sum_score)}')

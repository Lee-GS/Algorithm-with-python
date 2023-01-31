import sys
from collections import deque

N,M = map(int,input().split())

graph = [] #그래프 선언
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip()))) #그래프 입력 받기
    
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[N-1][M-1]

print(bfs(0,0))

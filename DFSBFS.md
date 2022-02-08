# DFS/BFS

1. 스택(stack)

- 선입후출(First In Last Out) 구조
- 후입선출(Last In First Out) 구조

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# [5, 2, 3, 1]
# [1, 3, 2, 5]
```

- 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.

2. 큐(queue)

- 선입선출(First In First Out) 구조

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
print(list(queue)) # 리스트 자료형으로 변경

# deque([3, 7, 1, 4])
# deque([4, 1, 7, 3])
```

- 파이선으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용
- deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 간단하다.

3. 재귀 함수

- 자기 자신을 다시 호출하는 함수

```python
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()
```

- 재귀함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다.

```python
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i==100:
        return
    print(i,'번째 재귀 함수에서',i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료합니다.')


recursive_function(1)
```

4. DFS

- DFS는 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

- 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

- 인접 리스트 : 리스트로 그래프의 연결관계를 표현하는 방식

  1. 인접 행렬 방식

  ```python
  INF = 999999999 # 무한의 비용 선언
  
  # 2차원 리스트를 이용해 인접 행렬 표현
  graph = [[0,7,5],
           [7,0,INF],
           [5,INF,0]]
  
  print(graph)
  ```

  2. 인접 리스트 방식

  ```python
  # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]
  
  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1,7))
  graph[0].append((2,5))
  
  # 노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0,7))
  
  # 노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0,5))
  
  print(graph)
  ```

  - 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비 
  - 인접 리스트 방식은 연결된 정보만 사용하기 때문에 메모리를 효율적으로 사용, 정보를 얻는 속도가 느림

  

- DFS는 스택 자료구조를 이용하며 구체적인 동작 과정은 다음과 같다.

  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.

  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 

     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

- O(N) 의 시간 복잡도

- 스택을 이용하는 알고리즘이기 때문에 실제 구현은 재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있다.

```python
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2,3,8], [1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph,1,visited)
```



5. BFS

- BFS 알고리즘은 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석
- 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어 가까운 노드부터 탐색을 진행하게 된다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.

```python
from collections import deque

def bfs(graph,start,visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2,3,8], [1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
bfs(graph,1,visited)
```

|           | DFS            | BFS              |
| --------- | -------------- | ---------------- |
| 동작 원리 | 스택           | 큐               |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |



## 실전 문제

1. 음료수 얼려 먹기


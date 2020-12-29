# 파이썬으로 구현하는 알고리즘

<br>

## 목록

+ [탐색 알고리즘 ( Search Algorithms )](#탐색-알고리즘--searching-algorithms-)
  + [선형 탐색법 ( Linear Search )](#선형-탐색법--linear-search-)
  + [이진 탐색법 ( Binary Search )](#이진-탐색법--binary-search-)
  
+ [정렬 알고리즘 ( Sorting Algorithms )](#정렬-알고리즘--sorting-algorithms-)
  + [버블 정렬 ( Bubble Sort )](#버블-정렬--bubble-sort-)
  + [병합 정렬 ( Merge Sort )](#병합-정렬--merge-sort-)
  + [삽입 정렬 ( Insertion Sort )](#삽입-정렬--insertion-sort-)
  + [셸 정렬 ( Shell's Sort )](#셸-정렬--shell's-sort-)
  + [선택 정렬 (Selection Sort )](#선택-정렬--selection-sort-)
  
+ [그래프 알고리즘 ( Graph Algorithms )](#그래프-알고리즘--graph-algorithms-)
  + [깊이 우선 탐색 ( Depth First Search )](#깊이-우선-탐색--depth-first-search-)
  + [너비 우선 탐색 ( Breadth First Search )](#s너비-우선-탐색--breadth-first-search-)

+ [탐욕 알고리즘 ( Greedy Algorithms )](#탐욕-알고리즘--greedy-algorithms-)
  + 기본 알고리즘
    + [허프만 코드 ( Huffman code )](#허프만-코드--huffman-code-)
  + 그래프 관련 알고리즘
    + [다익스트라 알고리즘 ( Dijkstra’s Algorithm )](#다익스트라-알고리즘--dijkstra’s-algorithm-)
    + [크루스칼 알고리즘 ( Kruskal’s algorithm )](#크루스칼-알고리즘--kruskal’s-algorithm-)
    + [프림 알고리즘 ( Prim’s algorithm )](#프림-알고리즘--prim’s-algorithm-)

+ [동적 프로그래밍 ( Dynamic Programming )](#동적-프로그래밍--dynamic-programming-)

<br>

------------------

<br>

## 탐색 알고리즘 ( Searching Algorithms )

+ ### 개요
  + 방대한 데이터에서 목적에 맞는 데이터를 찾아내기 위한 알고리즘
  + 종류
    + Linear Search
    + Binary Search
    + Jump Search
    + Interpolation Search
    + Exponential Search
    + Sublist Search (Search a linked list in another list)
    + Fibonacci Search
    + The Ubiquitous Binary Search
    + Recursive program to linearly search an element in a given array
    + Recursive function to do substring search
    + Unbounded Binary Search Example (Find the point where a monotonically increasing function becomes positive first time)
    
+ ## 선형 탐색법 ( Linear Search )
  + ### 개요
    + 차례로 하나씩 비교하여 원하는 데이터를 찾아냄 
    + 단순하고 구현이 쉬움
    + 비효율적임
    
  + ### 구현
    <pre><code>
    # Python3 code to linearly search x in arr[]. 
    # If x is present then return its location, 
    # otherwise return -1 


    def search(arr, n, x): 

        for i in range(0, n): 
            if (arr[i] == x): 
                return i 
        return -1


    # Driver Code 
    arr = [2, 3, 4, 10, 40] 
    x = 10
    n = len(arr) 

    # Function call 
    result = search(arr, n, x) 
    if(result == -1): 
        print("Element is not present in array") 
    else: 
        print("Element is present at index", result) 
        
    # 출처 : https://www.geeksforgeeks.org/linear-search/ 
    </code></pre>
    
+ ## 이진 탐색법 ( Binary Search ) 
  + ### 개요
    + 반복적으로 범위를 반으로 검색 후 원하는 데이터를 찾아냄
    + 사전에 정렬이 되어 있어야 함
    
  + ### 이진트리의 재귀적 구현
    <pre><code>
    # Python3 Program for recursive binary search. 

    # Returns index of x in arr if present, else -1 
    def binarySearch (arr, l, r, x): 

        # Check base case 
        if r >= l: 

            mid = l + (r - l) // 2

            # If element is present at the middle itself 
            if arr[mid] == x: 
                return mid 

            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            elif arr[mid] > x: 
                return binarySearch(arr, l, mid-1, x) 

            # Else the element can only be present  
            # in right subarray 
            else: 
                return binarySearch(arr, mid + 1, r, x) 

        else: 
            # Element is not present in the array 
            return -1

    # Driver Code 
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10

    # Function call 
    result = binarySearch(arr, 0, len(arr)-1, x) 

    if result != -1: 
        print ("Element is present at index % d" % result) 
    else: 
        print ("Element is not present in array") 

    # 출처 : https://www.geeksforgeeks.org/binary-search/ 
    </code></pre>
  
  + ### 이진트리의 반복적 구현
    <pre><code>
    # Python3 code to implement iterative Binary  
    # Search. 

    # It returns location of x in given array arr  
    # if present, else returns -1 
    def binarySearch(arr, l, r, x): 

        while l <= r: 

            mid = l + (r - l) // 2; 

            # Check if x is present at mid 
            if arr[mid] == x: 
                return mid 

            # If x is greater, ignore left half 
            elif arr[mid] < x: 
                l = mid + 1

            # If x is smaller, ignore right half 
            else: 
                r = mid - 1

        # If we reach here, then the element 
        # was not present 
        return -1

    # Driver Code 
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10

    # Function call 
    result = binarySearch(arr, 0, len(arr)-1, x) 

    if result != -1: 
        print ("Element is present at index % d" % result) 
    else: 
        print ("Element is not present in array") 

    # 참고 : https://www.geeksforgeeks.org/binary-search/ 
    </code></pre>
  
  
> ###### 참고 : https://blog.hexabrain.net/245 , https://www.geeksforgeeks.org/searching-algorithms/ , https://yeolco.tistory.com/74 

<br>

------------

<br>

## 정렬 알고리즘 ( Sorting Algorithms )

+ ### 개요
  + 원소들을 번호순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘
  + 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 알고리즘
  + 얼마나 효과적으로 해결할 수 있느냐가 정렬 문제의 핵심
  
  + 종류
    + O(n²)
      + [버블 정렬( Bubble Sort )](#버블-정렬--bubble-sort-)
      + [선택 정렬( Selection sort )](#선택-정렬--selection-sort-)
      + [삽입 정렬( Insertion sort )](#삽입-정렬--insertion-sort-)
      
    + O( n log n )
      + [병합 정렬( Merge sort )](#병합-정렬--merge-sort-)
      + 힙 정렬( Heap sort )
      + 퀵 정렬( Quick sort )
      + 하이브리드 정렬
      + 팀 정렬( Tim sort )
      + 인트로 정렬( Intro sort )
      
    + etc
      + 기수 정렬( Radix sort )
      + 카운팅 정렬( Counting sort )
      + [셸 정렬( Shell's sort )](#셸-정렬--shell's-sort-)
      + 보고 정렬( Bogo sort, stupid sort )
      + 보고보고 정렬( Bogobogo sort )
      + 대기 정렬( Sleep sort )
      
  + ### 버블 정렬 ( Bubble Sort )
    + 개요
      + 인접한 두개의 요소를 비교, 순서가 맞지 않으면 요소를 교환함     
        ( 비교 알고리즘 기반 )
      + 반복문이 한번 실행될 때마다 마지막 하나의 원소가 정렬    
        -> 거품이 올라오는 것처럼 보여 버블 정렬이라 불림
        
    + 구현
      <pre><code>
      def bubblesort(list):

      # Swap the elements to arrange in order
          for iter_num in range(len(list)-1,0,-1):
              for idx in range(iter_num):
                  if list[idx]>list[idx+1]:
                      temp = list[idx]
                      list[idx] = list[idx+1]
                      list[idx+1] = temp

      list = [19,2,31,45,6,11,121,27]
      bubblesort(list)
      print(list)
      
      # 출처 : https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
      </code></pre>
      
  + ### 병합 정렬 ( Merge Sort )
    + 개요
      + 원소 개수가 1 또는 0이 될 때까지 두 부분으로 나눔   
        -> 나눈 순서의 역순으로 크기를 비교 및 병합   
        ( 분할-정복 알고리즘 기반 ) 
        
    + 구현
      <pre><code>
      def merge_sort(unsorted_list):
          if len(unsorted_list) <= 1:
              return unsorted_list
      # Find the middle point and devide it
          middle = len(unsorted_list) // 2
          left_list = unsorted_list[:middle]
          right_list = unsorted_list[middle:]

          left_list = merge_sort(left_list)
          right_list = merge_sort(right_list)
          return list(merge(left_list, right_list))

      # Merge the sorted halves

      def merge(left_half,right_half):

          res = []
          while len(left_half) != 0 and len(right_half) != 0:
              if left_half[0] < right_half[0]:
                  res.append(left_half[0])
                  left_half.remove(left_half[0])
              else:
                  res.append(right_half[0])
                  right_half.remove(right_half[0])
          if len(left_half) == 0:
              res = res + right_half
          else:
              res = res + left_half
          return res

      unsorted_list = [64, 34, 25, 12, 22, 11, 90]

      print(merge_sort(unsorted_list))
      
      # 출처 : https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
      </code></pre> 
  
  + ### 삽입 정렬 ( Insertion Sort )
    + 개요
      + 아직 정렬되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복
      + 평균적으로 삽입정렬이 선택정렬과 버블정렬에 비해 빠름 
      
    + 구현
      <pre><code>
      def insertion_sort(InputList):
          for i in range(1, len(InputList)):
              j = i-1
              nxt_element = InputList[i]
      # Compare the current element with next one

              while (InputList[j] > nxt_element) and (j >= 0):
                  InputList[j+1] = InputList[j]
                  j=j-1
              InputList[j+1] = nxt_element

      list = [19,2,31,45,30,11,121,27]
      insertion_sort(list)
      print(list)
      
      # 출처 : https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm 
      </code></pre>
  
  + ### 셸 정렬 ( Shell Sort )
    + 개요
      + 정렬 과정 
        + 먼저 정렬해야 할 리스트를 일정한 기준에 따라 분류
        + 연속적이지 않은 여러 개의 부분 리스트를 생성
        + 각 부분 리스트를 삽입 정렬을 이용하여 정렬
        + 모든 부분 리스트가 정렬되면 다시 전체 리스트를 더 적은 개수의 부분 리스트로 만든 후에 알고리즘을 반복
        + 위의 과정을 부분 리스트의 개수가 1이 될 때까지 반복
      + 삽입 정렬을 보완한 알고리즘
      + 시간 복잡도가 명확하지 않음
      
    + 구현
      <pre><code>
      def shellSort(input_list):
    
          gap = len(input_list) // 2
          while gap > 0:

              for i in range(gap, len(input_list)):
                  temp = input_list[i]
                  j = i
      # Sort the sub list for this gap

                  while j >= gap and input_list[j - gap] > temp:
                      input_list[j] = input_list[j - gap]
                      j = j-gap
                  input_list[j] = temp

      # Reduce the gap for the next element

              gap = gap//2

      list = [19,2,31,45,30,11,121,27]

      shellSort(list)
      print(list)
      
      # 출처 : https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm 
      </code></pre>
    
  
  + ### 선택 정렬 ( Selection Sort )
    + 개요
      + 주어진 배열에서 최댓값(최솟값)을 찾아 맨 오른쪽(왼쪽)값과 교체 - 반복
      + 대체로 버블정렬보다 빠름
      
    + 구현
      <pre><code>
      def selection_sort(input_list):

        for idx in range(len(input_list)):

            min_idx = idx
            for j in range( idx +1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
      # Swap the minimum value with the compared value

            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


      l = [19,2,31,45,30,11,121,27]
      selection_sort(l)
      print(l)
      
      # 출처 : https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm 
      </code></pre>
    

> ###### 참고 : https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 , https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm , http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html , https://gmlwjd9405.github.io/2018/05/08/algorithm-shell-sort.html 

<br>

------------

<br>

## 그래프 알고리즘 ( Graph Algorithms )

+ ### 개요
  + 개요
    + 구성 : 정점(Vertex) + 변(Edge)
    + 유향 그래프 : 한쪽 방향으로만 이동 가능
    + 무향 그래프 : 양쪽 방향 이동 가능
    + 사용 예 ) 도시-도로 통신망, 컴퓨터 통신망, SNS에서의 친구 관계 등

  + ### 깊이 우선 탐색 ( Depth First Search )
    + 개요
      + 한 방향으로 최대한 깊숙히 들어가서 확인 후 다시 돌아가 다른 방향을 탐색
      + 사용 예 ) traverse, backtracking 등 
      + 먼저 방문한 노드에 연결된 노드보다, 현재 방문한 노드에 연결된 노드를 방문해야 함    
        -> 자료구조 스택 사용 
        
      + <div><img src="https://user-images.githubusercontent.com/52907116/103291818-ede41c00-4a2f-11eb-8bb5-bef77a0f3fc8.gif" width = "25%"></img></div>
    
      > ( WIKIPEDIA, DFS )
      
    + 구현
      <pre><code>
        class graph:
            def __init__(self,gdict=None):
                if gdict is None:
                    gdict = {}
                self.gdict = gdict
                
        # Check for the visisted and unvisited nodes
        def dfs(graph, start, visited = None):
            if visited is None:
                visited = set()
                
            visited.add(start)
            print(start)
            
            for next in graph[start] - visited:
                dfs(graph, next, visited)
                
            return visited

        gdict = { "a" : set(["b","c"]),
                        "b" : set(["a", "d"]),
                        "c" : set(["a", "d"]),
                        "d" : set(["e"]),
                        "e" : set(["a"])
                        }


        dfs(gdict, 'a')
        
        # 출처 : https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm 
      </code></pre>
    
  + ### 너비 우선 탐색 ( Breadth First Search )
    + 개요
      + 갈림길에 연결되어 있는 모든 길을 한번씩 탐색 후 그 다음에 연결되어 있는 길들을 넓게 탐색 
      + 현재 방문한 노드에 연결된 노드보다, 먼저 방문한 노드에 연결된 노드를 방문해야 함    
        -> 자료구조 큐 사용 
        
      <div><img src="https://user-images.githubusercontent.com/52907116/103291819-ee7cb280-4a2f-11eb-93ce-50257a49417d.gif" width = "25%"></img></div>   
      
      > ( WIKIPEDIA, BFS )
      
    
    + 구현
      <pre><code>
        import collections
        class graph:
            def __init__(self,gdict=None):
                if gdict is None:
                    gdict = {}
                self.gdict = gdict

        def bfs(graph, startnode):
        # Track the visited and unvisited nodes using queue
                seen, queue = set([startnode]), collections.deque([startnode])
                while queue:
                    vertex = queue.popleft()
                    marked(vertex)
                    
                    for node in graph[vertex]:
                        if node not in seen:
                            seen.add(node)
                            queue.append(node)

        def marked(n):
            print(n)

        # The graph dictionary
        gdict = { "a" : set(["b","c"]),
                        "b" : set(["a", "d"]),
                        "c" : set(["a", "d"]),
                        "d" : set(["e"]),
                        "e" : set(["a"])
                        }

        bfs(gdict, "a")
        
        # 출처  : https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm 
        
      </code></pre>

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm , https://namu.wiki/w/%EA%B7%B8%EB%9E%98%ED%94%84(%EC%9D%B4%EC%82%B0%EC%88%98%ED%95%99) , https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html 

<br>

------------

<br>

## 탐욕 알고리즘 ( Greedy Algorithms )

+ ### 개요
  + 목표 : 미래를 알지 못하는 상황에서 주어진 순간에 최적의 선택을 함   
    ( 매 순간 최적이라고 생각되는 경우를 선택 ) 
  + 최적의 해에 가까운 값을 구하기 위해 사용 
  + 최적의 해를 구해준다는 보장을 하지 못함 
  + 분할과 정복, 동적 프로그래밍보다 빠름  
  
  + ### 허프만 코드 ( Huffman code )
    + 개요
    
    + 구현
     <pre><code>
     #코드 테스트
     </code></pre>
     
  + ### 다익스트라 알고리즘 ( Dijkstra’s Algorithm )
    + 개요 
    
    + 구현
      <pre><code>
      #코드 테스트
      </code></pre>
      
  + ### 크루스칼 알고리즘 ( Kruskal’s algorithm )
    + 개요
    
    + 구현
      <pre><code>
      #코드 테스트
      </code></pre>
      
  + ### 프림 알고리즘 ( Prim’s algorithm ) 
    + 개요
    
    + 구현
      <pre><code>
      #코드 테스트
      </code></pre>
  

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : https://www.fun-coding.org/Chapter19-greedy-live.html , https://skerritt.blog/greedy-algorithms/ ,https://janghw.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Greedy-Algorithm-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 , https://www.geeksforgeeks.org/greedy-algorithms/#standardGreedyAlgorithms 

<br>

------------

<br>

## 동적 프로그래밍 ( Dynamic Programming )

+ ### 1. 개요
  + 

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : 

<br>

------------

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

+ [동적 계획법 ( Dynamic Programming )](#동적-계획법--dynamic-programming-)

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
      + 고정 길이 코드 ( Fixed Length Code ) : 모든 코드의 길이가 똑같은 코드의 체계 
      + 가변 길이 코드 ( Variavle Length Code )  
        + 접두어 코드 ( Prefix Code ) : 코드 집합의 어느 한 코드도 다른 코드의 접두어가 되지 않는 코드   
      + 데이터를 압축하는 방법중의 하나로 쓰이는 알고리즘    
        -> ASCII와 같은 고정 길이 코드로 이루어진 데이터를 접두어 코드로 변환, 압축시키는 메커니즘
      
    + 구현
     <pre><code>
      import heapq
      import os

      class HeapNode:
        def __init__(self, char, freq):
          self.char = char
          self.freq = freq
          self.left = None
          self.right = None

        def __cmp__(self, other):
          if(other == None):
            return -1
          if(not isinstance(other, HeapNode)):
            return -1
          return self.freq > other.freq


      class HuffmanCoding:
        def __init__(self, path):
          self.path = path
          self.heap = []
          self.codes = {}
          self.reverse_mapping = {}

        # functions for compression:

        def make_frequency_dict(self, text):
          frequency = {}
          for character in text:
            if not character in frequency:
              frequency[character] = 0
            frequency[character] += 1
          return frequency

        def make_heap(self, frequency):
          for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

        def merge_nodes(self):
          while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)


        def make_codes_helper(self, root, current_code):
          if(root == None):
            return

          if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

          self.make_codes_helper(root.left, current_code + "0")
          self.make_codes_helper(root.right, current_code + "1")


        def make_codes(self):
          root = heapq.heappop(self.heap)
          current_code = ""
          self.make_codes_helper(root, current_code)


        def get_encoded_text(self, text):
          encoded_text = ""
          for character in text:
            encoded_text += self.codes[character]
          return encoded_text


        def pad_encoded_text(self, encoded_text):
          extra_padding = 8 - len(encoded_text) % 8
          for i in range(extra_padding):
            encoded_text += "0"

          padded_info = "{0:08b}".format(extra_padding)
          encoded_text = padded_info + encoded_text
          return encoded_text


        def get_byte_array(self, padded_encoded_text):
          if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

          b = bytearray()
          for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
          return b


        def compress(self):
          filename, file_extension = os.path.splitext(self.path)
          output_path = filename + ".bin"

          with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

          print("Compressed")
          return output_path


        """ functions for decompression: """

        def remove_padding(self, padded_encoded_text):
          padded_info = padded_encoded_text[:8]
          extra_padding = int(padded_info, 2)

          padded_encoded_text = padded_encoded_text[8:] 
          encoded_text = padded_encoded_text[:-1*extra_padding]

          return encoded_text

        def decode_text(self, encoded_text):
          current_code = ""
          decoded_text = ""

          for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
              character = self.reverse_mapping[current_code]
              decoded_text += character
              current_code = ""

          return decoded_text


        def decompress(self, input_path):
          filename, file_extension = os.path.splitext(self.path)
          output_path = filename + "_decompressed" + ".txt"

          with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while(byte != ""):
              byte = ord(byte)
              bits = bin(byte)[2:].rjust(8, '0')
              bit_string += bits
              byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output.write(decompressed_text)

          print("Decompressed")
          return output_path
          
     # 출처 : https://bhrigu.me/post/huffman-coding-python-implementation/ 
     </code></pre>
     
  + ### 다익스트라 알고리즘 ( Dijkstra’s Algorithm )
    + 개요 
      + 그래프의 한 정점에서 모든 정점까지의 최단거리를 구하는 알고리즘   
        ( 최단 경로 문제 ) 
      + PRIM 알고리즘과 유사함 
      + 활용 예 ) 내비게이션, 미로탐색 알고리즘 등 
      + 알고리즘 로직        
        1) 최단 경로 트리에 포함된 정점을 추적하는 settSet(최단 경로 트리 세트)를 생성   
          ( 소스와의 최소 거리가 계산되고 종료, 처음에는 이 집합이 비어 있음 )    
        2) 입력 그래프의 모든 정점에 거리 모든 거리 값을 무한대로 초기화    
          ( 소스 정점은 먼저 선택되도록 거리 값을 0으로 할당 ) 
        3) sptSet이 모든 정점을 포함하지 않을동안 반복  
          3-1) sptSet에 없고 최소 거리 값이 있는 꼭지점 u를 선택   
          3-2) sptSet를 포함   
          3-3) u의 모든 인접 정점의 거리 값을 업데이트    
        인접한 모든 꼭지점 v에 대해, u(소스로부터)의 거리 값과 edge u-v의 무게의 합이 v의 거리 값보다 작으면, v의 거리 값을 업데이트 
      
    
    + 구현
      <pre><code>
        # Python program for Dijkstra's single  
        # source shortest path algorithm. The program is  
        # for adjacency matrix representation of the graph 

        # Library for INT_MAX 
        import sys 

        class Graph(): 

            def __init__(self, vertices): 
                self.V = vertices 
                self.graph = [[0 for column in range(vertices)]  
                            for row in range(vertices)] 

            def printSolution(self, dist): 
                print "Vertex \tDistance from Source"
                for node in range(self.V): 
                    print node, "\t", dist[node] 

            # A utility function to find the vertex with  
            # minimum distance value, from the set of vertices  
            # not yet included in shortest path tree 
            def minDistance(self, dist, sptSet): 

                # Initilaize minimum distance for next node 
                min = sys.maxint 

                # Search not nearest vertex not in the  
                # shortest path tree 
                for v in range(self.V): 
                    if dist[v] < min and sptSet[v] == False: 
                        min = dist[v] 
                        min_index = v 

                return min_index 

            # Funtion that implements Dijkstra's single source  
            # shortest path algorithm for a graph represented  
            # using adjacency matrix representation 
            def dijkstra(self, src): 

                dist = [sys.maxint] * self.V 
                dist[src] = 0
                sptSet = [False] * self.V 

                for cout in range(self.V): 

                    # Pick the minimum distance vertex from  
                    # the set of vertices not yet processed.  
                    # u is always equal to src in first iteration 
                    u = self.minDistance(dist, sptSet) 

                    # Put the minimum distance vertex in the  
                    # shotest path tree 
                    sptSet[u] = True

                    # Update dist value of the adjacent vertices  
                    # of the picked vertex only if the current  
                    # distance is greater than new distance and 
                    # the vertex in not in the shotest path tree 
                    for v in range(self.V): 
                        if self.graph[u][v] > 0 and sptSet[v] == False and \ 
                        dist[v] > dist[u] + self.graph[u][v]: 
                                dist[v] = dist[u] + self.graph[u][v] 

                self.printSolution(dist) 

        # Driver program 
        g = Graph(9) 
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
                [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                [0, 0, 4, 14, 10, 0, 2, 0, 0], 
                [0, 0, 0, 0, 0, 2, 0, 1, 6], 
                [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                [0, 0, 2, 0, 0, 0, 6, 7, 0] 
                ]; 

        g.dijkstra(0); 

        # This code is contributed by Divyanshu Mehta 
        # 출처 : https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ 
      </code></pre>
      
  + ### 크루스칼 알고리즘 ( Kruskal’s algorithm )
    + 개요
      + 최소 비용 신장 트리를 찾는 알고리즘    
      + 최소 비용 신장 트리 ( Minimun Spanning Tree )     
        -> 각 단계에서 사이클을 이루지 않는 최소 비용 간선 선택   
        ( 최소 비용의 간선으로 구성, 사이클을 포함하지 않음 )  
      + 간선 선택을 기반으로 하는 알고리즘   
      + 그래프 내에 적은 숫자의 간선만을 가지는 ‘희소 그래프(Sparse Graph)’의 경우 쓰기 적합
      + 알고리즘 로직    
        1. 모든 엣지를 가중치의 오름차순으로 정렬   
        2. 가장 작은 엣지를 골라서 지금까지 형성된 신장 트리로 사이클을 형성하는지 확인    
          b-1. if 사이클이 형성되지 않은 경우      
            해당 엣지를 포함   
          b-2. 해당 엣지 삭제    
        3. N-1개의 간선이 생성될때까지 2단계 반복      
      
    + 구현
      <pre><code>
        # Python program for Kruskal's algorithm to find
        # Minimum Spanning Tree of a given connected,
        # undirected and weighted graph

        from collections import defaultdict

        # Class to represent a graph


        class Graph:

            def __init__(self, vertices):
                self.V = vertices  # No. of vertices
                self.graph = []  # default dictionary
                # to store graph

            # function to add an edge to graph
            def addEdge(self, u, v, w):
                self.graph.append([u, v, w])

            # A utility function to find set of an element i
            # (uses path compression technique)
            def find(self, parent, i):
                if parent[i] == i:
                    return i
                return self.find(parent, parent[i])

            # A function that does union of two sets of x and y
            # (uses union by rank)
            def union(self, parent, rank, x, y):
                xroot = self.find(parent, x)
                yroot = self.find(parent, y)

                # Attach smaller rank tree under root of
                # high rank tree (Union by Rank)
                if rank[xroot] < rank[yroot]:
                    parent[xroot] = yroot
                elif rank[xroot] > rank[yroot]:
                    parent[yroot] = xroot

                # If ranks are same, then make one as root
                # and increment its rank by one
                else:
                    parent[yroot] = xroot
                    rank[xroot] += 1

            # The main function to construct MST using Kruskal's
                # algorithm
            def KruskalMST(self):

                result = []  # This will store the resultant MST

                # An index variable, used for sorted edges
                i = 0

                # An index variable, used for result[]
                e = 0

                # Step 1:  Sort all the edges in 
                # non-decreasing order of their
                # weight.  If we are not allowed to change the
                # given graph, we can create a copy of graph
                self.graph = sorted(self.graph, 
                                    key=lambda item: item[2])

                parent = []
                rank = []

                # Create V subsets with single elements
                for node in range(self.V):
                    parent.append(node)
                    rank.append(0)

                # Number of edges to be taken is equal to V-1
                while e < self.V - 1:

                    # Step 2: Pick the smallest edge and increment
                    # the index for next iteration
                    u, v, w = self.graph[i]
                    i = i + 1
                    x = self.find(parent, u)
                    y = self.find(parent, v)

                    # If including this edge does't
                    #  cause cycle, include it in result 
                    #  and increment the indexof result 
                    # for next edge
                    if x != y:
                        e = e + 1
                        result.append([u, v, w])
                        self.union(parent, rank, x, y)
                    # Else discard the edge

                minimumCost = 0
                print "Edges in the constructed MST"
                for u, v, weight in result:
                    minimumCost += weight
                    print("%d -- %d == %d" % (u, v, weight))
                print("Minimum Spanning Tree" , minimumCost)

        # Driver code
        g = Graph(4)
        g.addEdge(0, 1, 10)
        g.addEdge(0, 2, 6)
        g.addEdge(0, 3, 5)
        g.addEdge(1, 3, 15)
        g.addEdge(2, 3, 4)

        # Function call
        g.KruskalMST()

        # This code is contributed by Neelam Yadav
        
        # 출처 : https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/ 
      </code></pre>
      
  + ### 프림 알고리즘 ( Prim’s algorithm ) 
    + 개요
      + 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장해나가는 알고리즘 
      + 정점 선택을 기반으로 하는 알고리즘  
      + 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리 확장
      + 그래프에 간선이 많이 존재하는 ‘밀집 그래프(Dense Graph)’ 의 경우 쓰기 적합 
      + 알고리즘 
        1. 최소 신장 트리에 이미 포함된 정점을 추적하는 설정 mstSet를 생성
        2. 입력 그래프의 모든 정점에 키 값 할당    
          ( 모든 키 값을 무한대로 초기화, 첫 번째 꼭지점에 대해 키 값을 0으로 할당하여 먼저 선택 )   
        3. mstSet이 모든 정점을 포함하지 않을 동안 반복
          3-1. mstSet에 없고 최소 키 값이 있는 꼭지점 u를 선택
          3-2. ustomstSet를 포함
          3-3. u의 모든 인접 정점의 키 값을 업데이트
          
    + 구현
      <pre><code>
        # A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
        # The program is for adjacency matrix representation of the graph 

        import sys # Library for INT_MAX 

        class Graph(): 

            def __init__(self, vertices): 
                self.V = vertices 
                self.graph = [[0 for column in range(vertices)]  
                            for row in range(vertices)] 

            # A utility function to print the constructed MST stored in parent[] 
            def printMST(self, parent): 
                print "Edge \tWeight"
                for i in range(1, self.V): 
                    print parent[i], "-", i, "\t", self.graph[i][ parent[i] ] 

            # A utility function to find the vertex with  
            # minimum distance value, from the set of vertices  
            # not yet included in shortest path tree 
            def minKey(self, key, mstSet): 

                # Initilaize min value 
                min = sys.maxint 

                for v in range(self.V): 
                    if key[v] < min and mstSet[v] == False: 
                        min = key[v] 
                        min_index = v 

                return min_index 

            # Function to construct and print MST for a graph  
            # represented using adjacency matrix representation 
            def primMST(self): 

                # Key values used to pick minimum weight edge in cut 
                key = [sys.maxint] * self.V 
                parent = [None] * self.V # Array to store constructed MST 
                # Make key 0 so that this vertex is picked as first vertex 
                key[0] = 0 
                mstSet = [False] * self.V 

                parent[0] = -1 # First node is always the root of 

                for cout in range(self.V): 

                    # Pick the minimum distance vertex from  
                    # the set of vertices not yet processed.  
                    # u is always equal to src in first iteration 
                    u = self.minKey(key, mstSet) 

                    # Put the minimum distance vertex in  
                    # the shortest path tree 
                    mstSet[u] = True

                    # Update dist value of the adjacent vertices  
                    # of the picked vertex only if the current  
                    # distance is greater than new distance and 
                    # the vertex in not in the shotest path tree 
                    for v in range(self.V): 

                        # graph[u][v] is non zero only for adjacent vertices of m 
                        # mstSet[v] is false for vertices not yet included in MST 
                        # Update the key only if graph[u][v] is smaller than key[v] 
                        if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                                key[v] = self.graph[u][v] 
                                parent[v] = u 

                self.printMST(parent) 

        g = Graph(5) 
        g.graph = [ [0, 2, 0, 6, 0], 
                    [2, 0, 3, 8, 5], 
                    [0, 3, 0, 0, 7], 
                    [6, 8, 0, 0, 9], 
                    [0, 5, 7, 9, 0]] 

        g.primMST(); 

        # Contributed by Divyanshu Mehta
        
        # 출처 : https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/ 
      </code></pre>
  

> ###### 참고 : https://www.fun-coding.org/Chapter19-greedy-live.html , https://skerritt.blog/greedy-algorithms/ ,https://janghw.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Greedy-Algorithm-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 , https://www.geeksforgeeks.org/greedy-algorithms/#standardGreedyAlgorithms , https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 , https://www.fun-coding.org/Chapter20-shortest-live.html , https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html ,https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html 

<br>

------------

<br>

## 동적 계획법 ( Dynamic Programming )

+ ### 개요
  +  복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법     
    -> 주어진 문제를 풀기 위해서, 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음, 그것을 결합하여 최종적인 목적에 도달   
  + 하위 문제의 수가 기하급수적으로 증가할 때 유용함 
  + 메모이제이션(Memoization) : 동적계획법에서 아주 중요한 개념으로 함수의 값을 계산한 뒤 계산된 값을 배열에 저장하는 방식    
    -> 이러한 메모이제이션은 필요한 때마다 함수를 다시 호출하지 않고 값을 빠르게 가져올 수 있음 
   
+ 피보나치를 통해 구현방식 알아보기 
  + Top-down - 큰 문제를 작은 문제로 쪼개면 해결 - 재귀로 구현
    <pre><code>
      def fibo(n):
        if n < 3:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)
    </code></pre>
    
  + Bottom-up : 작은 문제부터 차례대로 해결 - 반복문으로 구현
    <pre><code>
      def fibo(n):
        li = []
        for i in range(0,n):
            if i < 2:
                li.append(1)
            else:
                li.append(li[i-1] + li[i-2])
                
        return li[n-1]
    </code></pre>

> ###### 참고 : https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%95 ,https://wooder2050.medium.com/%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95-dynamic-programming-%EC%A0%95%EB%A6%AC-58e1dbcb80a0 ,https://velog.io/@polynomeer/%EB%8F%99%EC%A0%81-%EA%B3%84%ED%9A%8D%EB%B2%95Dynamic-Programming

<br>

------------

# 파이썬으로 구현하는 자료구조

<br>

## 목록
+ [배열 ( Array )](#배열-array)
+ [리스트 ( List )](#리스트-list)
  +  [단일 연결 리스트 ( Singly Linked List )](#단일-연결-리스트--singly-linked-list-)
  +  [이중 연결 리스트 ( Doubly Linked List )](#이중-연결-리스트--doubly-linked-list-)
  +  [원형 연결 리스트 ( Circular Linked List )](#원형-연결-리스트--circular-linked-list-)
+ [스택 ( Stack )](#스택--stack-)
+ [큐 ( Queue )](큐--queue-)
  + [우선순위 큐 ( Priority Queue )](#우선순위-큐--priority-queue-)
+ [셋 ( Set )](#셋--set-)
+ [트리 ( Tree )](#트리--tree-)
  + [이진 트리 ( Binary Tree )](#이진-트리--binary-tree-)
+ [그래프 ( Graph )](#그래프--graph-)

<br>

------------------

<br>

## 배열 (Array)

+ ### 1. 개요
  + 같은 타입의 변수들로 이루어진 유한 집합
  + 배열을 구성하는 각각의 값 = 배열 요소 (element)
  + 배열에서의 위치를 가리키는 숫자 = 인덱스 (index)
  + 같은 종류의 데이터를 많이 다뤄야 하는 경우에 사용할 수 있는 가장 기본적인 자료 구조
  
+ ### 2. 장점
  + 구현이 쉬움
  + 참조를 위한 추가적인 메모리 할당이 필요없음
  + 운영체제의 캐시 지역성 활용 가능
  + 검색 성능이 좋음 ( index를 이용한 random access 가능 )
  
    -> 순차 접근인 경우에도 연결 리스트보다 빠른 성능 
  
    -> ( 배열은 데이터를 하나의 연속된 메로리 공간에 할당하므로 )
  
+ ### 3. 단점
  + 자료의 삽입, 삭제 과정에서 비효율적 
  
    ( 다음 항목의 모든 요소들을 이동시켜야 하기 때문 )
  
  + 크기를 바꿀 수 없음 
  
    ( 크게 잡으면 메모리 낭비, 작게 잡으면 자료 저장 불가 )
  
  + 메모리 재사용 불가능 
  
    ( 배열은 초기 사이즈만큼의 메모리를 할당 받아 사용 )
  
    -> 데이터의 존재 유무와 상관없이 일정한 크기의 메모리 공간을 점유
  
    -> 배열 요소를 삭제하더라도 배열 자체가 메모리에 남음
  
+ ### 파이썬의 List가 배열과 다른점
  + 서로 다른 자료형을 원소로 가질 수 있음
  + 동적 배열로써 배열과는 다르게 자유롭게 크기를 확장할 수 있음
  + 원소들의 값을 자유롭게 변경 가능함
  
<br>

> ###### 참고 : http://www.tcpschool.com/c/c_array_oneDimensional , https://codedragon.tistory.com/7468 , https://daimhada.tistory.com/106?category=820522

------------
------------
<br>

## 리스트 (List)

+ ## 단일 연결 리스트 ( Singly Linked List )

  + ### 1. 개요
    + 동일한 타입의 항목들이 일렬로 연결된 것 
    + 데이터를 노드의 형태로 저장
    + 노드의 구성 : 데이터 + 다음 노드를 가르키는 포인터
    + 선형 데이터 자료구조

  + ### 2. 장점
    + Linked list의 길이를 동적으로 조절 가능
    + 데이터의 삽입과 삭제가 쉬움

  + ### 3. 단점
    + 임의의 노드에 바로 접근할 수 없음
    + 다음 노드의 위치를 저장하기 위한 추가 공간이 필요함
    + Cache locality를 활용해 근접 데이터를 사전에 캐시에 저장하기 어려움
    + Linked list를 거꾸로 탐색하기 어려움

  + ### 배열과 다른점
    + 배열은 물리적인 배치 구조 자체가 연속적으로 저장
    + Linked list는 다음 노드를 가르키는 포인터에 다음 노드의 위치를 저장
  
  + 구현
  
  <pre><code>

  # A complete working Python program to demonstrate all 
  # insertion methods of linked list 

  # Node class 
  class Node: 

      # Function to initialise the node object 
      def __init__(self, data): 
          self.data = data  # Assign data 
          self.next = None  # Initialize next as null 


  # Linked List class contains a Node object 
  class LinkedList: 

      # Function to initialize head 
      def __init__(self): 
          self.head = None


      # Functio to insert a new node at the beginning 
      def push(self, new_data): 

          # 1 & 2: Allocate the Node & 
          #        Put in the data 
          new_node = Node(new_data) 

          # 3. Make next of new Node as head 
          new_node.next = self.head 

          # 4. Move the head to point to new Node 
          self.head = new_node 


      # This function is in LinkedList class. Inserts a 
      # new node after the given prev_node. This method is 
      # defined inside LinkedList class shown above */ 
      def insertAfter(self, prev_node, new_data): 

          # 1. check if the given prev_node exists 
          if prev_node is None: 
              print "The given previous node must inLinkedList."
              return

          #  2. create new node & 
          #      Put in the data 
          new_node = Node(new_data) 

          # 4. Make next of new Node as next of prev_node 
          new_node.next = prev_node.next

          # 5. make next of prev_node as new_node 
          prev_node.next = new_node 


      # This function is defined in Linked List class 
      # Appends a new node at the end.  This method is 
      # defined inside LinkedList class shown above */ 
      def append(self, new_data): 

          # 1. Create a new node 
          # 2. Put in the data 
          # 3. Set next as None 
          new_node = Node(new_data) 

          # 4. If the Linked List is empty, then make the 
          #    new node as head 
          if self.head is None: 
              self.head = new_node 
              return

          # 5. Else traverse till the last node 
          last = self.head 
          while (last.next): 
              last = last.next

          # 6. Change the next of last node 
          last.next =  new_node 


      # Utility function to print the linked list 
      def printList(self): 
          temp = self.head 
          while (temp): 
              print temp.data, 
              temp = temp.next



  # Code execution starts here 
  if __name__=='__main__': 

      # Start with the empty list 
      llist = LinkedList() 

      # Insert 6.  So linked list becomes 6->None 
      llist.append(6) 

      # Insert 7 at the beginning. So linked list becomes 7->6->None 
      llist.push(7); 

      # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
      llist.push(1); 

      # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
      llist.append(4) 

      # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
      llist.insertAfter(llist.head.next, 8) 

      print 'Created linked list is:', 
      llist.printList() 

  # This code is contributed by Manikantan Narasimhan 


  # 출처 : https://www.geeksforgeeks.org/linked-list-set-1-introduction/ 
  </code></pre>

<br> 

> ###### 참고 : https://daimhada.tistory.com/72, https://deep-learning-study.tistory.com/146, https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8, https://m.blog.naver.com/beaqon/221240103226 

<br>

+ ## 이중 연결 리스트 ( Doubly Linked List )
  
  + ### 1. 개요
    + 노드의 구성 : 이전 노드를 가리키는 포인터 + 자료 공간 + 다음 노드를 가리키는 포인터 
 
  + ### 2. 장점
    + 단일 연결리스트의 단점을 보완 
    + ( 오직 한 쪽 방향으로만 탐색색하는 것이 아닌 양방향 탐색이 가능함 ) 
    
  + ### 3. 단점
    + 두개의 레퍼런스를 요구함 ( ex: prev, next )

  + ### 단일 연결 리스트와 다른점 
    + 이전 노드에 대한 정보를 알 수 있음  
    + ( 특정 노드의 이전 노드를 삭제하거나 특정 노드의 이전에 삽입 가능 )
  
  + 구현

  <pre><code>

  # A complete working Python program to demonstrate all
  # insertion methods

  # A linked list node
  class Node:

      # Constructor to create a new node
      def __init__(self, data):
          self.data = data
          self.next = None
          self.prev = None

  # Class to create a Doubly Linked List
  class DoublyLinkedList:

      # Constructor for empty Doubly Linked List
      def __init__(self):
          self.head = None

      # Given a reference to the head of a list and an
      # integer, inserts a new node on the front of list
      def push(self, new_data):

          # 1. Allocates node
          # 2. Put the data in it
          new_node = Node(new_data)

          # 3. Make next of new node as head and
          # previous as None (already None)
          new_node.next = self.head

          # 4. change prev of head node to new_node
          if self.head is not None:
              self.head.prev = new_node

          # 5. move the head to point to the new node
          self.head = new_node

      # Given a node as prev_node, insert a new node after
      # the given node
      def insertAfter(self, prev_node, new_data):

          # 1. Check if the given prev_node is None
          if prev_node is None:
              print "the given previous node cannot be NULL"
              return

          # 2. allocate new node
          # 3. put in the data
          new_node = Node(new_data)

          # 4. Make net of new node as next of prev node
          new_node.next = prev_node.next

          # 5. Make prev_node as previous of new_node
          prev_node.next = new_node

          # 6. Make prev_node ass previous of new_node
          new_node.prev = prev_node

          # 7. Change previous of new_nodes's next node
          if new_node.next is not None:
              new_node.next.prev = new_node

      # Given a reference to the head of DLL and integer,
      # appends a new node at the end
      def append(self, new_data):

          # 1. Allocates node
          # 2. Put in the data
          new_node = Node(new_data)

          # 3. This new node is going to be the last node,
          # so make next of it as None
          new_node.next = None

          # 4. If the Linked List is empty, then make the
          # new node as head
          if self.head is None:
              new_node.prev = None
              self.head = new_node
              return

          # 5. Else traverse till the last node
          last = self.head
          while(last.next is not None):
              last = last.next

          # 6. Change the next of last node
          last.next = new_node

          # 7. Make last node as previous of new node
          new_node.prev = last

          return

      # This function prints contents of linked list
      # starting from the given node
      def printList(self, node):

          print "\nTraversal in forward direction"
          while(node is not None):
              print " % d" %(node.data),
              last = node
              node = node.next

          print "\nTraversal in reverse direction"
          while(last is not None):
              print " % d" %(last.data),
              last = last.prev

  # Driver program to test above functions

  # Start with empty list
  llist = DoublyLinkedList()

  # Insert 6. So the list becomes 6->None
  llist.append(6)

  # Insert 7 at the beginning.
  # So linked list becomes 7->6->None
  llist.push(7)

  # Insert 1 at the beginning.
  # So linked list becomes 1->7->6->None
  llist.push(1)

  # Insert 4 at the end.
  # So linked list becomes 1->7->6->4->None
  llist.append(4)

  # Insert 8, after 7.
  # So linked list becomes 1->7->8->6->4->None
  llist.insertAfter(llist.head.next, 8)

  print "Created DLL is: ",
  llist.printList(llist.head)

  # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
  # 출처 : https://www.geeksforgeeks.org/doubly-linked-list/ 

  </code></pre>

  
<br>

> ###### 참고 : https://daimhada.tistory.com/72, https://scarletbreeze.github.io/articles/2019-07/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0(10), https://m.blog.naver.com/PostView.nhn?blogId=beaqon&logNo=221240197476&proxyReferer=https:%2F%2Fwww.google.com%2F

<br>

+ ## 원형 연결 리스트 ( Circular Linked List )
  + ### 1. 개요
    + 모든 노드가 연결되어 원을 형석하는 연결 리스트 ( NULL이 없음 )
 
  + ### 2. 장점
    + 한 노드에서 다른 모든 노드로의 접근이 가능함
      ( 노드의 삽입, 삭제가 자유로움 )
    
  + ### 3. 단점
    + 노드의 삽입, 삭제 시 선행 노드의 포인터가 필요
    + 원형으로 순환하기 때문에 무한 루프에 빠질 가능성이 있음

  + ### 단일 연결 리스트와 다른점 
    + 단일 연결 리스트의 마지막 노드는 NULL을 가리켰음
    + 하지만 원형 연결 리스트의 마지막 노드는 첫 번째 노드를 가리킴
  
  + 구현 
  
  <pre><code>

  # Python program to demonstrate  
  # circular linked list traversal  

  # Structure for a Node 
  class Node: 

      # Constructor to create  a new node 
      def __init__(self, data): 
          self.data = data  
          self.next = None

  class CircularLinkedList: 

      # Constructor to create a empty circular linked list 
      def __init__(self): 
          self.head = None

      # Function to insert a node at the beginning of a 
      # circular linked list 
      def push(self, data): 
          ptr1 = Node(data) 
          temp = self.head 

          ptr1.next = self.head 

          # If linked list is not None then set the next of 
          # last node 
          if self.head is not None: 
              while(temp.next != self.head): 
                  temp = temp.next 
              temp.next = ptr1 

          else: 
              ptr1.next = ptr1 # For the first node 

          self.head = ptr1  

      # Function to print nodes in a given circular linked list 
      def printList(self): 
          temp = self.head 
          if self.head is not None: 
              while(True): 
                  print "%d" %(temp.data), 
                  temp = temp.next
                  if (temp == self.head): 
                      break 


  # Driver program to test above function 

  # Initialize list as empty 
  cllist = CircularLinkedList() 

  # Created linked list will be 11->2->56->12 
  cllist.push(12) 
  cllist.push(56) 
  cllist.push(2) 
  cllist.push(11) 

  print "Contents of circular Linked List"
  cllist.printList() 

  # This code is contributed by  
  # Nikhil Kumar Singh(nickzuck_007) 
  # 출처 : https://www.geeksforgeeks.org/circular-linked-list-set-2-traversal/ 

  </code></pre>

  
<br>

> ###### 참고 : https://daimhada.tistory.com/72, https://ehrn35.tistory.com/8, https://jwlee010523.tistory.com/entry/%EC%9B%90%ED%98%95-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8Circular-Linked-List 

<br>

------------
------------
<br>

## 스택 ( Stack )

+ ### 1. 개요
  + 한 쪽으로만 자료를 넣고 뺄 수 있는 구조
  + 구조 : FILO - First in Last Out 
  + 활용 예 ) 재귀 알고리즘, 괄호 검사, 역순 문자열 등 
  
+ ### 2. 장점
  + 히스토리 역추적에 최적화
    ( ex : 실행 취소(Undo), 복구(Redo) 등 )
    
+ ### 3. 단점
  + 크기가 불확실 할 때 확장시 확장연산이 오래걸림
  + 데이터 탐색이 오래 걸림 
  
+ ### 구현

  <pre><code>

  # Python program to demonstrate 
  # stack implementation using a linked list. 
  # node class
  class Node:
     def __init__(self, value):
        self.value = value
        self.next = None

  class Stack:

     # Initializing a stack. 
     # Use a dummy node, which is 
     # easier for handling edge cases. 
     def __init__(self):
        self.head = Node("head")
        self.size = 0

     # String representation of the stack
     def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
           out += str(cur.value) + "->"
           cur = cur.next
        return out[:-3]   

     # Get the current size of the stack
     def getSize(self):
        return self.size

     # Check if the stack is empty
     def isEmpty(self):
        return self.size == 0

     # Get the top item of the stack
     def peek(self):

        # Sanitary check to see if we 
        # are peeking an empty stack. 
        if self.isEmpty():
           raise Exception("Peeking from an empty stack")
        return self.head.next.value

     # Push a value into the stack. 
     def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

     # Remove a value from the stack and return. 
     def pop(self):
        if self.isEmpty():
           raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

  # Driver Code
  if __name__ == "__main__":
     stack = Stack()
     for i in range(1, 11):
        stack.push(i)
     print(f"Stack: {stack}")

     for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
     print(f"Stack: {stack}")

  # 출처 : https://www.geeksforgeeks.org/stack-in-python/ 

  </code></pre>

<br>

> ###### 참고 : https://galid1.tistory.com/178, https://cloudstudying.kr/lectures/141, https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue 

------------
<br>

## 큐 ( Queue )

  + ### 1. 개요
    + 데이터의 삽입 삭제가 서로 다른 방향에서 이루어짐
    + 구조 : FIFO - First in First Out ( 선입선출 ) 
    + 활용 예 ) BFS, 캐싱 처리, 프린터 출력 처리 등

  + ### 2. 장점
    + 입력 데이터들의 순서를 정하는데 최적화

  + ### 3. 단점
    + front, rear 부분 인덱스를 증가시키면 문제 발생
      ( front 부분이 배열 끝에 도달 -> 공간이 남아있는데도 쓰지 못하는 경우 발생 )
        -> 원형 큐로 해결 가능
 
  + 구현
  
  <pre><code>
  # Python3 program for array implementation of queue 
  
  # Class Queue to represent a queue 
  class Queue: 

      # __init__ function 
      def __init__(self, capacity): 
          self.front = self.size = 0
          self.rear = capacity -1
          self.Q = [None]*capacity 
          self.capacity = capacity 

      # Queue is full when size becomes 
      # equal to the capacity  
      def isFull(self): 
          return self.size == self.capacity 

      # Queue is empty when size is 0 
      def isEmpty(self): 
          return self.size == 0

      # Function to add an item to the queue.  
      # It changes rear and size 
      def EnQueue(self, item): 
          if self.isFull(): 
              print("Full") 
              return
          self.rear = (self.rear + 1) % (self.capacity) 
          self.Q[self.rear] = item 
          self.size = self.size + 1
          print("% s enqueued to queue"  % str(item)) 

      # Function to remove an item from queue.  
      # It changes front and size 
      def DeQueue(self): 
          if self.isEmpty(): 
              print("Empty") 
              return

          print("% s dequeued from queue" % str(self.Q[self.front])) 
          self.front = (self.front + 1) % (self.capacity) 
          self.size = self.size -1

      # Function to get front of queue 
      def que_front(self): 
          if self.isEmpty(): 
              print("Queue is empty") 

          print("Front item is", self.Q[self.front]) 

      # Function to get rear of queue 
      def que_rear(self): 
          if self.isEmpty(): 
              print("Queue is empty") 
          print("Rear item is",  self.Q[self.rear]) 


  # Driver Code 
  if __name__ == '__main__': 

      queue = Queue(30) 
      queue.EnQueue(10) 
      queue.EnQueue(20) 
      queue.EnQueue(30) 
      queue.EnQueue(40) 
      queue.DeQueue() 
      queue.que_front() 
      queue.que_rear() 
      
  # 출처 : https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/ 
  </code></pre> 
  
> ###### 참고 : https://syundev.tistory.com/34, https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue 

## 우선순위 큐 ( Priority Queue )
  
  + ### 1. 개요
    + 활용 예 ) CPU 스케줄링, Dijkstra의 최단 경로 알고리즘, 대기열 응용프로그램 등 
    + 주로 힙으로 구현

  + ### 2. 장점
    + 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나옴

  + ### 3. 단점
    + 배열로 구현할 시 ( 최악의 경우 )
      1) 데이터 삽입 과정에서 인덱스를 모두 밀어야 함 
      2) 삽입 위치를 찾기 위해 모든 인덱스를 탐색해야 함
    + 연결 리스트로 구현할 시 ( 최악의 경우 )
      1) 삽입 위치를 찾기 위해 모든 인덱스를 탐색해야 함
 
  + 구현

  <pre><code>
  
  import heapq
  class PriorityQueue():
      def __init__(self):
          self.queue = []
          self.count = 0

      def enqueue(self, priority, v):
          self.count += 1
          heapq.heappush(self.queue,(priority, self.count,  v))

      def dequeue(self):
          heapq.heappop(self.queue)

      def display(self):
          print(self.queue)


  if __name__ == "__main__":
      pq = PriorityQueue()
      print(pq.enqueue(1, 'test1'))
      print(pq.enqueue(4, 'test2'))
      print(pq.enqueue(3, 'test3'))
      print(pq.enqueue(1, 'test4'))
      print(pq.enqueue(2, 'test5'))
      print(pq.enqueue(1, 'test6'))
      pq.display() # [(1, 1, 'test1'), (1, 4, 'test4'), (1, 6, 'test6'), (4, 2, 'test2'), (2, 5, 'test5'), (3, 3, 'test3')]

  #출처 : https://daimhada.tistory.com/169
  </code></pre> 

> ###### 참고 : https://hannom.tistory.com/36 

<br>

------------
<br>

## 셋 ( Set )

  + ### 1. 개요
    + 

  + ### 2. 장점
    + 

  + ### 3. 단점
    +
 
  + 구현

  <pre><code>
  </code></pre> 
  
<br>

------------
<br>

## 트리 ( Tree )

  + ### 1. 개요
    + 노드로 이루어진 자료 구조
    + 트리는 하나의 루트 노드를 가짐
    + 루트 노드는 0개 이상의 자식 노드를 가짐
    + 자식 노드 또한 0개 이상의 자식 노드를 가짐 ( 반복 ) 
    + 활용 예 ) 리눅스, 윈도우 등의 파일 시스템 구조
    
  + ### 2. 용어 정리
    + 루트 노드(root node): 부모가 없는 노드, 트리는 하나의 루트 노드만을 가짐
    + 단말 노드(leaf node): 자식이 없는 노드, ‘말단 노드’ 또는 ‘잎 노드’라고도 불림
    + 내부(internal) 노드: 단말 노드가 아닌 노드
    + 간선(edge): 노드를 연결하는 선 (link, branch 라고도 부름)
    + 형제(sibling): 같은 부모를 가지는 노드
    + 노드의 크기(size): 자신을 포함한 모든 자손 노드의 개수
    + 노드의 깊이(depth): 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수
    + 노드의 레벨(level): 트리의 특정 깊이를 가지는 노드의 집합
    + 노드의 차수(degree): 하위 트리 개수 / 간선 수 (degree) = 각 노드가 지닌 가지의 수
    + 트리의 차수(degree of tree): 트리의 최대 차수
    + 트리의 높이(height): 루트 노드에서 가장 깊숙히 있는 노드의 깊이

  + ### 3. 특징
    + 그래프의 한 종류로 ‘최소 연결 트리’ 라고도 불림
    + 계층 모델에 속함
    + 사이클이 없음
    + 루트에서 어떤 노드로 가는 경로는 유일함
    + 종류 : 이진 트리, 이진 탐색 트리, 균형 트리 , 이진 힙 등 
    
  + 구현
  
  <pre><code>
  
  # Python program to introduce Binary Tree 
  
  # A class that represents an individual node in a 
  # Binary Tree 
  class Node: 
      def __init__(self,key): 
          self.left = None
          self.right = None
          self.val = key 


  # create root 
  root = Node(1) 
  ''' following is the tree after above statement 
          1 
        /   \ 
       None  None'''

  root.left      = Node(2); 
  root.right     = Node(3); 

  ''' 2 and 3 become left and right children of 1 
             1 
           /   \ 
          2      3 
       /    \    /  \ 
     None None None None'''


  root.left.left  = Node(4); 
  '''4 becomes left child of 2 
             1 
         /       \ 
        2          3 
      /   \       /  \ 
     4    None  None  None 
    /  \ 
  None None'''
  # 출처 : https://www.geeksforgeeks.org/binary-tree-set-1-introduction/ 
  </code></pre> 
  
  > ###### 참조 : https://gmlwjd9405.github.io/2018/08/12/data-structure-tree.html , https://m.blog.naver.com/justkukaro/220548164184

## 이진 트리 ( Binary Tree )

  + ### 1. 개요
    + 

  + ### 2. 장점
    + 

  + ### 3. 단점
    +
 
  + 구현
  
  <pre><code>
  </code></pre> 


<br>

------------
<br>

## 그래프 ( Graph )

  + ### 1. 개요
    + 

  + ### 2. 장점
    + 

  + ### 3. 단점
    +
 
  + 구현
  
  <pre><code>
  </code></pre>  

<br>

------------

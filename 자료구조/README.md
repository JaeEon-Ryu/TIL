# 파이썬으로 구현하는 자료구조

## 목록
+ 배열
+ 리스트

<br>

------------------

<br>

## 배열(Array)

+ ### 1. 개요
  > + 같은 타입의 변수들로 이루어진 유한 집합
  > + 배열을 구성하는 각각의 값 = 배열 요소 (element)
  > + 배열에서의 위치를 가리키는 숫자 = 인덱스 (index)
  > + 같은 종류의 데이터를 많이 다뤄야 하는 경우에 사용할 수 있는 가장 기본적인 자료 구조
  
+ ### 2. 장점
  > + 구현이 쉬움
  > + 참조를 위한 추가적인 메모리 할당이 필요없음
  > + 운영체제의 캐시 
  > + 검색 성능이 좋음 ( index를 이용한 random access 가능 )
  >
  >   -> 순차 접근인 경우에도 연결 리스트보다 빠른 성능 
  >
  >   -> ( 배열은 데이터를 하나의 연속된 메로리 공간에 할당하므로 )
  
+ ### 3. 단점
  > + 자료의 삽입, 삭제 과정에서 비효율적 
  >
  >   ( 다음 항목의 모든 요소들을 이동시켜야 하기 때문 )
  >
  > + 크기를 바꿀 수 없음 
  >
  >   ( 크게 잡으면 메모리 낭비, 작게 잡으면 자료 저장 불가 )
  >
  > + 메모리 재사용 불가능 
  >
  >   ( 배열은 초기 사이즈만큼의 메모리를 할당 받아 사용 )
  >
  >   -> 데이터의 존재 유무와 상관없이 일정한 크기의 메모리 공간을 점유
  >
  >   -> 배열 요소를 삭제하더라도 배열 자체가 메모리에 남음
  
+ ### 파이썬의 List가 배열과 다른점
  > + 서로 다른 자료형을 원소로 가질 수 있음
  > + 동적 배열로써 배열과는 다르게 자유롭게 크기를 확장할 수 있음
  > + 원소들의 값을 자유롭게 변경 가능함
  
<br>

######  : http://www.tcpschool.com/c/c_array_oneDimensional , https://codedragon.tistory.com/7468 , https://daimhada.tistory.com/106?category=820522

------------
------------
<br>

## 리스트(List): Singly Linked List / Doubly Linked List / Circular linked List

+ ### 1. 개요
  > + 데이터를 노드의 형태로 저장
  > + 노드의 구성 : 데이터, 다음 노드를 가르키는 포인터
  > + 선형 데이터 자료구조
  
+ ### 2. 장점
  > + Linked list의 길이를 동적으로 조절 가능
  > + 데이터의 삽입과 삭제가 쉬움
  
+ ### 3. 단점
  > + 임의의 노드에 바로 접근할 수 없음
  > + 다음 노드의 위치를 저장하기 위한 추가 공간이 필요함
  > + Cache locality를 활용해 근접 데이터를 사전에 캐시에 저장하기 어려움
  > + Linked list를 거꾸로 탐색하기 어려움
  
+ ### 배열과 다른점
  > + 배열은 물리적인 배치 구조 자체가 연속적으로 저장
  > + Linked list는 다음 노드를 가르키는 포인터에 다음 노드의 위치를 저장
  
+ ## 단일 연결 리스트 ( Singly Linked List )
  > + 각 노드의 구성 : 자료 공간 + 한개의 포인터 공간
  >
  >   ( 각 노드의 포인터는 다음 노드를 가리킴 )
  >
  > + 구현
  >
<pre><code>

# 노드 클래스 생성
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self): # 실제 값을 보기 위해 필요 # 없을 시 주소값을 보게 된다
        return str(self.data)

# 단일 연결 리스트 생성
class singly_linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    # 인덱스에 해당하는 노드의 값 얻기
    def select_node(self, index):
   
        current = self.head # 처음부터 탐색
        for _ in range(index):
            current = current.next
        return current.data

    # 매개변수로 받은 인덱스에 노드 추가
    def insert_node(self, index, data):

        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return

        current = self.head
        for _ in range(1, index):
            current = current.next

        node.next = current.next
        current.next = node
        self.size += 1

    # 앞쪽에 추가
    def push_left(self, val):
        self.insert_node(0, val)

    # 뒷쪽에 추가
    def push_right(self, val):
        self.insert_node(self.size, val)

    # 매개변수로 받은 인덱스 부분 삭제
    def delete_node(self, index):

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head 
        for _ in range(1, index): 
            current = current.next 

        current.next = current.next.next
        self.size -= 1

if __name__ == "__main__":
    s_list = singly_linked_list()
    s_list.push_right(Node(1))
    s_list.push_right(Node(2))
    s_list.push_right(Node(3))
    s_list.push_right(Node(4))
    s_list.push_right(Node(5))
    s_list.delete_node(0)
    print(s_list.select_node(0)) # 2
    print(s_list.select_node(3)) # 5

</code></pre>

  
  
<br>

###### 참고 : https://daimhada.tistory.com/72, https://deep-learning-study.tistory.com/146, https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8

------------
------------
<br>

## 스택(Stack)

<br>

------------
<br>

## 큐(Queue)

<br>

------------
<br>

## 맵(Map)

<br>

------------
<br>

## 셋(Set)

<br>

------------
<br>

## 트리/바이너리 트리 (Tree/Binary Tree)

<br>

------------
<br>

## 프라이오리티 큐(Priority Queue)

<br>

------------
<br>

## 그래프(Graph)

<br>

------------

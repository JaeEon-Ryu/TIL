# 파이썬으로 구현하는 알고리즘

<br>

## 목록
+ [탐색 알고리즘 ( Search Algorithms )](#탐색-알고리즘--searching-algorithms-)
+ [정렬 알고리즘 ( Sorting Algorithms )](#정렬-알고리즘--sorting-algorithms-)
+ [그래프 알고리즘 ( Graph Algorithms )](#그래프-알고리즘--graph-algorithms-)
+ [탐욕 알고리즘 ( Greedy Algorithms )](#탐욕-알고리즘--greedy-algorithms-)
+ [동적 프로그래밍 ( Dynamic Programming )](#동적-프로그래밍--dynamic-programming-)

<br>

------------------

<br>

## 탐색 알고리즘 ( Searching Algorithms )

+ ### 1. 개요
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

+ ### 1. 개요
  + 

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : 

<br>

------------

<br>

## 그래프 알고리즘 ( Graph Algorithms )

+ ### 1. 개요
  + 

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : 

<br>

------------

<br>

## 탐욕 알고리즘 ( Greedy Algorithms )

+ ### 1. 개요
  + 

<pre><code>
#코드 테스트
</code></pre>

> ###### 참고 : 

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

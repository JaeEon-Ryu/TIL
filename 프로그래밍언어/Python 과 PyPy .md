## 개요
+ Python의 언어 구현 중 하나
+ C로 짜인 기존의 CPython과 달리 Python으로 Python을 만든 프로젝트
+ 성능면에서 CPython 능가
+ JIT (Just In Time) 컴파일 사용  
  -> stackoverflow에 따르면 이로 인해 기존 Cpython 보다 7.5배 더 빠르다는 주장이 있음

<br>

## 기존의 Cpython
+ 인터프리터이면서 컴파일러인 존재
+ 실행순서 : python 코드 컴파일 -> bytecode 변환 -> 인터프리터 실행

<br>

## PyPy 구현체
+ JIT(just in time) 컴파일 : 프로그램을 실행하는 시점에서 필요한 부분들을 즉석으로 컴파일 하는 방식  
  -> 인터프리트 하면서 자주 쓰이는 코드를 캐싱하기 때문에 인터프리터의 느린 실행속도 개선 가능  
    ( JVM 에서도 바이트 코드를 기계어로 번역할 때, JIT 컴파일러를 사용함 )  

<br>

## 성능차이
+ 속도   : PyPy > Python ( PyPy 가 더 빠름 )
+ 메모리 : PyPy < Python ( PyPy 의 메모리가 더 많음 )  
  ```
  실제 백준 2557 문제에 같은 코드를 제출 한 결과

  1. 메모리
  PyPy3 : 121,675 KB
  Python3 : 29,380 KB

  2. 처리 속도
  PyPy3 : 148 ms
  Python3 : 60ms
  ```
  
<br>

## 결론
+ 간단한 코드일 때 : Python3가 우세함
+ 복잡한 코드를 반복 사용할 때 : PyPy3가 우세함
+ 따라서 코드 상황에 맞추어 적절히 사용할 것  

<br>

#### reference
[ 나무위키 - PyPy ](https://namu.wiki/w/PyPy)  
[ Ralp Ralp - Python3 와 PyPy3 차이](https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4)  
[ takudaddy - 기초 문제 풀기로 살펴보는 파이썬과 파이파이 차이 ](https://takudaddy.tistory.com/125)  
[ stackoverflow - what's the differences python3 and pypy3 ](https://stackoverflow.com/questions/59050724/whats-the-differences-python3-and-pypy3)  

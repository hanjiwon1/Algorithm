본격적으로 코딩테스트 준비를 시 작 했 다.  

바로 알고리즘부터 풀고싶었지만 파이썬 기초 문법 복습이 필요할 것 같아서 백준 단계별 문제에서 1단계부터 빠르게 풀어보았다.  

사실 파이썬으로 알고리즘을 짜는건 처음인 것 같다. 꼭 거쳐야 할 과정이라고 생각하고, 오늘 풀어본 문제들 중 한번 더 보고 기억해야할 것들을 기록해보려 한다.
___
## 2884. 알람시계

이건 금방 풀었지만 다른 사람들이 짠 코드를 보니 시간계산 수학적으로 다루는 사람이 많았다.

수학적 사고를 키우는 연습도 필요하다고 생각했다.
___
## 15552. 빠른 A+B
파이썬에서 입력을 받을 때 input보다 빠른 sys.stdin.readline()을 사용하여 푸는 문제였다.

백준에서 준 팁에 의하면 readline을 사용하여 입력받을 때 개행문자까지 함께 입력받기 대문에 문자열 저장의 경우 .rstrip()을 추가로 사용해 주어야 한다.
___
## 2742. 기찍N
자연수 N이 주어졌을 때 N부터 1까지 역순으로 출력시키는 문제이다.

파이썬 코딩를 제대로 한적이 거의 없어서 그런지 range()를 활용하지 못했다.   

`내가 짠 코드`
```python
n = int(input())
for i in range(n):
    print(n-i)
```

다른 사람이 제출한 코드를 보니 range로 반복을 잘 활용하고 있었다.  

`다른 사람 코드`
```python
n = int(input())

for i in range(n,0,-1):
    print(i)
```
range(start, stop, step)은 
start부터 step의 간격으로 stop 직전 까지의 정수 범위를 의미한다.
___
## 2438. 별찍기 - 1
이것 역시 씨로 코딩하던 습관이 베여서 괜히 이중포문을 썼다. 

효율적인 코딩을 위해 여러 함수나 기능을 잘 이용하고 싶은데 다른 사람이 짠 코드를 보면 배워야 할 것이 산더미라는 것을 느낀다.  
문득 알고리즘도, 파이썬도 너무 오랜만이라 겁이 난다..ㅋ

`내가 짠 코드`
```python
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
```

`다른 사람 코드`
```python
s=int(input())

for i in range(1,s+1):
    print("*"*i)
```
파이썬은 참 직관적인 구조인것같다. 그걸 잘 사용하느냐는 이제 나의 능력인데, 여러 코드를 보고 부족한 점을 매꿔야겠다고 다시한번 생각했다.
___
## 10871. X보다 작은 수
리스트를 개행 없이 띄어쓰기로 입력받을 때 sys.stdin.readline().split()을 이용해서 받으면 list로 저장되는 것을 이용했다.  

`내가 짠 코드`
```python
import sys
n, x = map(int, input().split())
a = sys.stdin.readline().split()
for i in range(n):
    if int(a[i])<x: print(a[i], end=' ')
```
제출 후 다른 사람은 어떻게 짯을까 보는데 map함수를 이용해서 list를 입력받을 수 있다는 사실을 알게되었다.  

`다른 사람 코드`
```python
c=list(map(int,input().split()))
```
어떤 것이 성능면에서 좋은지는 코드가 너무 짧고 단순해서 모르겠지만 input보다는 readline이 더 빠르다는 이야기를 들어서 입력 데이터가 커지면 readline을 사용해야겠다.

map함수를 이용하지 않고 입력받는 것도 발견했다.  
```python
seq=input()

for i in seq.split():
    if (int(i)<x):
        print(int(i),end=" ")
```
정수 데이터를 다루는 문제였는데, 문자열로 입력받고 split()해준 뒤 int로 변환해주는 방식이다.
___
## 10951. A+B - 4
루프를 돌리는 문제였는데 문제 설명에 종료조건이 나와있지 않아서 잠시 당황한 문제다. 

언어를 공부할 때 영어가 싫어서 예외처리만 나오면 넘겨버렸더니 이 상황이 온것같다..ㅋ(반성중)

oj시스템에서 채점을 위해 넣는 파일이 끝나면(EOF) 루프가 종료될 수 있는 예외처리를 해주는 문제다.

EOF의 마커는 빈 문자열이다.
try문을 실행하던 중 에러가 발생하면 나머지 절은 건너뛰고 except절이 실행된다.

`내가 짠 코드`
```python
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
```
예외처리를 하지 않고 실행시키는 방식도 있다.

`다른 사람 코드`
```python
import sys

for i in sys.stdin:
    a,b = map(int,i.split())
    print(a+b)
```
호옹..
유독 짧은 코드가 있길래 보았는데 보길 잘한것같다.
___
## 3052. 나머지

`내가 짠 코드`
```python
a = []
cnt = 1
for i in range(10):
    n = int(input())
    a.append(n%42)
a.sort()
for j in range(9):
    if a[j] != a[j+1]: cnt += 1
print(cnt)
```
처음에 이렇게 풀었는데

리스트에 원소를 append하면서 동시에 input을 받을 수 있다는 것을 알았다.
또 리스트 원소 중 중복을 제거할 때 set()을 사용한다.

`이렇게`
```python
num = []
for i in range(10):
    num.append(int(input())%42)


print(len(set(num)))
```
[리스트 설명(파이썬 정리 잘되어있는듯)](https://blockdmask.tistory.com/425)

___
## 4344. 평균은 넘겠지
`내가 짠 코드`
```python
c = int(input())
for _ in range(c):
    std = list(map(int, input().split()))
    std_num = std[0]
    del(std[0])
    AVG = sum(std)/len(std)

    cnt = 0

    for i in range(len(std)):
        if std[i]>AVG: cnt += 1

    print(format((cnt/std_num*100), "0.3f"), '%', sep='')

```
제출 후 코드가 유난히 짧은 답안이 있어서 확인해 보았다.

`다른 사람 코드`
```python
n = int(input())

for i in range(n):
    li = list(map(int,input().split()))
    mean = sum(li[1:])/li[0]
    cnt = 0
    for i in li[1:]:
        if i>mean:
            cnt+=1 
    print('%.3f'%(cnt/li[0]*100)+'%')
```
리스트의 인덱스와 프린트문을 잘 쓴것 같다.

아직 프린트를 할 때 조차 어떤 방식이 더 효율적인지 알 수가 없다. 모르는게 많아서..ㅎ
___
하고싶은 말을 좀 더 써보자면 졸업 후 혼자서 개발공부를 하고 개발자로서 취업준비를 한다는 것이 좀 두렵기도 하다. 다들 쉬운 방법을 아는 것 같고 나 혼자만 덩그러니 떨어져서 혹시 내가 하는 방식이 잘못되진 않았을까, 내가 너무 어렵고 느리게 가는건 아닐까 불안한 마음이 들었기 때문이다.    

전공을 따르지 않겠다고 고집피우며 4년을 보내고 졸업을 앞둔 지금 개발자로서의 꿈을 가졌지만, 늦었다고 생각하지 않고 꾸준히 성실하게 내가 해야하는 것들을 해 나아간다면 그게 언젠가 내 인생의 좋은 거름이 될거라는 확신을 가지고 기쁜 마음으로 공부할 것이다.  

노력이 얼마나 중요한지 내 자신에게 증명해보일 것이다.  
누가 볼까 부끄럽지만 지금 마음가짐을 잊지 않기 위해 이렇게 남겨본다. ㅋㅋ

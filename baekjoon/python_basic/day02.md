오늘은 프론트앤드를 시작하기 전 html과 css에 대해 전반적으로 공부하고 알고리즘은 파이썬으로 함수를 구현하는것만 해보았다.  

지금 하는게 사실 알고리즘공부라기 보다는 파이썬을 좀 더 빠르게 사용하기 위한 연습이라고 볼 수 있는데, 언제까지 이것만 잡고있을 수는 없지만 아직은 아는것 보다 모르는 문법이 더 많은 것 같다고 생각해서 백준 단계별 문제를 모두 풀어보기로 계획을 바꾸었다. 그래도 어제보단 속도가 붙었다. 얼른 높은 레벨 문제도 머리써가면서 풀어보고싶다.  

___
## 4673. 셀프넘버
10000보다 작거나 같은 셀프넘버를 출력하는 프로그램이다. 반복문을 최대한 사용하지 않고 사용하는 방법을 고민해보았지만 1부터 10000까지 돌리는 반복문을 총 3개 사용했다.  
아직 문제가 단순해서 시간적인 부분은 크게 적용되지 않지만 문제가 많이 복잡할때 파이썬의 경우 시간초과가 날 수도 있어서 최대한 깔끔한 로직으로 생각해보고싶다.  

`내가 짠 코드`
```python
def find_selfnum():
        dn = []
        dn.append(0)
        for i in range(0, 10000): 
            dn.append(0)
        for i in range(1, 10001):
            num = i
            a = []
            j = 0
            while True:
                if num == 0: break
                a.append(num%10)
                num = num//10
            if (i+sum(a)) > 10000:
                continue
            dn[i+sum(a)] = i
            #print(dn)
        for i in range(1, 10000):           
            if dn[i] == 0: print(i)
                
find_selfnum()
```
반복문을 줄일 방법이 없나 고민을 하다 시간이 꽤 걸린 문제다. 답안을 제출한 뒤 내가 짠 코드보다 길이가 짧은 다른 사람의 코드도 확인해 보았다. 대부분 나보다 길이가 짧았다.

`다른 사람 코드-1`
```python
def Kaprekar_func(pnum):
    result = pnum
    for i in str(pnum):
        result += int(i)
    return result


initial_list = list(range(1, 10001))

for i in range(1,10001):
    after_kaprekar = Kaprekar_func(i)
    try:
        initial_list.remove(after_kaprekar)
    except ValueError:
        pass

for i in initial_list:
    print(i)
```
위 코드를 보면 각 자리수를 더하기 위해 pnum을 str처리해주었다.   
**각 자리수를 구할 땐 int->str 이용하기**
ㅋㅋ
나는 d(n)이 10000이 넘을 때 if문을 사용해서 인덱스 문제를 방지했는데 위 코드는 예외처리를 이용했다.  
그리고 1부터10000까지 들어있는 리스트에서 d(n)값을 제거하여 남아있는 값을 셀프넘버로 출력시켜주었다.  
코드가 훨씬 훨씬 간단하고 직관적이다.  

또 다른 코드를 보았는데
`다른 사람 코드-2`
```python
self_num = set(range(1,10001))
def d(n):
    for i in str(n):
        n += int(i)
    return n
exist_num = set(map(d,self_num))
for num in sorted(self_num-exist_num): print(num)
```
self_num변수에 1부터 10000까지 입력 후 map함수를 안에 d(self_num)을 호출했다.   
그러면 1~10000의 숫자가 차례로 d(n)이 계산되어 exist_num에 dict으로 들어간다.  
마지막 줄에서 1부터 10000까지의 숫자가 들어있는 self_num변수에서 d(n)이 들어있는 exist_num을 빼주어 정렬한 뒤 출력한다.  

오..  
근데 위와 같은 경우는 d함수를 10000번 호출하기 때문에 성능면에서 어떨지 모르겠다.  

내가 짠 코드가 길이는 좀 길었어도 시간이 다른 사람이 제출한것과 2배에서 10배까지 적게 걸렸다.  

이유를 생각해 보았는데 함수 호출을 최소화 했기 때문이라고 생각한다.  

하지만 내가 짠 코드의 치명적인 단점을 발견했다.  
문제에서는 1부터 10000까지의 숫자라고 한정지었지만 만약 범위가 바뀌면 함수 안의 모든 범위를 수정해야한다. 재사용성이 떨어지는 코드이기 때문에 숫자를 변수로 수정해주는 작업을 하면 성능과 속도를 잡을 수 있을 것 같다.  

`수정한 코드`
```python
def find_selfnum(start_num, end_num):
        dn = []
        dn.append(0)
        for i in range(0, end_num+1): 
            dn.append(0)
        for i in range(start_num, end_num+1):
            seed = i
            str_seed = str(seed)
            for j in range(len(str_seed)):
                    seed += int(str_seed[j])
            if (seed) > end_num:
                continue
            dn[seed] = i
        for i in range(start_num, end_num):           
            if dn[i] == 0: print(i)

s_num = 1
e_num = 10000
find_selfnum(s_num, e_num)
```
더 개선해야 할 사항이 남았겠지만 이 문제는 여기까지만 보고 set함수에 대해 복습해야겠다.

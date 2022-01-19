### 파이썬

- 귀도 반 로섬이 크리스마스 프로젝트로 새로운 언어를 직접만들기로 결심

  ### 1. 읽기 쉬어야 한다. --> 중괄호보다는 깔끔하게 인덴트로 처리한 공백으로 둘러쌈

  ### 2. 사용자가 원하는 모듈 패키지를 만들 수 있어야 했으며 다른프로그램에서 쓸 수 있어야하마. --> 이 방식은은 easy_install을 거쳐 pip를 통해 패키지 인덱스를 제공하는 형태로 완성

  ### 3. 약간 독특하고 신비한 이름원함 --> 영국의 코미디 그룹 몬티 파이썬

- 별칭 --> 실행가능한 수도코드
- 딥러닝의 물결과 인공지능 주도하는 표준 언어
- 파이썬 공식 인터프리터 CPython

### 파이썬 코드의 특징 1. 인덴트(indent)

- PEP 8에 따라 공백 4칸을 원칙으로 함
- pep(python enhancement proposals) --> PEP 프로세스는 새로운 기능을 제안하고 커뮤니티의 의견을 수렴하여 파이썬 디자인 결정을 문서화하는 파이썬 주요 개발 프로세스
- 공백 4칸 들여쓰기가 원칙(파이썬 답게 강제는 아님)

```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

```python
def long_function_name(
		var_one, var_two, var_three, # 첫 번째줄 파라미터 없다면 인덴트 한 번 더 해줌
    	var_four):
    print(val_one)
```

### 파이썬 코드의 특징 2. 네이밍 컨벤션(변수명 짓는법)

- 자바랑 다르게 각 단어를 밑줄(_)로 구분하여 표기하는 **Snake case**를 따른다.
- **최소한 직접 작성하는 코드는 소문자 변수명과 함수명을 기본으로 하자!**
- **파이썬은 파이썬다운 방식(Pythonic Way)에 자부심이 있음, 카멜 케이스뿐만 아니라 자바스타일 지양해야함**

```python
# 카멜 케이스
camelCase: int = 1 # 단어를 대소문자로 구분
# 스네이크 케이스 
snake_case: int =1 # 단어를 _로 이어줌
```

### 파이썬 코드의 특징 3. 타입 힌트(PEP484)

```python
a: str = "1"
b: int = 1
```

- 타입 힌트를 사용하여 명시적으로선언하게 되면 가독성이 좋아지며 버그 발생 확률을 줄일 수 있다.
- 문자열에 정수를 할당하는 등의 방식은 지양
- 타입힌트 확인하는 법 `$pip install mypy` 활용

### 파이썬 코드의 특징 4. 리스트 컴프리헨션

- 파이썬은 map, filter와 같은 함수형기능을 지원, 람다 표현식도 지원

```python
list(map(lambda x: x + 10, [1, 2, 3]))
# output --> [11, 12, 13]
```

- 파이썬은 1.0 버전 부터 람다를 지원
- 리스트 컴프리헨션은 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문(2.0부터 지원)
- map과 filter 대신 리스트컴프리헨션을 쓰는 것이 파이써닉함
- 2.7 버전부터를 리스트뿐만아니라 딕셔너리 등이 가능하게 추가됨

```python
a = {key: value for key, value in original.items()}
# 무리하게는 쓰지말자, 대체로 표현식은 2개를 넘지 않아야 함
```

### 파이썬 코드의 특징 5. 제너레이터(Generator)

- 2001년 2.2 버전 때 추가
- 루프의 반복 동작을 제어할 수 있는 루틴형태

```python
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
# yield 구문을 사용하면 제너레이터를 리턴할 수 있다.
# return처럼 중간값을 리턴하고 종료되지 않고, 계속해서 맨 끝에 도달할 때까지 실행된다.(while True 라서)
get_natural_number()
# output ==> <generator object get_natural_number at 0x10d3139d0>
```

```python
# 다음 값을 생성하려면 next()로 추출하면 된다.
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))
# output : 1 2 3 ... 98 99 100
```

```python
# 제너레이터는 다음과 같이 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
def generator():
    yield 1
    yield 'string'
    yield True
>> g = generator()
>> g
<generator object get_natural_number at 0x10d3139d0>
>> next(g)
1
>> next(g)
'string'
>> next(g)
True
```

### 파이썬 코드의 특징 6. range

```python
>>> list(range(5))
[0,1,2,3,4]
>>> range(5) # range 클래스를 return
range(0,5)
>>> type(range(5))
<class 'range'>
>>> for i in range(5): # for 문에서는 내부적으로 generator의 next()를 호출하듯 매번 다음 숫자 생성
    	print(i, end = ' ')
0 1 2 3 4
```

- 파이썬 2.x 에서는 **range()**[== list(range()) (3.x 버전의)]와 **xrange()**가 같이 존재했었음
- 생성조건만 정해두고 필요할 때 생성 --> 메모리 절약

```python
>>> a = [n for n in range(1000000)]
>>> b = range(1000000)
>>> len(a)
1000000
>>> len(b)
1000000
>>> len(a) == len(b)
True

>>> b
range(0, 1000000) # 생성해야 한다는 조건만 존재
>>> type(b)
<class 'range'>

>>> sys.getsizeof(a)
8697464
>>> sys.getsizeof(b) # 메모리 점유가 훨씬 적음 / 또한 인덱스 접근 시에는 바로 생성하도록 구현됨
48
```

### 파이썬 코드의 특징 7. enumerate

- 리스트, 튜플, 셋 등을 인덱스를 포함한 enumerate 객체로 리턴함

```python
>>> a = [1,2,3,2,45,2,5]
>>> a
[1, 2, 3, 2, 45, 2, 5]
>>> enumerate(a)
<enumerate object at 0x1010f83f2>
>>> list(enumerate(a))
[(0,1),(1,2),(2,3),(3,2),(4,45),(5,2),(6,5)]  # 인덱스를 자동으로 부여

a = ['a1', 'a2', 'a3']
for i in range(len(a)):
    print(i, a[i])
    
for i, v in enumerate(a):  # enumerate 사용이 가장 깔끔함
    print(i, v)
```

### 파이썬 코드의 특징 8. `//` 나눗셈 연산자

- 파이썬 2 이하에서 기본 나눗셈 연산자(`/`)는 타입을 유지했음 (ex 5 / 3 = 1)
- PEP238에서 변경이 제안됨 기존의 `/`가 `//`로 변경
- 정수형을 나눗셈할 때 정수형을 리턴하고 내림연산자의 역할을 함 ==> 몫을 구하는 연산자
- 나미지 연산자(모듈로 연산자) `%`  , 몫과 나머지 동시에 구하려면 `divmod()`함수를 사용

### 파이썬 코드의 특징 8. print

- 코딩테스트에서는 사실상 print가 유일한 디버깅임

```python
print('A1', 'B2')
print('A1', 'A2', sep=',')
print('aa',end=' ')
# 리스트를 출력할 때는 join()으로 묶어서 처리
a = ['A', 'B']
print(' ',join(a))
#
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit))
# 2: Apple
# 가장 선호하는 방법은 f-string(formated string literal)
# 변수를 뒤에 별로로 부여할 필요 없이 마치 템플릿을 사용하듯 인라인으로 삽입가능
# 간결, 직관 속도도 빠름 (3.6+ 지원)
print(f'{idx + 1}: {fruit})
# 2: Apple      
```

### 파이썬 코드의 특징 9. pass

- 코드의 전체 골격을 잡아 놓고 내부에서 처리할 내용을 차근차근 만들 때 사용함

```python
class MyClass(object):
    def method_a(self):
        # 여기에 pass 추가
        pass
    
    def method_b(self):
        print("Method B")

c = Myclass()
```

- pass는 Null 연산으로 아무것도 하지 않음 / 인덴트 오류 같은 불필요한 오류 방지 / 목업인터페이스 구현 후
  추후 구현 가능케 함

### 파이썬 코드의 특징 10. locals

- locals()는 로컬 심볼 테이블 딕셔너리를 가져오는 메소드, 업데이트 가능
- 로컬에 선언된 모든 변수를 조회할 수 있는 명령어이기 때문에 디버깅에 도움됨
- 잘못 선언한 부분이 없는지 확인

```python
import pprint
pprint.pprint(locals())
# pprint는 줄바꿈 해줌
# 결과값은 클래스 메소드 내부의 모든 로컬 변수를 출력해줌 -> 디버깅에 활용
```

### 코딩 스타일

- 참고할 만한 책 : -Clean Code / 프로그래밍 수련법
- PEP8 / 구글의 파이썬 스타일 가이드
- 가능한 한 많은 사람이 좋아하며 선호하는 방식을 택하는 것이 중요

### 변수명과 주석

- 간단한 주석을 부여하는 편이 훨씬 가독성이 높음
- 변수명도 의미있는 이름을 부여하자 / 스네이크 케이스
- 주석을 영어로 달자

### 리스트 컴프리헨션

- 너무 남발하지 말자
- 꼭 한 줄로 안해도됨
- 표현식 2개 넘지 말자

### 구글 파이썬 스타일 가이드

- 함수의 기본값으로 가변 객체 사용x(리스트, 딕셔너리)
- 불변객체 사용 None을 명시적으로 할당하는 것도 좋음
- True, False을 판별할 때는 암시적 방법이 더 간결함 (ex> if foo:)
- 최대 줄 길이는 80으로 하자

### 파이썬 철학

```python
# 아름다움이 추함보다 낫다
# 명시적인 것이 암시적인 것보다 낫다
# 단숨함이 복잡함보다 낫다
# 복잡함이 꼬인 것보다 낫다
# 수평이 계층보다 낫다
# 여유로운 것이 밀집된 것보다 낫다
# 가독성이 중요하다
# 특별한 경우라는 것은 규칙을 어겨야 할 정도로 특별한 것이 아니다
# 비록 실용성이 순수성에 우선하지만
# 에러 앞에서는 절대 침묵하지 말라
# 명시적으로 에러를 감추려는게 아니라면,
# 모호함을 앞에 두고 이를 유추하겠다는 유혹을 버려라 
# 문제를 풀어낼 -바람직 하고도 유일하며- 명확한 방법이 존재할 것이다.
```
































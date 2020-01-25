# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:32:33 2019

5장 본문의 모든 코드
@author: Kang Hwan Soo
"""
#%% 5장 1절

#%% 리스트 개념
menu = ['coffee', 'beverage', 'ade']
coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']
coffeeprice = [['에스프레소', 2500], ['아메리카노', 2800], ['카페라떼', 3200]]

#%%
menu = ['COFFEE', 'BEVERAGE', 'ADE']
menu
print(menu)

#%% 05-01coffeelist.py	다양한 커피 종류가 저장된 리스트
coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']
print(coffee)
print(type(coffee))

num = 0
for s in coffee:
    num += 1
    print('%d. %s' % (num, s))

#%% 05-02coffeemenu.py 간단한 커피 메뉴 만들기
menu = ['COFFEE', 'BEVERAGE', 'ADE']
coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']

print('=' * 45)
for category in menu:
    print('{:^15s}'.format(category), end=' ')
print()
print('=' * 45)

for ckind in coffee:
    print('{:^10s}'.format(ckind))    
    
#%% 빈 리스트 
pl = [] #빈 리스트
print(pl)

#%% 빈 리스트 play the rock-paper-scissors game
pl = list()
pl.append('C++')
pl.append('java')
print(pl)

#%% 05-03mart.py	리스트로 편의점에서 구입할 품목 목록 만들기
goods = []
for i in range(3): #i를 _로 가능
    item = input('구입할 품목은 ? ') 
    goods.append(item)
    print(goods)

print('길이: %d' % len(goods))

#%% 문자 리스트와 len
py = ['p', 'y', 't', 'h', 'o', 'n']
py
py = list('python')
py
len(py)

#%% 리스트 첨자 참조
py = list('python')
print(py[0], py[5])
print(py[-3], py[-1])
print(py[-len(py)], py[len(py)-1])

#%% 05-04langugelist.py	프로그래밍 언어 리스트에서 첨자로 항목 참조
pl = ['C', 'C++', 'Python', 'Java']
print(pl[0])
print(pl[2])
print()

for i in range(len(pl)):
    print(pl[i])

#%%
from random import choice
rsp = ['가위', '바위', '보']
print(choice(rsp))

#%% 05-05rockgame.py	가위 바위 보 리스트 항목 참조
rsp = ['가위', '바위', '보']
for i in range(len(rsp)):
    print(rsp[i], end=' ')
print()

from random import choice
print('컴퓨터의 가위바위보 5개')
for i in range(5):
    print(choice(rsp))

#%% 메소드 count(), index()
top = ['BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연', 'BTS']
top.count('BTS')
top.index('볼빨간사춘기')
top.index('BTS')
top.index('여자친구')

song = ['작은 것들을 위한 시', '나만 봄', '소우주', 'Kill This Love', '사계']

#%% 첨자 항목으로 항목 수정
top = ['BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연', 'BTS']
top[1] = '장범준' 
top[3] = '잔나비'
print(top)

#%% 05-06foodorder.py	중국집에서 음식 주문 하기
food = ['짜장면', '짬뽕', '우동', '울면']
print(food)
#탕수육 주문 추가 
food.append('탕수육')
print(food)
#짬뽕을 굴짬뽕으로 변경 주문 
food[1] = '굴짬뽕'
print(food)

#우동을 물만두로 변경 주문
food[food.index('우동')] = '물만두'
print(food)

#%% 일부 중첩된 리스트
animal = [['사자', '코끼리', '호랑이'], '조류', '어류']
print(animal)
print(animal[0])
print(animal[0][1])

#%% 05-07nestedanimallist.py	동물의 분류를 리스트로 처리 
animal = [['사자', '코끼리', '호랑이'], '조류', '어류']
print(animal)

for s in animal:
    print(s)
print()

bird = ['독수리', '참새', '까치']
fish = ['갈치', '붕어', '고등어']
animal[1:] = [bird, fish] 
print(animal)

for lst in animal:
    for item in lst:
        print(item, end = ' ')
    print() 
print()

#%% 심화학습: 일관성 있는 중첩된 리스트
books = [['파이썬 개론', ['강환수']],
         ['Perfect C', ['강환수', '이동규']],
         ['컴퓨터 개론', ['강환수', '조진형', '신용현']]]
print(books[0][0]) #첫 번째 책의 책이름 
print(books[1][1]) #두 번째 책의 저자 
print(books[1][1][1]) #두 번째 책의 두 번째 저자
print(books[2][1][2]) #세 번째 책의 세 번째 저자

#%% 심화학습: 일관성 있는 중첩된 리스트 출력
books = [['파이썬 개론', ['강환수']],
         ['Perfect C', ['강환수', '이동규']],
         ['컴퓨터 개론', ['강환수', '조진형', '신용현']]]

#책명과 저자 출력1
for b in books:
    print('책명: %s,' % b[0], end = ' ')
    print('저자:', b[1])
print()

#책명과 저자 출력2
for b in books:
    print('책명: %s,' % b[0], end = ' ')
    print('저자:', end = ' ')
    for author in b[1]:
        print(author, end = ' ')
    print() 
print()

#%% 중간점검 1, 05-chk01.py 
java = list('java')
print(type(java))
print(len(java))

numstr = '01234567890'
string = 'hellopython'
print(string[2:11:3])

#%% 중간점검 2, 05-chk02.py     
lst = [1, 3, 7, 9]
lst.index(5)

lst = [10, 30, 40, 50]
lst[:3] = 100

#%% 5장 2절

#%% sllicing
alp = list('abcdefghij')
print(alp)
len(alp)

print(alp[:]) 
print(alp[::])
print(alp[::-1])
print(alp[:]) 

#%% sllicing 순차
alp = list('abcdefghij')
print(alp[1:5]) 
print(alp[1:10:2]) 
 
#%% sllicing 역순
alp = list('abcdefghij')
print(alp[-2:-9:-1]) 
print(alp[-3::-2]) 

#%% sllicing 혼재
alp = list('abcdefghij')
print(alp[1:-1]) 
print(alp[-1:1:-1]) 
print(alp[-2:2:-2]) 

#%% 05-08swordslice.py	한 글자의 한국 단어로 이해하는 리스트 슬라이싱 
wlist = ['밥','삶','길','죽','꿈','차','떡','복','말']
print('wlist[:] = ', wlist[:])
print('wlist[::] = ', wlist[::])
print('wlist[::-1] = ', wlist[::-1])
#오름차순
print(wlist[::3])
print(wlist[1::3])
print(wlist[2::3])
#내림차순
print(wlist[::-2])
print(wlist[-1:-8:-3])
#오름과 내림차순의 혼재
print(wlist[1:-1:])
print(wlist[-2:-9:-3])

#wlist = list('밥삶길죽꿈차떡복말')

#%% 슬라이스로 일부분 수정
sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
sports[0:3] = ['축구']
print(sports)

#%%
sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
sports[0:3] = '축구'
print(sports)

#%% 정수 항목으로 점검 
t = [1, 2, 3, 4, 5, 6]
t[1:3] = [30, 40]
t
t[1:3] = 30

#%% 항목에 리스트 저장
sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
sports[5] = ['핸드볼']
print(sports)

#%% 슬라이스에 슬라이스 대입 1
sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
sports[1:3] = sports[4:6]
print(sports)

#%% 슬라이스에 슬라이스 대입 2
sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
others = ['축구', '미식축구', '골프']
sports[1:4] = others[:2]
print(sports)

#%%리스트의 항목 삽입
kpop = []
kpop.insert(0, '블랙핑크')
kpop.insert(0, 'BTS')
kpop
kpop.insert(1, '장범준')
kpop

#%%리스트의 항목 삭제 remove()
kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
kpop.remove('장범준')
print(kpop)    

kpop.remove('장준')
if '장준' in kpop:
    kpop.remove('장준')
print(kpop)    

#%% 리스트의 항목 삭제 pop()
kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
print(kpop.pop(1))
print(kpop.pop())
print(kpop)

#%% 리스트의 항목 또는 자체 삭제 del 
kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
del kpop[0] #del(kpop[0])도 가능
print(kpop)

kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
del kpop[0:2]
print(kpop)

kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
del kpop
print(kpop)

#%% 리스트의 항목 모두 제거하는 clear() 메소드 
kpop = ['BTS', '장범준', '블랙핑크', '잔나비']
kpop.clear()
print(kpop)

#%% 05-09iteminsertremove.py	학용품 리스트의 항목 삽입과 삭제 
item = ['연필', '볼펜']
#현재 학용품 품목 출력
print(item)

#연필 1개와 볼펜 3자루 삽입
item.insert(1, 2)
item.insert(3, 3)
#맨 뒤에 지우개, 1개를 삽입
item.insert(4, '지우개')
item.insert(5, 1)
#현재 학용품 품목 출력
print(item)

#연필 2자루 삭제
print(item.pop(1)) #첨자 1 항목 삭제
item.remove('연필') #연필 삭제
del item[2:] #지우개와 수 품목 삭제

#현재 학용품 품목 출력
print(item)

#%% 리스트의 추가
day = ['월', '화', '수']
day2 = ['목', '금', '토', '일']
day.extend(day2) 
print(day)

#%% 리스트의 연결
korean = ['불고기', '설렁탕']
chinese = ['탕수육', '기스면']
food = korean + chinese
print(food)

#%% 리스트의 연결과 반복
days = ['월', '화']
print(days * 3)

#%% 
one = '잣밤배귤감'
wlist = list(one)
print(wlist)
wlist.reverse()
print(wlist)

#%% 
one = '잣밤배귤감'
wlist = list(one)
wlist.sort()
print(wlist)
wlist.sort(reverse=True)
print(wlist)

#%% 
fruit = ['사과', '귤', '복숭아', '파인애플']
s_fruit = sorted(fruit)
print(s_fruit)
print(fruit)

rs_fruit = sorted(fruit, reverse=True)
print(rs_fruit)

#%% 05-10wordsort.py	한 글자 단어와 과일의 정렬
word = list('삶꿈정')
word.extend('복빛')
print(word)
word.sort()
print(word)
 
fruit = ['복숭아', '자두', '골드키위', '귤']
print(fruit)
fruit.sort(reverse=True)
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))
    
#%% 리스트 컴프리헨션 이전
even = []
for i in range(2, 11, 2):
    even.append(i)
print(even)

#%% 리스트 컴프리헨션
even = [i for i in range(2, 11, 2)]
print(even)
      
#%%
odd = []
for i in range(10):
    if i%2 == 1:
        odd.append(i)
print(odd)

odd = [i for i in range(10) if i%2 == 1]
print(odd)

#%% 컴프리헨션 공식
리스트 = []
for 항목 in 시퀀스:
    if 조건식:
        리스트.append(항목연산식)
    
리스트 = [항목연산식 for 항목 in 시퀀스 if 조건식]

#%% 05-11listcomprehension.py	다양한 리스트 컴프리헨션
#for 문으로 리스트 생성
a = []
for i in range(10):
    a.append(i) 
print(a)

#컴프리헨션으로 리스트 생성
seq = [i for i in range(10)]
print(seq)

#for 문으로 리스트 생성
s = []
for i in range(10):
    if i%2 == 1:
        s.append(i**2) 
print(s)

#컴프리헨션으로 리스트 생성
squares = [i**2 for i in range(10) if i%2 == 1]
print(squares)

#%% 동일 리스트의 공유
f1 = ['사과', '귤', '복숭아', '파인애플']
f2 = f1
f2.pop()
print(f1)
print(f2)

#%% 슬라이스로 리스트 복사
f1 = ['사과', '귤', '복숭아', '파인애플']
f2 = f1[:]
f2.pop(1)
print(f1, f2)

#%% copy()로 리스트 복사
f1 = ['사과', '귤', '복숭아', '파인애플']
f3 = f1.copy()
f3.pop()
print(f1, f3)

#%% 함수 list()로 리스트 복사
f1 = ['사과', '귤', '복숭아', '파인애플']
f4 = list(f1)
f4.append('감')
print(f1, f4)

#%% 동일 객체 검사 is
f1 = ['사과', '귤', '복숭아', '파인애플']
f2 = f1
print(f1 is f2)
f3 = f1[:]
print(f1 is f3)

#%% 중간점검 3, 05-chk03.py 
lst = [1, 5]
lst[0] = 3
lst.append(7)
lst[1:3] = [10]
print(lst)

lst = [1, 5, 1, 7, 1]
lst[lst.count(1)] = 70
lst[len(lst)-1] = 80
lst.insert(1, 50)
print(lst)

#%% 중간점검 4, 04-chk04.py 
squares = [x**2 for x in range(1, 11, 2)]
print(squares)

#%% 5장 3절

#%% 튜플 샘플
singer = ('BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연')
credit = ([2020, 1, 18], [2020, 2, 17])
space = '밤', '낮', '해', '달'

type(singer)    
type(credit)    
type(space)
    
#%% 빈 튜플 생성
empty1 = ()
type(empty1)
print(empty1)
empty2 = tuple()
print(empty1)
    
#%% 튜플 기초
credit = (16, 17)
credit = 16, 17
print(credit)

inta = 1
tupa = 1,
print(tupa)
    
#%%
nation = '대한민국', '뉴질랜드', '캐나다'
city = ('부산', '웰링톤', '몬트리올')
nation[1]
city[1:3]

city[2] = '오타와' #오류

for _ in range(len(nation)):
    print('%s: %s' % (nation[_], city[_]))

#%% 05-12kpoptuple.py	K-pop 가수와 곡으로 구성된 튜플의 참조
singer = ('BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연')
song = ('작은 것들을 위한 시', '나만, 봄', '소우주', 'Kill This Love', '사계')
print(singer)
print(song)

print(singer.count('BTS'))
print(singer.index('볼빨간사춘기'))
print(singer.index('BTS'))
print()

for _ in range(len(singer)):
    print('%s: %s' % (singer[_], song[_]))

#%% mutable vs immutable
#str is immutable
p = 'python'
y = 'python'
print(id(p), id(y))
print(p is y)
p[0] ='P' #수정 불가능, 오류 발생

#%%tuple is immutable
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(id(tup2), id(tup2))
print(tup1 is tup2)
tup1[0] = 10 #수정 불가능

#%%list is mutable
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2)
print(id(lst1), id(lst2))
print(lst1 is lst2)
lst1[0] = 10 #수정 가능
print(lst1)

#%% 퓨플 연결 + 연산자와 반복 * 연산자
kpop = ('BTS', '블랙핑크')
num = (7, 4)
print(kpop + num)

days = ('1학기', '2학기')
print(days * 4)

#%% 	튜플 항목의 순서를 정렬한 리스트를 반환하는 내장 함수 sorted()
fruit = ('사과', '귤', '복숭아', '파인애플')
tup = sorted(fruit)
print(type(tup), tup)

print(sorted(fruit, reverse=True))
print(fruit)

#%%
kpop = ('BTS', '장범준', '블랙핑크', '잔나비')
del kpop
print(kpop)

#%% 05-13daytuple.py	영어 요일 단어로 구성된 튜플 만들기
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday')
# ('sunday')로 하면 튜플이 아니고 문자열 
day3 = ('sunday', ) 

day = day1 + day2 + day3
print(type(day))
print(day)

day = day1 + day2 + day3 * 3
print(day)

#%% 중간점검 5, 05-chk05.py 
a = 1
print(type(a))
b = 1,
print(type(b))

#%% 중간점검 6, 05-chk06.py 
print(sorted((5, 4, 1)))
print(sorted((5, 4, 1), reverse=True))
    
#%% 프로젝트 Lab

#%% 프로젝트 Lab1 05-pl01-sportsnumber.py 
sports = ['축구', '야구', '농구', '배구']
#위 종목에 대응하는 팀원 수를 항목으로 구성 
num = [11, 9, 5, 6]
print(sports)
print(num)
#위 두 리스트로 출력
for i in range(len(sports)):
    print('%s: %d명 ' % (sports[i], num[i]), end = ' ')
print(); print()

#2차원 리스트로 생성
sponum = [sports, num]
print(sponum)
#2차원 리스트에서 출력
for i in range(len(sponum[0])):
    print('%s: %d명 ' % (sponum[0][i], sponum[1][i]), end = ' ')
print(); print()

#다른 구조의 2차원 리스트 생성을 컴프리헨션으로 처리
psponum = [[sports[i], num[i]] for i in range(len(sports))]
print(psponum)
#위 리스트에서 출력
for one in psponum:
    print('%s: %d명 ' % (one[0], one[1]), end = ' ')
print()

#%% 프로젝트 Lab2 05-pl02-priceburgerorder.py 햄버거 주문받아 주문 가격 표시 난이도: 실전
menu = ('주문종료', '올인원팩', '투게더팩', '트리오팩', '패밀리팩')
price = (0, 6000, 7000, 8000, 10000)
       
#주문에 필요한 메시지 만들기
msg = '주문할 콤보 번호와 수량을 계속해서 입력하세요!'
for i in range(len(menu)):
    msg += '\n\t %d %s' % (i, menu[i])
    if i != 0:
        msg +=  ' %5d 원' % (price[i])
msg += '\n >> '
        
more = True
total = 0

while more:
    instr = input(msg)
    if instr.count(' ') > 0: #두 개의 입력 인지를 검사 
        #입력이 2개이면 분리하여 각각 입력
        order, cnt = instr.split()
        cnt = int(cnt)
    else:
        #입력이 1개이면 주문 번호 입력
        order = instr
    order = int(order)
    if order == 0:
        print()
        print(' 주문종료 '.center(20, '*'))
        more = False
    elif 1 <= order <= 4:
        print('%s, %d개 주문' % (menu[order], cnt))
        sub = price[order] * cnt 
        total += sub
        print('%s 주문가격 %d, 총 가격 %d' % (menu[order], sub, total))
    else:
        print('모르겠어요. 다시 주문하세요!')
        
else:
    print('총 주문가격 %d 원' % total)
    print('주문을 마치겠습니다.')
    print(' 안녕! '.center(20, '='))
        
#%% end of file


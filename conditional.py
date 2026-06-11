# age=int(input('age'))
# if age<8:
#     print('미취학 아동입니다.')
#     print('많이 놀아야되요')
# elif age<14:
#     print('초등학생입니다.')
# else:
#     print('중학생 이상입니다.')

# print("짝수와 홀수를 알려 줘요")
# num=int(input('숫자를 입력하세요:'))
# div=num%2
# if div==0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')

# print(" 공배수를 알려 줘요")
# num1=int(input('첫 번째 숫자를 입력하세요:'))
# num2=int(input('두 번째 숫자를 입력하세요:'))
# num3=int(input('세 번째 숫자를 입력하세요:'))
# div1=num3%num1==0
# div2=num3%num2==0
# if div1 and div2:
#     print('공배수입니다.')
# else:
#     print('공배수가 아닙니다.')
# print(eval('2*3'))

# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# op=input('+, -, *, / 중 하나를 입력하세요:')
# if op=='+':
#     print(num1,op,num2,'=',num1+num2)
#     print('%d %s %d = %d' %(num1, op, num2, num1+num2))
#     print(f'{num1} {op} {num2} = {num1+num2}')

# import random
# cnt = 0
# for i in range(5):
#     num1=random.randint(1, 15)
#     num2=random.randint(5,20)
#     op=random.choice(['+','-','*'])
#     ex= str(num1) + op + str(num2)
#     print(ex)
#     answer=input('=')
#     if int(answer)== eval(ex):
#         print('맞췄습니다')
#     else:       
#         print('틀렸습니다')
#         cnt = cnt+1
# if cnt==0:
#     print('당신은 천재~~')
# import random
# ai= random.randint(1,100)
# cnt=0
# while True:
#     guess = int(input('guess:'))
#     cnt += 1
#     if guess==ai:
#         print('congratulations')
#         print(cnt,'번 만에 맞췄어')
#         break
#     elif guess<ai:
#         print('up')
#         continue
#     elif guess>ai:
#         print('down')
        

# sum=0
# for i in range(1, 1000+1):
#     sum=sum+i
# print(" 1부터 1000까지의 합 : %d"% sum)
# i=1
# while i<5:
#     print("%d층입니다."%i)
#     i=i+1

# for i in range(1,11):
#     if i%3==0:
#         continue
#     print

def total(a,b):
    c=a+b
    return c
print(total(1,2))

#하노이 탑 이동순서

k = int(input())

stack1=[]
stack2=[]
stack3 =[]

n = int(input())
#이게 어떻게 재귀...???
def hanoi(stack1,stack2,stack3):
    if len(stack1) == 0 and len(stack2)== n:
        
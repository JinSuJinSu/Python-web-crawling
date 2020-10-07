
from tkinter import*

root = Tk()
root.title("Calculator")
#root.geometry("640x480")#가로x세로 크기로 조정
root.geometry("640x480+500+200")#가로x세로 + x좌표 +y좌표


#계산기 기능을 위한 변수
num_input = StringVar()
expression = ''
# 버튼 기능 넣기
def btn_click(num):
    global expression
    expression = expression + str(num)
    num_input.set(expression)


# Clear 기능 넣기
def num_init():
    pass

# 나누기 기능 넣기
def num_div():
    pass

# 곱하기 기능 넣기
def num_mul():
    pass

# 더하기 기능 넣기
def num_plu():
    pass

# 빼기 기능 넣기
def num_sub():
    pass


# 계산된 숫자가 쓰일 화면을 만든다.
screen_width = Entry(root, width=20, textvariable = num_input)
screen_width.grid(row = 0, columnspan = 4, sticky = N+E+W+S, padx = 3, pady = 3, ipady = 5)

#맨 윗줄부터 차례대로 계산기에 들어가는 버튼들을 추가해준다.

#1번째 줄
btn_left_parentheses= Button(root, text = '(', width =5, height =2, command=lambda:btn_click('('))
btn_right_parentheses= Button(root, text = ')', width =5, height =2, command=lambda:btn_click(')'))
btn_percent= Button(root, text = '%', width =5, height =2, command=lambda:btn_click('%'))
btn_AC= Button(root, text = 'Clear', width =5, height =2, command = num_init)


btn_left_parentheses.grid(row = 1, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_right_parentheses.grid(row = 1, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_percent.grid(row = 1, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_AC.grid(row = 1, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)


#2번째 줄
btn_7= Button(root, text = '7', width =5, height =2, command=lambda:btn_click(7))
btn_8= Button(root, text = '8', width =5, height =2, command=lambda:btn_click(8))
btn_9= Button(root, text = '9', width =5, height =2, command=lambda:btn_click(9))
btn_division= Button(root, text = '/', width =5, height =2, command = num_div)

btn_7.grid(row = 2, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_8.grid(row = 2, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_9.grid(row = 2, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_division.grid(row = 2, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)


#3번째 줄
btn_4= Button(root, text = '4', width =5, height =2, command=lambda:btn_click(4))
btn_5= Button(root, text = '5', width =5, height =2, command=lambda:btn_click(5))
btn_6= Button(root, text = '6', width =5, height =2, command=lambda:btn_click(6))
btn_multiplication= Button(root, text = 'x', width =5, height =2, command = num_mul)

btn_4.grid(row = 3, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_5.grid(row = 3, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_6.grid(row = 3, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_multiplication.grid(row = 3, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

#4번째 줄
btn_1= Button(root, text = '1', width =5, height =2, command=lambda:btn_click(1))
btn_2= Button(root, text = '2', width =5, height =2, command=lambda:btn_click(2))
btn_3= Button(root, text = '3', width =5, height =2, command=lambda:btn_click(3))
btn_subtraction= Button(root, text = '-', width =5, height =2, command = num_sub)

btn_1.grid(row = 4, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_2.grid(row = 4, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_3.grid(row = 4, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_subtraction.grid(row = 4, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

#5번째 줄
btn_0= Button(root, text = '0', width =5, height =2, command=lambda:btn_click(0))
btn_dot= Button(root, text = '.', width =5, height =2, command=lambda:btn_click('.'))
btn_equal= Button(root, text = '=', width =5, height =2)
btn_plus= Button(root, text = '+', width =5, height =2, command = num_plu)

btn_0.grid(row = 5, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_dot.grid(row = 5, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_equal.grid(row = 5, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_plus.grid(row = 5, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)




root.mainloop()
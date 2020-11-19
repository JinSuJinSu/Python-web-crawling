
from tkinter import*

root = Tk()
root.title("Calculator")
#root.geometry("640x480")#가로x세로 크기로 조정
root.geometry("640x480+500+200")#가로x세로 + x좌표 +y좌표


#계산기 화면에 입력될 변수
btn_input = StringVar()


#계산기 화면 생성
calculator_screen = Entry(root, width=20, bd = 2, textvariable = btn_input)
calculator_screen.grid(row = 0, columnspan = 4, sticky = N+E+W+S, padx = 3, pady = 3, ipady = 5)

#계산기 버튼들 생성
#1. 1번째 줄
btn_clear= Button(root, text = 'Clear', width =5, height =2, command =lambda:btn_clear())
btn_clear.grid(row = 1, columnspan = 4, sticky = N+E+W+S, padx = 3, pady = 3)


#2. 2번째 줄
btn_7= Button(root, text = '7', width =5, height =2, command=lambda:btn_click(7))
btn_8= Button(root, text = '8', width =5, height =2, command=lambda:btn_click(8))
btn_9= Button(root, text = '9', width =5, height =2, command=lambda:btn_click(9))
btn_division= Button(root, text = '/', width =5, height =2, command=lambda:btn_div())

btn_7.grid(row = 2, column = 0, padx = 3, pady = 3)
btn_8.grid(row = 2, column = 1, padx = 3, pady = 3)
btn_9.grid(row = 2, column = 2, padx = 3, pady = 3)
btn_division.grid(row = 2, column = 3, padx = 3, pady = 3)


#3. 3번째 줄
btn_4= Button(root, text = '4', width =5, height =2, command=lambda:btn_click(4))
btn_5= Button(root, text = '5', width =5, height =2, command=lambda:btn_click(5))
btn_6= Button(root, text = '6', width =5, height =2, command=lambda:btn_click(6))
btn_multiplication= Button(root, text = '*', width =5, height =2, command=lambda:btn_mul())

btn_4.grid(row = 3, column = 0, padx = 3, pady = 3)
btn_5.grid(row = 3, column = 1, padx = 3, pady = 3)
btn_6.grid(row = 3, column = 2, padx = 3, pady = 3)
btn_multiplication.grid(row = 3, column = 3, padx = 3, pady = 3)

#4. 4번째 줄
btn_1= Button(root, text = '1', width =5, height =2, command=lambda:btn_click(1))
btn_2= Button(root, text = '2', width =5, height =2, command=lambda:btn_click(2))
btn_3= Button(root, text = '3', width =5, height =2, command=lambda:btn_click(3))
btn_subtraction= Button(root, text = '-', width =5, height =2, command=lambda:btn_sub())
btn_1.grid(row = 4, column = 0, padx = 3, pady = 3)
btn_2.grid(row = 4, column = 1, padx = 3, pady = 3)
btn_3.grid(row = 4, column = 2, padx = 3, pady = 3)
btn_subtraction.grid(row = 4, column = 3, padx = 3, pady = 3)

#5. 5번째 줄
btn_0= Button(root, text = '0', width =5, height =2, command=lambda:btn_click(0))
btn_dot= Button(root, text = '.', width =5, height =2, command=lambda:btn_click('.'))
btn_equal= Button(root, text = '=', width =5, height =2, command=lambda:btn_equal())
btn_addition= Button(root, text = '+', width =5, height =2, command=lambda:btn_add())

btn_0.grid(row = 5, column = 0, padx = 3, pady = 3)
btn_dot.grid(row = 5, column = 1, padx = 3, pady = 3)
btn_equal.grid(row = 5, column = 2, padx = 3, pady = 3)
btn_addition.grid(row = 5, column = 3, padx = 3, pady = 3)

# 계산기에 필요한 기능들

#1. 클릭 기능
def btn_click(btn):
    current = calculator_screen.get()
    calculator_screen.delete(0,END)
    calculator_screen.insert(0, current + str(btn))


#2. 초기화 기능
def btn_clear():
    calculator_screen.delete(0, END)


#3. 더하기 기능
def btn_add():
    first_number = calculator_screen.get()
    global first_num
    global calculation
    calculation = 'addition'
    first_num = int(first_number)
    calculator_screen.delete(0,END)


#4. 빼기 기능
def btn_sub():
    first_number = calculator_screen.get()
    global first_num
    global calculation
    calculation = 'subtraction'
    first_num = int(first_number)
    calculator_screen.delete(0,END)


#5. 곱하기 기능
def btn_mul():
    first_number = calculator_screen.get()
    global first_num
    global calculation
    calculation = 'multiplication'
    first_num = int(first_number)
    calculator_screen.delete(0,END)


#6. 나누기 기능
def btn_div():
    first_number = calculator_screen.get()
    global first_num
    global calculation
    calculation = 'divsiion'
    first_num = int(first_number)
    calculator_screen.delete(0,END)


#7. 계산 결과 기능
def btn_equal():
    second_number = calculator_screen.get()
    calculator_screen.delete(0,END)

    if calculation == 'addition':
        calculator_screen.insert(0,first_num + int(second_number))

    elif calculation == 'subtraction':
        calculator_screen.insert(0,first_num - int(second_number))

    elif calculation == 'multiplication':
        calculator_screen.insert(0,first_num * int(second_number))

    elif calculation == 'divsiion':
        calculator_screen.insert(0,first_num / int(second_number))

    else:
        pass



root.mainloop()


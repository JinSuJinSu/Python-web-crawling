
from tkinter import*

root = Tk()
root.title("Calculator")
#root.geometry("640x480")#가로x세로 크기로 조정
root.geometry("640x480+500+200")#가로x세로 + x좌표 +y좌표


#계산기 화면에 입력될 변수
btn_input = StringVar()

#계산기 화면 생성
caculator_screen = Entry(root, width  = 20, bd = 2, textvariable = btn_input)
caculator_screen.grid(row=0, columnspan = 4, sticky = N+E+W+S, padx = 3, pady= 3, ipady = 5)



#계산기 버튼들 생성
#1. 1번째 줄
btn_clear = Button(root, text = 'Clear', width = 5, height = 2, command =lambda:btn_clear())
btn_clear.grid(row=1, columnspan = 4, sticky = N+E+W+S, padx = 3, pady= 3)

# 계산기 단일 버튼 클래스 생성
class CreateButton:
    def __init__(self, button, v1, v2, function, v3,v4, v5,v6):
        self.button = button
        self.v1 = v1
        self.v2 = v2
        self.function = function
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        result = Button(root, text = button, width = v1, height = v2, command = function)
        result.grid(row=v3, column = v4, padx = v5, pady = v6)




#2. 2번째 줄
btn_7 = CreateButton('7',5,2,lambda:btn_click(7),2,0,3,3)
btn_8 = CreateButton('8',5,2,lambda:btn_click(8),2,1,3,3)
btn_9 = CreateButton('9',5,2,lambda:btn_click(9),2,2,3,3)
btn_division = CreateButton('/',5,2,lambda:btn_div(),2,3,3,3)



#3. 3번째 줄
btn_4 = CreateButton('4',5,2,lambda:btn_click(4),3,0,3,3)
btn_5 = CreateButton('5',5,2,lambda:btn_click(5),3,1,3,3)
btn_6 = CreateButton('6',5,2,lambda:btn_click(6),3,2,3,3)
btn_multiplication = CreateButton('*',5,2,lambda:btn_mul(),3,3,3,3)



#4. 4번째 줄
btn_1 = CreateButton('1',5,2,lambda:btn_click(1),4,0,3,3)
btn_2 = CreateButton('2',5,2,lambda:btn_click(2),4,1,3,3)
btn_3 = CreateButton('3',5,2,lambda:btn_click(3),4,2,3,3)
btn_subtraction = CreateButton('-',5,2,lambda:btn_sub(),4,3,3,3)



#5. 5번째 줄
btn_0 = CreateButton('0',5,2,lambda:btn_click(0),5,0,3,3)
btn_dot = CreateButton('.',5,2,lambda:btn_click('.'),5,1,3,3)
btn_eqaul = CreateButton('=',5,2,lambda:btn_equal(),5,2,3,3)
btn_addition = CreateButton('+',5,2,lambda:btn_add(),5,3,3,3)




# 계산기 기능들

#1. 클릭 기능

def btn_click(btn):
    current = caculator_screen.get()
    caculator_screen.delete(0,END)
    caculator_screen.insert(0, current + str(btn))



#2. 초기화 기능
def btn_clear():
    caculator_screen.delete(0,END)



#3. 더하기 기능

def btn_add():
    global first_number
    global calculation
    first_number = float(caculator_screen.get())
    calculation = 'addition'
    caculator_screen.delete(0,END)


#4. 빼기 기능
def btn_sub():
    global first_number
    global calculation
    first_number = float(caculator_screen.get())
    calculation = 'subtraction'
    caculator_screen.delete(0,END)



#5. 곱하기 기능
def btn_mul():
    global first_number
    global calculation
    first_number = float(caculator_screen.get())
    calculation = 'multiplication'
    caculator_screen.delete(0,END)



#6. 나누기 기능
def btn_div():
    global first_number
    global calculation
    first_number = float(caculator_screen.get())
    calculation = 'division'
    caculator_screen.delete(0,END)


#7. 계산 결과 기능
def btn_equal():
    second_number = float(caculator_screen.get())
    caculator_screen.delete(0,END)

    if calculation == 'addition':
        caculator_screen.insert(0, round((first_number + second_number),2))
    elif calculation == 'subtraction':
        caculator_screen.insert(0, round((first_number - second_number),2))
    elif calculation == 'multiplication':
        caculator_screen.insert(0, round((first_number * second_number),2))
    elif calculation == 'division':
        caculator_screen.insert(0, round((first_number / second_number),2))
    else:
        pass





root.mainloop()


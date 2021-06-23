import tkinter as tk

exp = ""

app = tk.Tk()
app.title('Basic Arithmetic')
app.geometry('500x400')


def finalans():
    global exp
    result.set(eval(exp))
    exp=""

def cs():
    global exp
    exp=""
    result.set(exp)

def onPress(num):
    global exp
    exp = exp+str(num)
    result.set(exp)
    


result = tk.Variable(app)
tk.Entry(app,textvariable=result,width=75).place(x=20,y=20)


tk.Button(app,text='7',width = 5,height=2, command=lambda: onPress(7)).place(x=30,y=50)
tk.Button(app,text='8',width = 5,height=2, command=lambda: onPress(8)).place(x=80,y=50)
tk.Button(app,text='9',width = 5,height=2, command=lambda: onPress(9)).place(x=130,y=50)
tk.Button(app,text='/',width = 5,height=2, command=lambda: onPress("/")).place(x=180,y=50)

tk.Button(app,text='4',width = 5,height=2, command=lambda: onPress(4)).place(x=30,y=120)
tk.Button(app,text='5',width = 5,height=2, command=lambda: onPress(5)).place(x=80,y=120)
tk.Button(app,text='6',width = 5,height=2, command=lambda: onPress(6)).place(x=130,y=120)
tk.Button(app,text='*',width = 5,height=2, command=lambda: onPress("*")).place(x=180,y=120)

tk.Button(app,text='1',width = 5,height=2, command=lambda: onPress(1)).place(x=30,y=190)
tk.Button(app,text='2',width = 5,height=2, command=lambda: onPress(2)).place(x=80,y=190)
tk.Button(app,text='3',width = 5,height=2, command=lambda: onPress(3)).place(x=130,y=190)
tk.Button(app,text='-',width = 5,height=2, command=lambda: onPress("-")).place(x=180,y=190)

tk.Button(app,text='C',width = 5,height=2, command=lambda: cs()).place(x=30,y=260)
tk.Button(app,text='0',width = 5,height=2, command=lambda: onPress(0)).place(x=80,y=260)
tk.Button(app,text='=',width = 5,height=2, command=lambda: finalans()).place(x=130,y=260)
tk.Button(app,text='+',width = 5,height=2, command=lambda: onPress("+")).place(x=180,y=260)




app.mainloop()




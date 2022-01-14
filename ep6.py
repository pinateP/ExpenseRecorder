# ep6.py

from tkinter import *
from tkinter import ttk,messagebox # ttk is theme of tk
from datetime import datetime
import csv

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่ายรายวัน by Pinet')
GUI.geometry('600x600+50+50')

# B1 = Button(GUI,text='Hello1')
# B1.pack(ipadx=25,ipady=10) #.pack() เป็นการติดปุ่มเข้ากับ GUI หลัก
                             # ipadx ทำให้ขนาดตามแนว x ขยายขนาด
# F1 = LabelFrame(GUI,text='ปุ่ม test')

############## Menu Bar ###################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='ไฟล์',menu = filemenu)
filemenu.add_command(label='บันทึก')
filemenu.add_command(label='ออก')
# Help menu
def About():
    messagebox.showinfo('About','Design By Pinet')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='ช่วยเหลือ',menu = helpmenu)
helpmenu.add_command(label='About',command = About)
# Donate menu
def Donate():
    messagebox.showinfo('Donate','BTC Address: 1234567')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='บริจาค',menu = donatemenu)
donatemenu.add_command(label='Donate',command = Donate)


###########################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='money-wallet-icon.png')
icon_t2 = PhotoImage(file='list-icon.png')


Tab.add(T1,text=f'{"เพิ่มค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')



F1 = Frame(T1)
#F1.place(x=150,y=50)
F1.pack()
days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัส',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}
        


def Save(event=None):
    expense = v_expense.get() #.get คือการดึงค่ามาจาก v_expense = StringVar()
    price = v_price.get()
    quantity = v_quantity.get()
    if expense == "" :
        messagebox.showerror('Error','กรุณากรอกข้อมูลรายการค่าใช้จ่าย')
        v_expense.set('')
        E1.focus()
        return
    elif price == "" :
        messagebox.showerror('Error','กรุณากรอกข้อมูลราคา')
        v_price.set('')
        E2.focus()
        return
    elif quantity == "" :
        messagebox.showerror('Error','กรุณากรอกข้อมูลจำนวน')
        v_quantity.set('')
        E3.focus()
        return
    
    try:
        total = float(price) * float(quantity)  
        today = datetime.now().strftime('%a')
        dt = datetime.now().strftime('{}-%d-%b-%Y %H:%M'.format(days[today]))
        print(f'รายการ: {expense},ราคา: {price},จำนวน: {quantity}')
        print (f'รวมทั้งหมด: {total},เวลาบันทึก: {dt}')
        text = 'รายการ: {} ราคาต่อหน่วย: {} บาท\nจำนวน: {} units รวมทั้งหมด: {} บาท'.format(expense,price,quantity,total)
        v_result.set(text)

        # clear ข้อมูลเก่า โดยการ
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
        # บันทึกข้อมูลลง csv
        with open ('savedata.csv','a',encoding='utf-8',newline='')as f:
            # with คือ สั่งเปิดและปิด file automatic
            # 'a' คือ append เพิ่มเข้าไปต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f)# เป็นการสร้างฟังก์ชั่นสำหรับเขียนข้อมูลลงไป
            data = [dt,expense,price,quantity,total]
            fw.writerow(data)
            # การทำให้ cursor กลับไปที่ตำแหน่งช่องกรอกบนสุด E1
        E1.focus()
        update_table()

    except Exception as e:
        print(e)
        # messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        # messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

# การทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event=None) ด้วย        
        
        
        
FONT1 = (None,20) # None อาจเปลี่ยนเป็น 'Angsana new' ก็ได้
                  # อันนี้เปลี่ยนแต่ขนาด

#----------Image------------------
main_icon = PhotoImage(file='Ecommerce-Cash-Register-icon.png')
Mainicon = Label(F1,image=main_icon)
Mainicon.pack()

#----------text1---------------------------------------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar() #StringVar() เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#------------------------------------------------------

#----------text2---------------------------------------
L = ttk.Label(F1,text='ราคา(บาท)',font=FONT1).pack()
v_price = StringVar() #StringVar() เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#------------------------------------------------------
#----------text3---------------------------------------
L = ttk.Label(F1,text='จำนวน(units)',font=FONT1).pack()
v_quantity = StringVar() #StringVar() เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#------------------------------------------------------
icon_b1 = PhotoImage(file='Save-icon.png')

B2 = ttk.Button(F1,text=f'{"บันทึก" : >{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=10,pady = 15)

v_result = StringVar()
v_result.set('------------Result------------')
result = ttk.Label(F1,textvariable=v_result,font = FONT1,foreground='blue')
result.pack(pady = 10)

##############TAB2#######################
def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f) # fr คือ ตัวแปร อ่านว่า fileReader
        data = list(fr)
    return data # return จะคืนค่ากลับไปที่ Fn read_csv โดยควรจะมีตัวแปรรับถ้าจะนำไปใช้งาน
        # print(data)
        # print('------')
        # print(data[0][0])
        # for a,b,c,d,e in data:
        #    print(e)
# rs = read_csv()
# print(rs)
#----------------------------------------
# สร้าง table มารับ csv

L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['วัน-เวลา','รายการ','ราคาต่อหน่วย','จำนวน','รวม']
resultTable = ttk.Treeview(T2,column=header,show='headings',height=10)
resultTable.pack()

# for i in range(len(header)):
#    resultTable.heading(header[i],text=header[i]) # or อีกแบบ

for h in header:
    resultTable.heading(h,text=h)

headerWidth = [150,170,80,80,80]
for h,w in zip(header,headerWidth):
    resultTable.column(h,width=w)

#หรือใช้ resultTable.column('วัน-เวลา',width = 10)
# for i in range(len(headerWidth)):
#    resultTable.column(header[i],width = headerWidth[i])

# แบบ manual insert -> resultTable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])
#                      resultTable.insert('','end',value=['อังคาร','ผักกาด',12,10,120])
# end หมายถึง ตัวใหม่ใส่ในลำดับท้าย ถ้า 0 หมายถึง ตัวข้อมูลใหม่อยู่บนสุดเสมอ

def update_table():
    resultTable.delete(*resultTable.get_children())
    # หรือเท่ากับ for c in resultTable.get_children():
    #                resultTable.delete(c)

    data = read_csv() # จะได้อยู่ในลักษณะ nested list
    for d in data:
        resultTable.insert('',0,value=d)

update_table()



##############TAB2#######################


GUI.bind('<Tab>',lambda X: E2.focus())
GUI.mainloop()

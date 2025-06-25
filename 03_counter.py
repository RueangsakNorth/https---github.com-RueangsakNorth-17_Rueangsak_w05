counter = 0
def intcrement():
    '''เพิ่มค่า counter ที่ละ 1'''
    global counter
    counter += 1
    print(f"Counter : {counter}")
def reset_counter():
    '''reset ให้เป็น 0'''
    global counter
    counter = 0
    print(f"Counter รีเซ็ตแล้ว")
        
intcrement()
intcrement()
intcrement()
reset_counter()
intcrement()


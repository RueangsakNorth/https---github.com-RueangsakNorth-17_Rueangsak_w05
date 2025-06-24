# # รับ parameter
# def ชื่อฟังชั่น (paramiter)
# pramiter1 + pramiter2

# def get_name(neme):
#     print(f"hello : {neme}")
# name = input("Enter you name :")
# get_name(name)

# def add_num(a,b):
    
#    result = a + b
#    return result
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = add_num(a,b)
# print(f"Sum is : {sum}")

def rect_cal(width,length):
    area = width * length
    perimeter = 2 * (width + length)
    return area, perimeter

width = int(input("Enter width: "))
length = int(input("Enter length: "))
area, perimeter = rect_cal(width, length)
print(f"Area: {area} Perimeter: {perimeter}")
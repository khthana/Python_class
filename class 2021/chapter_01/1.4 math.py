#---------------------------------------------
#?*Python math operation
#?  a + b
#?  a – b
#?  a * b
#?  b / a
#?  b % a Modulus   หารเอาเศษ
#?  a**b  Exponent  ยกกำลัง
#?  9//2 = 4 Floor Division  หารปัดลง
#---------------------------------------------

print(6 / 3)
print(2 ** 3)
print(5 % 2)
print(5 // 2)

#---------------------------------------------
#* กรณีมีหลาย Operator จะมีการทำงานก่อนหลัง 
#* PEMDAS
#* P = Parentheses ()
#* E = Exponent 
#* M = Multiplication *
#* D = Division /
#* A = Add
#* S = Subtrction 
#* หากมีวงเล็บ ต้องทำในวงเล็บก่อน
#* หากไม่มีวงเล็บ จะทำตามลำดับดังนี้
#* ยกกำลัง** , */ , // , % จากนั้นจึงเป็น + -
#* โดยการคำนวณจะทำจาก ซ้ายไปขวา
#---------------------------------------------

print(3 * 3 + 3 / 3 -3)

#| Ex1.8 จากคำสั่งข้างต้นให้ใส่วงเล็ก เพื่อให้ผลลัพธ์เป็น 3.0 


#| Ex1.9 จงเขียนโปรแกรมหาBody Mass Index (BMI) 
#|       = weight(kg) / height(m)^2 
#| Input:
#|      Enter weight : 80
#|      Enter height : 1.75
#|Output:
#|      80 ÷ (1.75 x 1.75) = 26.122448979591837
#|      BMI = 26

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")



#---------------------------------------------
#* การหารกับการปัดเศษ
#---------------------------------------------

print(8/3)
print(int(8/3))
print(8//3)
print(round(8/3))
print(round(8/3),2)

#---------------------------------------------
#* เรื่องชวนงงกับเลขทศนิยม
#* https://docs.python.org/3/tutorial/floatingpoint.html
#---------------------------------------------

a = 0.2
b = 0.1
print(a + b)

#---------------------------------------------
#* เราสามารถใช้ shortcut ในการเขียนโปรแกรม 
#* a=a+1 สามารถเขียนเป็น a+=1
#* a=a-1 สามารถเขียนเป็น a-=1
#* a=a*1 สามารถเขียนเป็น a*=1
#* a=a/1 สามารถเขียนเป็น a/=1
#---------------------------------------------

#| Ex1.10 คำนวณปริมาตรของ 4 เหลี่ยมลูกบาศก์
#| Output : Volume of Cube :

width = float(input("Enter input width = "))
length = float(input("Enter input length = "))
height = float(input("Enter input height = "))


#---------------------------------------------
### ตัวอย่าง : จงเขียนโปรแกรมคำนวณภาษีมูลค่าเพิ่ม
#---------------------------------------------

Income = float(input("Enter your income (Baht): "))
VAT = float(input("Enter your VAT (%): "))
Tax =
print("Your Tax is ", Tax, "Baht")

#| Ex1.11 คำนวณพื้นที่สามเหลี่ยม
#| สูตร 1/2 * Base * Height

#---------------------------------------------
### ตัวอย่าง : จงเขียนโปรแกรมหาเศษคละ
### เศษคละ คือ เศษส่วนที่เป็นผลบวกของจำนวนเต็มกับเศษส่วนแท้
### เช่น 25/7 = 3 + 4/7 
#---------------------------------------------

num1 = int(input("Enter input number 1 = "))
num2 = int(input("Enter input number 2 = "))
x = num1 // num2
y = num1 % num2
print("เศษคละเท่ากับ ", x, "(", y, "/", num2, ")")


#| Ex 1.12 จงเขียนโปรแกรมแปลงค่าจากองศาเซลเซียสไปเป็นองศาฟาเรนไฮต์
#| สูตรในการเปลี่ยนค่าจากองศาเซลเซียสไปเป็นองศาฟาเรนไฮต์มีดังนี้
#| F = (9/5)*C+32
#| รับข้อมูลองศาเซลเซียสเป็นจำนวนจริง
#| แสดงผลตัวเลขจำนวนจริง เป็นองศาฟาเรนไฮต์
#| 39.85 -> 103.73


#---------------------------------------------
### ตัวอย่าง : จงเขียนโปรแกรมคำนวณ หาคำตอบของสมการ
### ax2 + bx +c = 0
### เช่น 25/7 = 3 + 4/7 
### https://krupraiwan.wordpress.com/2014/09/15/quadratic-by-formula/
### รับค่า a,b,c แล้วให้คำตอบค่า x
#---------------------------------------------










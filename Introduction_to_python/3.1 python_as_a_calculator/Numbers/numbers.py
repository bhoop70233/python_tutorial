#The interpreter acts as a simple calculator
a=2+2
b=50-5*6
c=(50-5*6)/4
d=8/5 # division always returns a floating-point number
print(a,b,c,d)

q=17/3  # classic division returns a float
w=17//3 # floor division discards the fractional part
e=17%3 # the % operator returns the remainder of the division
r=5*3+2  #floored quotient *divisor +remainder

print(q,w,e,r)

t=5**2 # 5 squared
y=2 ** 7 # 2 to the power of 7

print(t,y)

width=20
height=5*9
u=width*height
print(u)

#full support for floating point,operators with mixed type operands covert the integer operand to floating point
i=4*3.75-1
print(i)

#python as a desk calculator
tax=12.5/100
price=100.50
o=print(price*tax)




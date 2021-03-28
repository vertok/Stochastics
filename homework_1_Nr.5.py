import math
# a
print("result:", -20*15+5*74)
# b
var1 = -20*15+5*74
print("var1 = ", var1)
# c
print("math.sqrt(var1)", math.sqrt(var1))
# d
var2 = math.pow(var1, 1/5.)
print("var2 = ", var2)
# e
print("var2 < pi: ", var2 < math.pi)
# f
var3 = (math.exp(5)-math.pow(math.pi, 2)) / math.log(10)
print("math.exp(5)-math.pow(math.pi, 2) / math.log(10) = ", var3)
# g
# round(var3) will be 60 which one is correct?
print("math.ceil(var3): ",math.ceil(var3))
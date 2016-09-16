from LinAlg import Vector


vector1 = Vector([8.218,-9.341])
vector2 = Vector([-1.129, 2.111])
vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.223, 0.878])
vector5 = Vector([1.671, -1.012, -0.318])
scalar = 7.41

vector6 = Vector([-0.221, 7.437])
vector7 = Vector([8.813, -1.331, -6.247])
vector8 = Vector([5.581, -2.136])
vector9 = Vector([1.996, 3.108, -4.554])

try:
    print (vector1 + vector2)
    print (vector3 - vector4)
    print (scalar * vector5)

    print (vector6.magnitude)
    print (vector7.magnitude)
    print (vector8.direction)
    print (vector9.direction)

except Exception as e:
    print(e)

'''
if(my_vector == Vector([1,2,4])):
    print("lol")
else:
    print("kip")
'''
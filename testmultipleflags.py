x,y,z = 0,1,0

if x == 1 or y== 1 or z== 1:
    print ("all tests are passed")

if  1 in (x,y,z):
    print("all the tests are passed")

if x or y or z:
     print("all the tests are passed")

if any((x,y,z)):
    print("Any one of the tests are passed")        
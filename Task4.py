Z=["python","django",[1,2,3,4,(5,8,3,"DON","KING"),"don","king"],7,9,10]

print("Given input Z is:",Z)
#output=1
print("Excepted value is :",Z[2][0:1:1])
#output=DON (+,-)
print("by using + indexing :",Z[2][4][3][0:3:1])
#print("by using - indexing :",Z[-2][-3][-1][-4::1])
#output=KING (-)
print("by using - indexing :",Z[-4][-3][-1][-4::1])
#output=ing  (+)
print("by using + indexing :",Z[2][6][1:4:1])
#output=ON (+)(-)
print("by using + indexing :",Z[2][4][3][1:3:1])
print("by using - indexing :",Z[-4][-3][-2][-2::1])
#output=8 (+)(-)
print("by using + indexing :",Z[2][4][1])
print("by using - indexing :",Z[-4][-3][-4])
#output=N (+)(-)  "first occerence)
print("by using + indexing :",Z[2][4][3])
print("by using - indexing :",Z[-4][-3][-1])
#output=k (+)(-)
print("by using + indexing :",Z[2][6][0])
print("by using - indexing :",Z[-4][-1][-4])
#output:['don', 'king'] (-)  one line
print("by using + indexing :",Z[-4][-2::1])


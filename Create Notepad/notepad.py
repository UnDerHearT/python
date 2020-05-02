#edit flie .txt for already exists

#a = เขียนต่อ
f = open("wow.txt","a")
#\n = เว้นบรรทัด
f.write("\nksdjgksd;vldsmv")
f.close

f = open("opena.txt","r")
print(f.read())

#เป็นการ Replace File
#ใช้ w
f = open("wow.txt","w")
f.write("\nksdjgksd;vldsmv")
f.close

f = open("opena.txt","r")
print(f.read())


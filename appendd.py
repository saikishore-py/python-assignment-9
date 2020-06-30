#program to append a file and display

f= open("gitam.txt","w")
f.write("this is kishore")

f= open("gitam.txt","a")
for i in range (2):
    f.write("Append line %d\r\n  %(i+1)")
f.close()


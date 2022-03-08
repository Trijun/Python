""" STRING MODIFICATION """ 

text="awesome"
print(text.upper())#upper
print(text)

""" upper() is a non destructive function meaning it only modifies the string and doesnt affect the original string"""

text1="     awesome      "
print(text1.strip())
print(text1.lstrip()) #leftstrip
print(text1.rstrip()) #rightstrip

print(text1.replace("aw","(awwww)")) #replace

text2="Trijun is awesome"
print(text2.split(" ")) #split

"""it splits the string based on " "(single white space) and creates a set[]"""

list_students="trijun,charlotte,3G,junie"
print(list_students.split(","))


txt = "The best student in class is: {}"
student = "TRIJUN"

print(txt.format(student)) #format

"""format function replaces the placeholder "()" to a different string"""

txt1 = "The best student in class is: {1} {0}"
student1 = "TRIJUN"
student2 = "3G"
print(txt1.format(student1,student2))

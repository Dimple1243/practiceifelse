classes_held=int(input("enter the classes held "))
classes_attended=int(input("enter the classes attended"))
percentage=classes_attended/classes_held*100
if percentage>=75:
    print("allowed to sit in the exam")
else:
    print(" not allowed to sit in the exam")

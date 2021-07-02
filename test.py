sub1 = int(input("Enter marks of 1st subject: "))
sub2 = int(input("Enter marks of 2nd subject: "))
sub3 = int(input("Enter marks of 3rd subject: "))
avg = (sub1 + sub2 + sub3)/3
print(int(avg))
if avg >= 50:
    print("Promoted")
else:
    print("failed")
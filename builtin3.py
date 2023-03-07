s1 = input()
s2 = reversed(s1)
s3 = ""
for x in s2:
    s3 = s3 + x
if s1 == s3:
    print("is Palindrome")
else:
    print("not Palindrome")

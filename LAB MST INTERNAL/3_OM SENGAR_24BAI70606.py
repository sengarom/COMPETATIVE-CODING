#OM SENGAR- UID - 24BAI70606 SECTION - 24AIT-NTPP-2
#LEET CODE PROBLEM - 3 - LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS


s = input("Enter a string:").strip()
n = len(s)
maxlength = 0
charset = set()
for right in range(n):
    if s[right] not in charset:
        charset.add(s[right])
        maxlength = max(maxlength, right - left + 1)
    else:
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])
print(maxlength)
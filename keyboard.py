n=input()
nums=input()
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
position=-1 if n =='R' else 1
result=''
for i in range(len(nums)):
    result+=keyboard[keyboard.index(nums[i])+position]
print(result)
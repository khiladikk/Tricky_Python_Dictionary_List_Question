#Solution 1:

numbers= raw_input("enter the numbers: ")
num_list = numbers.split(",")
print(num_list)
print tuple(numbers)


# Solution 2:
for i in numbers:
    
    if i%2 ==0:
        print(i)
        
    if i== 237:
        break

# Solution 3:
d ={}
word= "googlgoogle"

for i in word:
    d[i]= word.count(i)
         
print(d)    


#Solution 4:

string1 = raw_input('enter your string: ')
digits= 0
letters= 0
for i in string1:
    
    if i.isdigit():
        digits+= 1
          
    elif i.isalpha():
        letters+= 1
print("The number of digits is:")
print(digits)
print("The number of letters is:")
print(letters)


# Solution 5:
numbers = list(input("enter the numbers"))
numbers.sort()

print sum(numbers[1:-1])/len(numbers[1:-1])


#Solution 6:
total = 0

for i in range(len(numbers)):
    if (numbers[i]==13) or (numbers[i-1]==13):
        continue
    else:
        total += numbers[i]

print total
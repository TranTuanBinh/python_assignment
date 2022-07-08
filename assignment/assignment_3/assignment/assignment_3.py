#1 
""" Implement the algorithm from description (String: 8-1):
The program asks the user to enter a string. It then uses a for loop to iterate
over the string, counting the number of times that the letter T (uppercase or
lowercase) appears."""

in_str = input('Enter your string:  ') #gán string
count = 0 # gán count = 0 để hứng giá trị
for x in in_str :
    if x == 't' or x == 'T':
        count += 1



#2

#3
""" Implement the algorithm from description (List: 7-3):
The append method is commonly used to add items to a list. The item that is
passed as an argument is appended to the end of the list’s existing elements."""

member = ['binh','uyen','long','hoang','ha']
member.append('dung trieu')
print(member)
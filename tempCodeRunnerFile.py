Sample_Data = "Python 3.13"
letter_count = len(Sample_Data)
for i in range (0,11):
    char = Sample_Data[i]  
    if char == ' ' or char == '.':
        continue      
    print(char)
print(letter_count)
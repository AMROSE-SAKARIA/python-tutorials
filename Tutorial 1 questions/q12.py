neg=0
pos=0
nn=0
np=0
for i in range(4):
    num = int(input(f"Enter number {i+1}: ")) 
    if num<0:
        neg=neg+num
        nn=nn+1
    else:
        pos=pos+num
        np=np+1
avgn=neg/nn
avgp=pos/np        
print(f"Sum of negative numbers: {neg}")
print(f"Sum of positive numbers: {pos}")   
print(f"Average of negative numbers: {avgn}")
print(f"Average of positive numbers: {avgp}")     
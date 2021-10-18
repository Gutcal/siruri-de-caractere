s=' A B C D E F G H I J K L M N O P R S T U V W X Y Z '
s1=''
s2=''
s3=''
for i in s:
    x=chr(ord(i)+1)
    s1+=x
    y=s1.replace('!', '')
    a=y.replace('[', 'A')
print('Sirul 1:', a) 

s2=a
for i in s:
    b=s2.replace(("Z"), ("A"))
    c=b.replace('!', '')
    d=c.replace('[', 'A')
print('Sirul 2:', d)   

s3=s
for i in s:
    e=s3.replace((' '), ('-'))
print('Sirul 3:', e)  
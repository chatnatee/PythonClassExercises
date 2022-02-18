#list

a = [89798, 77456]
#a[0] #position 0=first 1=second ....

i = 4


print(a[i % len(a)]) #i % is the modeulus of a=[]

#list

passw = int(input('enter password:  '))

a = [89798, 77456]
#a[0] #position 0=first 1=second ....

i = 4


if passw == (a[i % len(a)]):
    print('Logged In')
    #############




    


else:
    print('wrong password')

Username = 'Santhosh'
Password = 1001
count = 3
while count>0:
    user= input('Enter Username: ')
    Pass = int(input('Enter Password: '))
    if Username==user and Password==Pass:
        print('Login Success!')
        break
    else:
        count-=1
        print('Invalid Credentials',count,'Attempts remaining')
        if count==1:
            print('Warning!!, Account Will be blocked')
        if count==0:
            print('Account Blocked Due to Multiple Attempts!!!')

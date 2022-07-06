
test1 = float(input('enter test grade:  ')) 
test2 = float(input('enter test grade:  '))
test3 = float(input('enter test grade:  '))
avg = (test1 + test2 + test3) /3
highscore = 95 
if avg > highscore :
    print('congratulation user')
else :
    print('better luck next time MU')

#------------------------

b_h = 40 
ot_m =1.5
h = int(input('enter your working hours:    '))
p_r = int(input('enter the rate:    ')) 
if h > b_h :
    ot_t = h - b_h
    ot_p = ot_t * p_r * ot_m
    g_p = ot_p + h * p_r 
    print(f'the gross pay is {g_p}') 
else : 
    g_p2 = h * p_r 
    print(f'the gross pay is {g_p2}')
 



#-------------------
min_salary = 30000.0
min_years = 2
salary = float(input('enter your salary here:       '))

years_on_job = int(input('enter number of years on job:     '))

if salary >= min_salary : 
    if years_on_job >= min_years : 
             print(' qualified') 
    else: 
             print(f'you must have been employed'
                     f' for at least {min_year}'
                     f' to be qualified ')
else : 
    print(f' you must earn at least' 
             f' {min_salary}'
             f' to be qualified')
 
#------------------------------
for x in range(5):
    print('HELLO WORLD')

#-------------------------
keep_going = 'y'
while keep_going == 'y':
     sales = float(input('enter the amount of sales: '))
     comm_rate = float(input('enter the commission rate:     '))
     commission = sales * comm_rate 
     print(f'the commission is {commission}')
import datetime as dt

class Counter:
    
    def __init__(self,my_start=0,my_end=None, my_step=1):

        self.my_start=my_start
        self.my_end=my_end
        self.my_step=my_step
        today_date= dt.datetime.now()

        print("Hello, old friend!",today_date.strftime("Today is %A, %B %d, %Y"),"and we are excited to play this game with you!")
        print("\n")
        print(f"{'*':*^79}")
        print("You will have three attempts to complete each question. After three attempts you will have to re-run this program again.",today_date.strftime("The time is %I:%M %p Goodluck!"))
        print("\n")
        print(f"{'*':*^79}")

        questions=[{"my_start":"(Integer Optional) Enter a start value (Integer Default: 0): "},{"my_end":"(Integer Required) Enter an end value: "},{"my_step":"(Optional) Enter a step value (Default: 1): "}]
        
        def setter(**kwargs):
            setattr(self,key,my_answer)

        for question in questions:
            for key,value in question.items():
                print(key,value)
                max_attempts=3
                while True:
                    try:
                        my_answer=input(value)
                        print(my_answer)
                        if len(my_answer)==0:
                            if key=='my_end':
                                print('This value is required and cannot be blank. Please input this number!')
                                raise ValueError
                            else:
                                my_blank_answer=input('Are you sure you want to leave this argument blank. Enter Y for Yes and N for No.').upper()
                                print(f"{'*':*^79}") 
                                if my_blank_answer in {'Y','N'}:
                                    break
                                else:
                                    raise ValueError
                        else:
                            if my_answer.isdigit():
                                if key=='my_end':
                                    if int(my_answer)>self.my_start:
                                        setattr(self,key,int(my_answer))
                                        print(f"{'*':*^79}")
                                        break
                                    else:
                                        print(f'Your END number must be greater than your START number: {self.my_start}! Please try again!')
                                        raise ValueError
                                else:
                                    setattr(self,key,int(my_answer))
                                    print(f"{'*':*^79}")
                                    break                                  
                            else:
                                if int(my_answer)<0:
                                    print("Your value can't be negative!")
                                    raise ValueError  
                                else:
                                    print("It cannot be a string! Please Try again!")
                                    raise ValueError

                    except ValueError:
                        max_attempts-=1
                        if max_attempts>=0:
                            print("You have",max_attempts,"attempts left!")
                            continue
                        else:
                            raise
    def __repr__(self):
        return f"Hello, This is my counter game that starts a count from {self.my_start}, ends before {self.my_end}, and in multiples of {self.my_step}."
    
    def print_count(self):
        #for n in list(range(self.my_start,self.my_end,self.my_step)):
            #print(n)
        x=self.my_start
        print("The numbers are:")
        while x in range(self.my_start,self.my_end,self.my_step):
            print(x,end=" ")
            x+=self.my_step

my_game=Counter()
print(my_game)
my_game.print_count()        
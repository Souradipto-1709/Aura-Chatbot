import random
import pyjokes
import turtle
from google import genai
from voice import speak
import pwinput

def aura_chatbot():
    speak('Welcome to Aura! Your Personal AI Assistant.')
    print('Welcome to Aura! Your Personal AI Assistant.')
    
    def activation():
        while True:
            speak('Activating Aura. Enter Password')
            active = pwinput.pwinput('Activating Aura...Enter your password: ', mask="*")
            if('your_password' == active):
                speak('Aura Activated')
                print('Aura Activated!')
                break
            else:
                speak('Aura not Activated. Enter correct Password.')
                print('Aura not Activated! Enter correct Password.')
    activation()
    
    def u_name():
        speak('Aura would like to know your name.')
        name=input('Aura would like to know your name...')
        speak(f'Nice to meet you {name}.')
        print(f'Nice to meet you {name}!')
    u_name()
    
    def asking_q():
        speak('Please, enter your name once more for verification.')
        name=input('Please, enter your name once more for verification: ')
        speak(f"Name {name} is saved")
        print(f"Name: '{name}' is saved!")
        
        def features():
            def greeting():
                speak(f"What's up {name}.")
                print(f"What's up {name}!")
                
            def calculator():
                speak('Welcome to my Calculator')
                print('Welcome to my Calculator:-')
                while True:
                    print('----')
                    speak("Choose between add, sub, mul, div, power, avg, mod and factorial. Type stop to exit: ")
                    choice = input("Choose between add, sub, mul, div, power, avg, mod and factorial. Type 'stop' to exit: ")
                    
                    if('add' in choice.lower()):
                        def add():
                            sum1 = (a1+a2+a3)
                            return sum1
                        
                        speak('Enter no. 1')
                        a1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        a2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        a3 = float(input('Enter no. 3: '))
                        a = add()
                        speak(f'The addition is {a}')
                        print(f'The sddition is {a}')
                        
                    elif('sub' in choice.lower()):
                        def sub():
                            diff = (s1-s2-s3)
                            return diff
                        
                        speak('Enter no. 1')
                        s1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        s2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        s3 = float(input('Enter no. 3: '))
                        s = sub()
                        speak(f'The subtraction is {s}')
                        print(f'The subtraction is {s}')
                        
                    elif('mul' in choice.lower()):
                        def mul():
                            pro = ((m1*m2)*m3)
                            return pro
                        
                        speak('Enter no. 1')
                        m1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        m2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        m3 = float(input('Enter no. 3: '))
                        m = mul()
                        speak(f'The multiplication is {m}')
                        print(f'The multiplication is {m}')
                        
                    elif('div' in choice.lower()):
                        def div():
                            if(d1==0 or d2==0 or d3==0):
                                speak('Invalid.')
                                return 'Invalid!'
                            else:
                                quo = ((d1/d2)/d3)
                                return quo
                            
                        speak('Enter no. 1')
                        d1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        d2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        d3 = float(input('Enter no. 3: '))
                        d = div()
                        speak(f'The quotient is {d}')
                        print(f'The quotient is {d}')
                        
                    elif('pow' in choice.lower()):
                        def power():
                            if(p2==0):
                                speak('Invalid.')
                                return "Invalid!"
                            else:
                                powe = (p1**p2)
                                return powe
                            
                        speak('Enter the no.')    
                        p1 = float(input('Enter the no.: '))
                        speak('Enter the power.')
                        p2 = int(input('Enter the power: '))
                        p = power()
                        speak(f'The power is {p}')
                        print(f'The power is {p}')
                        
                    elif('avg' in choice.lower()):
                        def avg():
                            average = ((av1+av2+av3)/3)
                            return average
                        
                        speak('Enter no. 1')
                        av1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        av2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        av3 = float(input('Enter no. 3: '))
                        av = avg()
                        speak(f'The average is {av}')
                        print(f'The average is {av}')
                        
                    elif('mod' in choice.lower()):
                        def mod():
                            if(mo1==0 or mo2==0 or mo3==0): 
                                speak('Invalid.')
                                return 'Invalid!'
                            else:
                                modls = ((mo1%mo2)%mo3)
                                return modls
                            
                        speak('Enter no. 1')
                        mo1 = float(input('Enter no. 1: '))
                        speak('Enter no. 2')
                        mo2 = float(input('Enter no. 2: '))
                        speak('Enter no. 3')
                        mo3 = float(input('Enter no. 3: '))
                        mo = mod()
                        speak(f'The remainder is {mo}')
                        print(f'The remainder is {mo}')
                        
                    elif('fact' in choice.lower()):
                        def factorial(n):
                            if(n==1 or n==0):
                                return 1
                            return n*factorial(n-1)
                        speak('Enter a no.')
                        n = int(input('Enter a no: '))
                        f = factorial(n)
                        speak(f'The factorial is {f}')
                        print(f'The factorial is {f}')
                        
                    elif('stop' in choice.lower()):
                        speak('Thanks for using my calculator.')
                        print('Thanks for using my calculator!')
                        break
                    else:
                        speak('Invalid Input!')
                        print('Invalid Input!')
                
            def game():
                speak("Welcome to Aura's gaming mode")
                print("Welcome to Aura's gaming mode!")
                
                def rps():
                    speak('You have chosen to play Rock, Paper and Scissor game.')
                    print('You have chosen to play Rock, Paper and Scissor game!')
                    speak('Choose between rock, paper and scissors')
                    choice = input('Choose between rock, paper and scissors: ').lower()
                    
                    if(choice == 'rock'):
                        choices1 = [
                            'I chose paper, I win!',
                            'I chose scissors, You win!',
                            'I also chose rock, Draw!'
                            ]
                        
                        c1 = random.choice(choices1)
                        speak(c1)
                        print(c1)
                        
                    elif(choice == 'paper'):  
                        choices2 = [
                            'I chose rock, You win!',
                            'I chose scissors, I win!',
                            'I also chose paper, Draw'
                            ]
                        
                        c2 = random.choice(choices2)
                        speak(c2)
                        print(c2)
                        
                    elif(choice == 'scissors'): 
                        choices3 = [
                            'I chose rock, I win!',
                            'I chose paper, You win!',
                            'I also chose scissors, Draw!'
                            ]
                        
                        c3 = random.choice(choices3)
                        speak(c3)
                        print(c3)
                        
                    else:
                        speak('Invalid Operation.')
                        print('Invalid Operation!')
                        
                def p_guess():
                    speak('Welcome to Perfect Guess game.')
                    print('Welcome to Perfect Guess game!')
                    r = range(1000)
                    comp = random.choice(r)
                    guess = 0
                    
                    while True:
                        speak('Guess the no between 1 to 1000.')
                        n = int(input('Guess the no between 1 to 1000: '))
                        guess+=1
                        
                        if(n<comp):
                            speak('You guessed a lower no! Better luck next time.')
                            print('You guessed a lower no! Better luck next time!')
                            
                        elif(n>comp):
                            speak('You guessed a higher no! Better luck next time.')
                            print('You guessed a higher no! Better luck next time!')
                            
                        elif(n<1 or n>1000):
                            speak('Out of the range.')
                            print('Out of the range!')
                            
                        elif(n==comp):
                            speak('The Perfect Guess.')
                            print('The Perfect Guess!')
                            break
                    
                    speak(f'Yes, You have guessed it correct. The Computer chose {comp}.')    
                    print(f'Yes, You have guessed it correct! The Computer chose {comp}.')
                    speak(f'You needed {guess} attempts to guess the correct no.')
                    print(f'You needed {guess} attempts to guess the correct no.')
                    speak('Thanks for playing my game.')
                    print('Thanks for playing my game!')
                    
                while True:
                    speak('Choose between Rock, Paper and Scissor game, 1 or Perfect Guess game, 2. Type bye to exit.')
                    g_choice = input("Choose between Rock, Paper and Scissor game(1) or Perfect Guess game(2). Type 'bye' to exit: ")
                    if('1' in g_choice):
                        rps()
                        
                    elif('2' in g_choice):
                        p_guess()
                        
                    elif('bye' in g_choice.lower()):
                        speak("Thanks for using Aura's gaming mode.")
                        print("Thanks for using Aura's gaming mode!")
                        break
                    
                    else:
                        speak('Invalid input.')
                        print('Invalid input!')
                        
            def jokes():
                joke = pyjokes.get_joke()
                speak(joke)
                print(joke)
                
            def draw():
                def d_star():
                    speak('Drawing Star.')
                    print('Drawing Star...')
                    star = turtle.Turtle()
            
                    for i in range(5):
                        star.forward(200)
                        star.right(144)
                    turtle.done()
                    
                def d_flower():
                    speak('Drawing Flower.')
                    print('Drawing Flower...')
                    t = turtle.Turtle()
                    t.speed(2)
                    
                    t.up()
                    t.right(90)
                    t.forward(100)
                    t.right(180)
                    t.down()
                    t.forward(150)
                    t.left(90)
                    for i in range(12):
                        t.circle(50)
                        t.left(30)
                    turtle.done()
                    
                    speak("Welcome to Aura's Drawing Mode.")
                    print("Welcome to Aura's Drawing Mode!")
                    
                    while True:
                        speak("What do you want to draw. Type bye to exit.")
                        d_choice = input("What do you want to draw. Type 'bye' to exit: ")
                        
                        if('star' in d_choice.lower()):
                            d_star()
                            
                        elif('flower' in d_choice.lower()):
                            d_flower()
                            
                        elif('bye' in d_choice.lower()):
                            speak("Thanks for using Aura's Drawing Mode.")
                            print("Thanks for using Aura's Drawing Mode!")
                            break
                        
                        else:
                            speak('Invalid Input.')
                            print('Invalid Input!')
                            
            def ai_part(u_input):
                try:
                    client = genai.Client()
                    chat = client.chats.create(
                        model="gemini-3.6-flash",
                        config={
                            "system_instruction": "You are Aura, a helpful, friendly and intelligent AI assistant. Give short, summarized answers to questions. You are created by Soura."
                        }                       
                    )
                    response = chat.send_message(u_input)
                    
                    if response.text:
                        speak(response.text.replace('*', ' '))
                        print(response.text)
                        
                    else:
                        speak("I couldn't get a text response.")
                        print("I couldn't get a text response!")
                        
                except Exception as error:
                    speak("I couldn't get a response from Gemini.")
                    print("I couldn't get a response from Gemini!")
                    speak(f"Error: {type(error).__name__, error}")
                    print("Error:", type(error).__name__, error)
                    
                # You have to create a API key for it at first.
                
            while True:
                print('     ')
                print('-----')
                speak('Ask whatever you like. Type bye to exit Aura.')
                u_input = input("Ask whatever you like. Type 'bye' to exit Aura: ")
                print('     ')
                
                if(u_input.lower().strip() in ('hi', 'hello', 'hey')):
                    greeting()
                    
                elif('calculation' in u_input.lower() or 'calculator' in u_input.lower()):
                    calculator()
                    
                elif('game' in u_input.lower()):
                    game()
                    
                elif('joke' in u_input.lower()):
                    jokes()
                    
                elif('draw' in u_input.lower()):
                    draw()
                
                elif('open website' in u_input.lower()):
                    from browser import open_browser
                    
                elif('music library' in u_input.lower()):
                    from music_lib import music_library
                    
                elif('bye' in u_input.lower()):
                    speak(f'Thanks for using Aura, {name}. Meet you next time.')
                    print(f'Thanks for using Aura, {name}! Meet you next time!')
                    break
                
                else:
                    ai_part(u_input)
                    
        features()
    asking_q()
aura_chatbot()

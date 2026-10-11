import webbrowser
from voice import speak
def open_browser():
                def google():
                    speak('Opening Google.')
                    print('Opening Google...')
                    webbrowser.open("https://www.google.com")
                def youtube():
                    speak('Opening Youtube.')
                    print('Opening Youtube...')
                    webbrowser.open("https://www.youtube.com")
                def chatgpt():
                    speak('Opening Chatgpt.')
                    print('Opening ChatGpt...')
                    webbrowser.open("https://chatgpt.com/")               
                def jhotstar():
                    speak('Opening Jio Hotstar.')
                    print('Opening Jio Hotstar...')
                    webbrowser.open("https://www.hotstar.com/in/home")                   
                def whatsapp():
                    speak('Opening Whatsapp.')
                    print('Opening WhatsApp...')
                    webbrowser.open("https://web.whatsapp.com/")
                def claude():
                    speak('Opening Claude.')
                    print('Opening Claude...')
                    webbrowser.open("https://claude.ai/new")
                def github():
                    speak('Opening Github.')
                    print('Opening GitHub...')
                    webbrowser.open("https://github.com/Souradipto-1709")
                def poki():
                    speak('Opening Poki.')
                    print('Opening Poki...')
                    webbrowser.open("https://poki.com/") 
                speak('Welcome to Website Opening Mode of Aura.')                  
                print('Welcome to Website Opening Mode of Aura!')
                while True:
                    speak("Which website do you want to open in Google Chrome. Type bye to exit.")
                    w_choice = input("Which website do you want to open in Google Chrome. Type 'bye' to exit: ")           
                    if('google' in w_choice.lower()):
                        google()                  
                    elif('youtube' in w_choice.lower()):
                        youtube()                  
                    elif('chatgpt' in w_choice.lower()):
                        chatgpt()                    
                    elif('jiohotstar' in w_choice.lower()):
                        jhotstar()                   
                    elif('whatsapp' in w_choice.lower()):
                        whatsapp()                       
                    elif('claude' in w_choice.lower()):
                        claude()                       
                    elif('github' in w_choice.lower()):
                        github()                      
                    elif('poki' in w_choice.lower()):
                        poki()                
                    elif('bye' in w_choice.lower()):
                        speak('Thanks for using this feature of Aura.')
                        print('Thanks for using this feature of Aura!')
                        break               
                    else:
                        speak('Website not Available.')
                        print('Website not Available!')
open_browser()

# You can also add your desired websites.
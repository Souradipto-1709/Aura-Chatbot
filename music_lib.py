import webbrowser
from voice import speak
def music_library():
    def believer():
        speak('Opening Believer.')
        print('Opening Believer...')
        webbrowser.open("https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP?si=ce92c28141004983")
    def bones():
        speak('Opening Bones.')
        print('Opening Bones...')
        webbrowser.open("https://open.spotify.com/track/0HqZX76SFLDz2aW8aiqi7G?si=a483cdea6cf443d3")
    def sapphire():
        speak('Opening Sapphire.')
        print('Opening Sapphire...')
        webbrowser.open("https://open.spotify.com/track/4Q0qVhFQa7j6jRKzo3HDmP?si=1e48263578f34d84")
    def unstopable():
        speak('Opening Unstopable.')
        print('Opening Unstopable...')
        webbrowser.open("https://open.spotify.com/track/2J2Z1SkXYghSajLibnQHOa?si=a7d41438bbc24f9f")
    def diewas():
        speak('Opening Die with a smile.')
        print('Opening Die With A Smile...')
        webbrowser.open("https://open.spotify.com/track/78mE33YpoWqMQTwgUQRhyo?si=2cb268911b864942")
    def ontf():
        speak('Opening On The Floor. Due to technical issues it is opening on Youtube.')
        print('Opening On The Floor. Due to technical issues it is opening on Youtube...')
        webbrowser.open("https://youtu.be/70XspGKI8kQ?si=DZJ777VQBPFzItZN")
    def daku():
        speak('Opening Daku.')
        print('Opening Daku...')
        webbrowser.open("https://open.spotify.com/track/5Szje6RzjoETtNBoAEfHDQ?si=04ba6ab52bd644cd")
    def life():
        speak('Opening Life.')
        print('Opening Life...')
        webbrowser.open("https://open.spotify.com/track/6WJecKIlX8CwDCS2bo4uFt?si=87bcaba66b574e9d")
    def bad_liar():
        speak('Opening Bad Liar.')
        print('Opening Bad Liar...')
        webbrowser.open("https://open.spotify.com/track/2RSHsoi04658QL5xgQVov3?si=67aa3ab89de4443e")
    def game_on():
        speak('Opening Game On.')
        print('Opening Game On...')
        webbrowser.open("https://open.spotify.com/track/0oekPABpNQshhsPOEkvESS?si=d941996c3ba040ee")
    def moye():
        speak('Opening Moye Moye.')
        print('Opening Moye Moye...')
        webbrowser.open("https://open.spotify.com/track/2fF8V1O1i1Y8s06FmJHJlz?si=665df8f2fb334d0b")
    def lmdownsl():
        speak('Opening Let me down slowly.')
        print('Opening Let Me Down Slowly...')
        webbrowser.open("https://open.spotify.com/track/2qxmye6gAegTMjLKEBoR3d?si=cf0f6307f4054e1e")
    def kamin():
        speak('Opening Kamin.')
        print('Opening Kamin...')
        webbrowser.open("https://open.spotify.com/track/057YRaQ57p70MVg4hMIIkB?si=737415024a15468c")
    def enemy():
        speak('Opening Enemy.')
        print('Opening Enemy...')
        webbrowser.open("https://open.spotify.com/track/1r9xUipOqoNwggBpENDsvJ?si=d17ebee1a13d4682")
    def france_2018():
        speak('Opening France 2018 world cup song..')
        print('Opening France 2018 World Cup Song...')
        webbrowser.open("https://open.spotify.com/track/45eY7Qi2PDUs8WJEhjGWdN?si=cb2c70feaa5c46d2")
    def headlights():
        speak('Opening Headlights.')
        print('Opening Headlights...')
        webbrowser.open("https://open.spotify.com/track/7BhmwvCdQZNwuQXSHw5TzP?si=c20642750dbd40cb")
    speak("Welcome to Aura's Music Library.")
    print("Welcome to Aura's Music Library!")
    while True:
        speak("Which song do you want to hear on Spotify and Youtube. Type bye to exit: ")
        m_choice = input("Which song do you want to hear on Spotify (and Youtube). Type 'bye' to exit: ")
        if('believer' in m_choice.lower()):
            believer()
        elif('bones' in m_choice.lower() or 'boys' in m_choice.lower()):
            bones()
        elif('sapphire' in m_choice.lower()):
            sapphire()
        elif('unstopable' in m_choice.lower()):
            unstopable()
        elif('die with a smile' in m_choice.lower()):
            diewas()
        elif('on the floor' in m_choice.lower()):
            ontf()
        elif('daku' in m_choice.lower()):
            daku()
        elif('life' in m_choice.lower()):
            life()
        elif('bad liar' in m_choice.lower()):
            bad_liar()
        elif('game on' in m_choice.lower()):
            game_on()
        elif('moye' in m_choice.lower()):
            moye()
        elif('let me down' in m_choice.lower()):
            lmdownsl()
        elif('kamin' in m_choice.lower()):
            kamin()
        elif('enemy' in m_choice.lower()):
            enemy()
        elif('france 2018' in m_choice.lower()):
            france_2018()
        elif('headlights' in m_choice.lower()):
            headlights()
        elif('bye' in m_choice.lower()):
            speak('Thanks for using this mode of Aura.')
            print('Thanks for using this mode of Aura!')
            break
        else:
            speak('Song not available.')
            print('Song not available!')
music_library()

# You can also add your desired songs.
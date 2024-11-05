import speech_recognition as sr
import pyttsx3
import pywhatkit
import pygame

pygame.init()

display_width = 564
display_height = 564

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MELODY')

gameDisplay.fill(white)
micImg = pygame.image.load('robot.jpg')
gameDisplay.blit(micImg,(0,0))

def close():
    pygame.quit()
    quit()


def text_objects(text, font):
    textSurface = font.render(text, True , alpha)
    return textSurface , textSurface.get_rect()

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay , ac , (x,y,w,h))

        if click[0] ==1 and action!= None:
            action()
    else:
        pygame.draw.rect(gameDisplay , ic, (x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms" , 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def s2t():
    gameDisplay.blit,(micImg, (0,0))


    listner = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        try:
            with sr.Microphone() as source:
                talk("Hi I am melody, what do you want to listen to today?")
                voice=listner.listen(source)
                command = listner.recognize_google(voice)
                command = command.lower()
                if 'melody' in command:
                    command = command.replace('melody','')
                    print(command)
        except:
            pass
        return command

    def run_melody():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play','')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        else:
            talk("I did not quite catch that please repeat the command once again!")
    run_melody()

def main():
    while True:
     for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()
     button("SPEAK!", 150, 450, 100, 50, green, bright_green, s2t)
     button("QUIT", 350, 450, 100, 50, red, bright_red, close)
     pygame.display.update()

if __name__ == '__main__':
    main()



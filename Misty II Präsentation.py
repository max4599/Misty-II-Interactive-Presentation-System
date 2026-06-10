#----------------------------------------------------------------------------------------------------------
# !!! ATTENTION !!! ONLY PYTHON 3.11 !!!
# python -m pip install mistyPy
# Copy folder MistyPy to *Python3-folder* (C:\Users\Seminar\AppData\Local\Programs\Python\Python313)
#C:\Users\Seminar\AppData\Local\Microsoft\WindowsApps\pythonw3.11.exe <SCRIPTNAME>
#----------------------------------------------------------------------------------------------------------

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from threading import Thread

from time import sleep
import math, random, sys, os,threading

misty = Robot("192.168.50.131") # Noctis / Cube
misty.display_text("aQa")

def recognized(event):
   if 'foundFaces' in event:
      for face in event['foundFaces']:
        name = face.get('name')
        if name:
           print('Hallo',{name})

        else:
           def reset_misty():
              misty.change_led(115, 211, 240)
              misty.move_arm(arm="both", position=30)
              misty.move_head(pitch=0, roll=0, yaw=0) 
              misty.display_image("e_DefaultContent.jpg")
              misty.set_default_volume(99)
              misty.stop()
           def speak1(text):
               misty.play_audio("s_Awe1.wav")
               sleep(3)
               misty.display_image("e_Joy.jpg")
               misty.transition_led(0, 255, 0, 0, 0, 255, "breathe", 1200)  # Transition from green to blue
               misty.move_arms(-40, 40)  # Move left arm up, right arm down
               misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local") 
           def speak2(text):  
              misty.play_audio("s_Joy.wav")
              sleep(3)
              misty.display_image("e_DefaultContent.jpg")
              misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local")
              misty.transition_led(0, 0, 255, 255, 0, 0, "breathe", 1200)  # Transition from blue to red
              misty.move_arms(-60,-60) 
           def speak3(text):
               misty.play_audio("s_Awe2.wav")
               sleep(3)
               misty.transition_led(250, 0, 0, 0, 0, 0, "Blink", 1200)
               misty.display_image("e_Joy.jpg")
               misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local") 
               for x in range(0, 4):
                 misty.move_arms(-30,30)
                 sleep(0.5)
                 misty.move_arms(30,-30) 
                 sleep(0.5)
           def countdown(tme):
              cdn = tme
              misty.transition_led(255, 127, 0, 0, 0, 255, "breathe", 1200)
              for x in range(0, tme):
                print("cnt = "+ str(cdn))
                misty.display_text("..:"+ str(cdn)+":..")
                cdn -= 1
              sleep(1)
              misty.display_text("aQa")
           while(True):
              print("Step #1")
              speak2("Schön, dass Sie da sind!  Entdecken  Sie  die  Welt  von   aQua,   effizient, nachhaltig  und  zukunftsorientiert.")
              misty.drive(linearVelocity=0, angularVelocity=10)
              misty.drive(linearVelocity=0, angularVelocity=-10)
              misty.move_head(pitch=-20, roll=0, yaw=40) # 0
              misty.move_arms(-30,30)
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)
    
              print("Step #2")
              speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
              mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
              misty.drive(linearVelocity=0, angularVelocity=-10)
              misty.drive(linearVelocity=0, angularVelocity=10)
              misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
              misty.move_arms(30,-30)
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)

              print("Step #3")
              speak1("aQua begrüßt Sie! Lassen  Sie sich von unseren Zukunftsperspektiven begeistern.")
              misty.drive(linearVelocity=0, angularVelocity=10)
              misty.move_head(pitch=-20, roll=0, yaw=0) #
              misty.move_arms(-30,30)
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)

              print("Step #4")
              speak2("Sind Sie neugierig? Sprechen Sie uns an!")
              misty.drive(linearVelocity=0, angularVelocity=-10)
              misty.move_head(pitch=-40, roll=0, yaw=0) #
              misty.move_arms(30,-30) 
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)

              print("Step #5")
              speak1("Die aQua verbindet Arbeitssuchende und Unternehmen mit maßgeschneiderten Bildungsangeboten\
              und passgenauen Dienstleistungen für unterschiedlichste Zielgruppen.")
              misty.drive(linearVelocity=-0, angularVelocity=0)
              misty.move_head(pitch=-20, roll=0, yaw=0) #
              misty.move_arms(0,0)    
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)
    
              print("Step #6")
              speak3("Die aQua schafft Chancen, baut Brücken und begleiten Menschen sicher in den Arbeitsmarkt.")
              misty.drive(linearVelocity=0, angularVelocity=10)
              misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
              misty.move_arms(30,-30)
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)
    
              print("Step #7")
              speak2("Sind Sie neugierig? Sprechen Sie uns an!")
              misty.drive(linearVelocity=0, angularVelocity=-5)
              misty.move_head(pitch=-40, roll=0, yaw=0) #
              misty.move_arms(30,-30) 
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)
    
              print("Step #8")          
              speak1("Unser Angebot richtet sich individuell nach den Bedürfnissen der Menschen,\
              die wir begleiten für einen nachhaltigen Erfolg und echte Entwicklung.")
              misty.drive(linearVelocity=-0, angularVelocity=5)
              misty.move_head(pitch=-20, roll=0, yaw=0) #0
              misty.move_arms(0,0)    
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)
    
              print("Step #8")
              speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
               mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
              misty.drive(linearVelocity=0, angularVelocity=-5)
              misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
              misty.move_arms(30,-30)
              sleep(4); reset_misty()
              rnd = random.randint(10, 12);
              countdown(rnd)

              quit()


misty.RegisterEvent('face_detec','FaceRecognition',500,callback=recognized)
misty.styrt_face_recognition()








       
def scan_head():
   try:
      while True:
         misty.MoveHead(roll = 0, pitch= 0, yaw = -30,velocity = 30)
         sleep(1.5)
         misty.MoveHead(roll= 0, pitch= 0, yaw=30, velocity = 30)
         sleep(1.5)
   
   except KeyboardInterrupt:
      misty.StopFaceRecognition()
      misty.MoveHead(roll = 0, pitch = 0,yaw = 0, velocity = 30)
      print('stop')

head_thread =threading.Thread(target=scan_head)    
  
head_thread.start()
                  
                     




# def recognized(data):
    
#     print(data)  
#     if data["message"]["label"] == 'Max': 
    
#       def reset_misty():
#           misty.change_led(115, 211, 240)
#           misty.move_arm(arm="both", position=30)
#           misty.move_head(pitch=0, roll=0, yaw=0) 
#           misty.display_image("e_DefaultContent.jpg")
#           misty.set_default_volume(99)
#           misty.stop()
#       def speak1(text):
#           misty.play_audio("s_Awe1.wav")
#           sleep(3)
#           misty.display_image("e_Joy.jpg")
#           misty.transition_led(0, 255, 0, 0, 0, 255, "breathe", 1200)  # Transition from green to blue
#           misty.move_arms(-40, 40)  # Move left arm up, right arm down
#           misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local")     
#       def speak2(text):  
#          misty.play_audio("s_Joy.wav")
#          sleep(3)
#          misty.display_image("e_DefaultContent.jpg")
#          misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local")
#          misty.transition_led(0, 0, 255, 255, 0, 0, "breathe", 1200)  # Transition from blue to red
#          misty.move_arms(-60,-60)
#       def speak3(text): 
#          misty.play_audio("s_Awe2.wav")
#          sleep(3)
#          misty.transition_led(250, 0, 0, 0, 0, 0, "Blink", 1200)
#          misty.display_image("e_Joy.jpg")
#          misty.speak(text,1.2, 1.1, voice="de-de-x-deb-local")
#          for x in range(0, 4):
#             misty.move_arms(-30,30)
#             sleep(0.5)
#             misty.move_arms(30,-30) 
#             sleep(0.5)
 
#       def countdown(tme):
#           cdn = tme
#           misty.transition_led(255, 127, 0, 0, 0, 255, "breathe", 1200)
#           for x in range(0, tme):
#             print("cnt = "+ str(cdn))
#             misty.display_text("..:"+ str(cdn)+":..")
#             cdn -= 1
#             sleep(1)
#           misty.display_text("aQa")
#       while(True):

#        print("Step #1")
#        speak2("Schön, dass Sie da sind!  Entdecken  Sie  die  Welt  von   aQua,   effizient, nachhaltig  und  zukunftsorientiert.")
#        misty.drive(linearVelocity=0, angularVelocity=10)
#        misty.drive(linearVelocity=0, angularVelocity=-10)
#        misty.move_head(pitch=-20, roll=0, yaw=40) # 0
#        misty.move_arms(-30,30)
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)
    
#        print("Step #2")
#        speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
#        mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
#        misty.drive(linearVelocity=0, angularVelocity=-10)
#        misty.drive(linearVelocity=0, angularVelocity=10)
#        misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#        misty.move_arms(30,-30)
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)

#        print("Step #3")
#        speak1("aQua begrüßt Sie! Lassen  Sie sich von unseren Zukunftsperspektiven begeistern.")
#        misty.drive(linearVelocity=0, angularVelocity=10)
#        misty.move_head(pitch=-20, roll=0, yaw=0) #
#        misty.move_arms(-30,30)
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)

#        print("Step #4")
#        speak2("Sind Sie neugierig? Sprechen Sie uns an!")
#        misty.drive(linearVelocity=0, angularVelocity=-10)
#        misty.move_head(pitch=-40, roll=0, yaw=0) #
#        misty.move_arms(30,-30) 
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)

#        print("Step #5")
#        speak1("Die aQua verbindet Arbeitssuchende und Unternehmen mit maßgeschneiderten Bildungsangeboten\
#        und passgenauen Dienstleistungen für unterschiedlichste Zielgruppen.")
#        misty.drive(linearVelocity=-0, angularVelocity=0)
#        misty.move_head(pitch=-20, roll=0, yaw=0) #
#        misty.move_arms(0,0)    
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)
    
#        print("Step #6")
#        speak3("Die aQua schafft Chancen, baut Brücken und begleiten Menschen sicher in den Arbeitsmarkt.")
#        misty.drive(linearVelocity=0, angularVelocity=10)
#        misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#        misty.move_arms(30,-30)
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)
    
#        print("Step #7")
#        speak2("Sind Sie neugierig? Sprechen Sie uns an!")
#        misty.drive(linearVelocity=0, angularVelocity=-5)
#        misty.move_head(pitch=-40, roll=0, yaw=0) #
#        misty.move_arms(30,-30) 
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)
    
#        print("Step #8")          
#        speak1("Unser Angebot richtet sich individuell nach den Bedürfnissen der Menschen,\
#        die wir begleiten für einen nachhaltigen Erfolg und echte Entwicklung.")
#        misty.drive(linearVelocity=-0, angularVelocity=5)
#        misty.move_head(pitch=-20, roll=0, yaw=0) #0
#        misty.move_arms(0,0)    
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)
    
#        print("Step #8")
#        speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
#        mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
#        misty.drive(linearVelocity=0, angularVelocity=-5)
#        misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#        misty.move_arms(30,-30)
#        sleep(4); reset_misty()
#        rnd = random.randint(10, 12);
#        countdown(rnd)

#        quit()
         
       

   

# os.system('cls')



# misty.register_event(event_name='face_detected', event_type=Events.FaceRecognition, callback_function=recognized, keep_alive=False)
# misty.keep_alive()
# sleep(360)
# quit()










# welcome = "Herzlich willkommen bei aqua, Wo Innovation auf Qualität trifft!"
# print(welcome+"\n"); speak1(welcome); sleep(4.0)

# while(True):

#     print("Step #1")
#     speak2("Schön, dass Sie da sind!  Entdecken  Sie  die  Welt  von   aQua,   effizient, nachhaltig  und  zukunftsorientiert.")
#     misty.drive(linearVelocity=0, angularVelocity=10)
#     misty.drive(linearVelocity=0, angularVelocity=-10)
#     misty.move_head(pitch=-20, roll=0, yaw=40) # 0
#     misty.move_arms(-30,30)
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)
    
#     print("Step #2")
#     speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
#     mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
#     misty.drive(linearVelocity=0, angularVelocity=-10)
#     misty.drive(linearVelocity=0, angularVelocity=10)
#     misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#     misty.move_arms(30,-30)
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)

#     print("Step #3")
#     speak1("aQua begrüßt Sie! Lassen  Sie sich von unseren Zukunftsperspektiven begeistern.")
#     misty.drive(linearVelocity=0, angularVelocity=10)
#     misty.move_head(pitch=-20, roll=0, yaw=0) #
#     misty.move_arms(-30,30)
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)

#     print("Step #4")
#     speak2("Sind Sie neugierig? Sprechen Sie uns an!")
#     misty.drive(linearVelocity=0, angularVelocity=-10)
#     misty.move_head(pitch=-40, roll=0, yaw=0) #
#     misty.move_arms(30,-30) 
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)

#     print("Step #5")
#     speak1("Die aQua verbindet Arbeitssuchende und Unternehmen mit maßgeschneiderten Bildungsangeboten\
#     und passgenauen Dienstleistungen für unterschiedlichste Zielgruppen.")
#     misty.drive(linearVelocity=-0, angularVelocity=0)
#     misty.move_head(pitch=-20, roll=0, yaw=0) #
#     misty.move_arms(0,0)    
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)
    
#     print("Step #6")
#     speak3("Die aQua schafft Chancen, baut Brücken und begleiten Menschen sicher in den Arbeitsmarkt.")
#     misty.drive(linearVelocity=0, angularVelocity=10)
#     misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#     misty.move_arms(30,-30)
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)
    
#     print("Step #7")
#     speak2("Sind Sie neugierig? Sprechen Sie uns an!")
#     misty.drive(linearVelocity=0, angularVelocity=-5)
#     misty.move_head(pitch=-40, roll=0, yaw=0) #
#     misty.move_arms(30,-30) 
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)
    
#     print("Step #8")          
#     speak1("Unser Angebot richtet sich individuell nach den Bedürfnissen der Menschen,\
#     die wir begleiten für einen nachhaltigen Erfolg und echte Entwicklung.")
#     misty.drive(linearVelocity=-0, angularVelocity=5)
#     misty.move_head(pitch=-20, roll=0, yaw=0) #0
#     misty.move_arms(0,0)    
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)
    
#     print("Step #8")
#     speak3("Die aQua ist Ihr Bildungsträger im Main-Kinzig-Kreis und begleitet Menschen\
#     mit passgenauer Qualifizierung und klaren Perspektiven auf dem Weg in die Arbeitswelt.")
#     misty.drive(linearVelocity=0, angularVelocity=-5)
#     misty.move_head(pitch=-20, roll=0, yaw=-40) # 0
#     misty.move_arms(30,-30)
#     sleep(4); reset_misty()
#     rnd = random.randint(10, 12);
#     countdown(rnd)

# quit()

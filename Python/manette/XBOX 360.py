import time
import pygame


def main():
    # Initialiser Pygame
    pygame.init()

    # Initialiser le joystick
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()




    try:
        print("Opérationnel !")
        while True:
            temp = 0.1
            # Gérer les événements Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Obtenir les valeurs des joysticks
            left_stick_x = joystick.get_axis(0)
            left_stick_y = joystick.get_axis(1)
            right_stick_x = joystick.get_axis(2)
            right_stick_y = joystick.get_axis(3)
            left_trigger = joystick.get_axis(4)
            right_trigger = joystick.get_axis(5)

            button_A = joystick.get_button(0)
            button_B = joystick.get_button(1)
            button_X = joystick.get_button(2)
            button_Y = joystick.get_button(3)

            button_LB = joystick.get_button(4)
            button_RB = joystick.get_button(5)

            button_XBOX = joystick.get_button(10)
            button_START = joystick.get_button(7)

            # Obtenir l'état du bouton X (remplacez 0 par le bon numéro de bouton si nécessaire)

            if (left_trigger > 0.5):  # reculer
                print("gachette gauche")
                time.sleep(0.1)


            elif (right_trigger > 0.5):  # avancer
                print("gachette droite")
                time.sleep(0.1)

            if left_stick_y < -0.8:
                print("Joystick 1: bas")
                time.sleep(0.1)

            elif left_stick_y > 0.8:
                print("Joystick 1: haut")
                time.sleep(0.1)


            # Si l'axe horizontal est incliné vers la droite
            elif left_stick_x > 0.8:
                print("Joystick 1: axe droite")
                time.sleep(0.1)
            elif left_stick_x < -0.8:
                print("Joystick 1: axe gauche")
                time.sleep(0.1)

                # Si l'axe vertical est incliné vers le haut
            elif right_stick_y < -0.8:
                print("Joystick 2: haut")
                time.sleep(0.1)

            elif right_stick_y > 0.8:
                print("Joystick 2: bas")
                time.sleep(0.1)


            # Si l'axe horizontal est incliné vers la droite
            elif right_stick_x > 0.8:
                print("Joystick 2: droite")
                time.sleep(0.1)
                
            elif right_stick_x < -0.8:
                print("Joystick 2: gauche")
                time.sleep(0.1)

            elif button_A:
                print("Bouton: A")

            elif button_X:
                print("Bouton: X")

            elif button_Y:
                print("Bouton: Y")

            elif button_B:
                print("Bouton: B")

            elif button_LB:
                print("Bouton: back")     
            
            elif button_XBOX:
                print("xbox")
            
            elif button_START:
                print("start")

            time.sleep(0.01)
    except KeyboardInterrupt:
        pygame.quit()


if __name__ == "__main__":
    main()

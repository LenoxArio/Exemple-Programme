import time
import pygame



def main():
    print("Load Server OK")
    # Initialiser Pygame
    pygame.init()

    # Initialiser le joystick
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    try:
        print("Opérationnel !")
        while True:
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

       
                
            print(right_trigger)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pygame.quit()


if __name__ == "__main__":
    # verif()
    main()

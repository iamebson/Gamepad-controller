import pygame

# Initialize Pygame
pygame.init()

# Initialize the joysticks
pygame.joystick.init()

# Get the number of connected joysticks
joystick_count = pygame.joystick.get_count()

# If at least one joystick is connected
if joystick_count > 0:
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    # Initialize the joystick
    joystick.init()
    # Get the name of the joystick
    joystick_name = joystick.get_name()
    print(f"Joystick connected: {joystick_name}")

    # Main loop
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            # If the user closes the window
            if event.type == pygame.QUIT:
                running = False
            # If a button on the joystick is pressed
            elif event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print(f"Button {button} pressed")
            # If a button on the joystick is released
            elif event.type == pygame.JOYBUTTONUP:
                button = event.button
                print(f"Button {button} released")
            # If an axis on the joystick is moved
            elif event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value
                print(f"Axis {axis} moved to {value}")

# Quit Pygame
pygame.quit()
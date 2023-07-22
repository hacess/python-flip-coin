import pygame
import random

pygame.init()

# Set up the screen
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flip a Coin')

# Load the coin image
coin_img = pygame.image.load('coin.png')
coin_img = pygame.transform.scale(coin_img, (100, 100))

# Coin properties
coin_center = (screen_width // 2, screen_height // 2)

# Function to draw the coin on the screen
def draw_coin():
    screen.blit(coin_img, (coin_center[0] - coin_img.get_width() // 2, coin_center[1] - coin_img.get_height() // 2))
    font = pygame.font.SysFont(None, 30)
    text = font.render("Press 'F' to flip the coin", True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - 130, screen_height - 50))

# Function to flip the coin
def flip_coin():
    return random.choice(['Heads', 'Tails'])

def main():
    clock = pygame.time.Clock()
    coin_result = None
    flip_animation = False
    flip_frame = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not flip_animation:
                    coin_result = flip_coin()
                    flip_animation = True
                    flip_frame = 0

        # Clear the screen
        screen.fill((255, 255, 255))

        if flip_animation:
            flip_frame += 1
            if flip_frame >= 20:  # Change animation speed by adjusting the value here
                flip_animation = False

        # Draw the coin or the flipped coin
        if flip_animation:
            rotated_coin = pygame.transform.rotate(coin_img, flip_frame * 18)  # Adjust the rotation speed here
            screen.blit(rotated_coin, (coin_center[0] - rotated_coin.get_width() // 2, coin_center[1] - rotated_coin.get_height() // 2))
        else:
            draw_coin()

        # Display the coin result
        if coin_result is not None and not flip_animation:
            font = pygame.font.SysFont(None, 50)
            text = font.render(coin_result, True, (0, 0, 0))
            screen.blit(text, (screen_width // 2 - 50, screen_height // 2 + coin_img.get_height() // 2 + 20))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
from pingpong.game import Game

# Initialize pygame
pygame.init()

# vars
HEIGHT = 500
WIDTH = 800
BLACK = (0,0,0)
WHITE = (255, 255, 255)

# set up display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ping-Pong AI Project')
clock = pygame.time.Clock()

# Create font for score display
font = pygame.font.SysFont('Arial', 32)

def drawGame(game: Game):
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    pygame.draw.rect(screen, WHITE, 
                    (game.player.pos_x + 10, game.player.pos_y, 
                    game.player.piece_width, game.player.piece_height))

    pygame.draw.rect(screen, WHITE, 
                    (game.agent.pos_x - 10, game.agent.pos_y, 
                    game.agent.piece_width, game.agent.piece_height))

    pygame.draw.circle(screen, WHITE, game.ball.coordinates, game.ball.radius)

    player_text = font.render(str(game.player.score), True, WHITE)
    agent_text = font.render(str(game.agent.score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(agent_text, (3*WIDTH//4, 20))

def main():
    game = Game(HEIGHT, WIDTH)

    running = True
    while running:
        key_input = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game.gameActive:
                    game.start_Game()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            key_input = "UP"
        elif keys[pygame.K_DOWN]:
            key_input = "DOWN"

        game.update(key_input)
        
        drawGame(game)


        pygame.display.flip()
        clock.tick(60)
                
    pygame.quit()

if __name__ == "__main__":
    main()
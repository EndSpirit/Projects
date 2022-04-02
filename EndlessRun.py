import pygame
import random as r

SC_WIDTH = 400
SC_HEIGHT = 800
bg_color = (237, 120, 202)
WITHE = (255, 255, 255)

clock = pygame.time.Clock()


class Game:

    TPS = 60

    def __init__(self,sc_title, height, width):
        self.width = width
        self.height = height
        self.title = sc_title

        self.game_sc = pygame.display.set_mode((width,height))
        self.game_sc.fill(bg_color)
        pygame.display.set_caption(self.title)


    def obstac_gen(self):
        t = []
        for i in range(4): 
            t.append(r.randint(0,1))
        if all(t):
            x = r.randint(0,3)
            t[x] = 0
        if not any(t):
            x = r.randint(0,3)
            t[x] = 1
        return t
   

    def run_game_loop(self):
        is_game_over = False
        direction = 0
        are_active = False

        text = "score: {}".format(0)
        score = 0

        player_character = GameChar(195, 575, 10, 10)

        while not is_game_over:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = 1
                    elif event.key == pygame.K_RIGHT:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        direction = 0

            if are_active == False:
                offseter = 0
                formut = 0
                dic = {}
                l = self.obstac_gen()
                for item in l:
                    offseter += 1 
                    if item != 0:
                        dic["obs{}".format(formut)] = Obstacle((100*(offseter))-98,-15,96,15)
                        formut += 1
                are_active = True
                      
                
                
                
            self.game_sc.fill(bg_color)

            check_list = list(dic.keys())

            for items in check_list:
                if player_character.detect_collision(dic["{}".format(items)]):
                    is_game_over = True
                dic["{}".format(items)].move()
                dic["{}".format(items)].draw(self.game_sc)
                
            
            player_character.move(direction,self.width)
            player_character.draw(self.game_sc)

            formater = ''.join(list(dic.keys()))
    
            if dic["obs{}".format(formater[3])].y_pos > 615:
                formater = ""
                score += 1
                print("score: {}".format(score))
                dic = {}
                are_active = False
                

            formater = ""
            pygame.display.update()
            clock.tick(self.TPS)





class GameChar:

    SPEED = 8

    def __init__(self, x, y, width, height):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw (self, bg):
        pygame.draw.rect(bg, WITHE,[self.x_pos, self.y_pos, self.width, self.height])

    def move(self, direct, width):
        if direct > 0:
            self.x_pos -= self.SPEED
        elif direct < 0:
            self.x_pos += self.SPEED

        if self.x_pos >= width -15:
            self.x_pos = width -15
        elif self.x_pos <= 5:
            self.x_pos = 5

    def detect_collision(self, other_entity):
        if self.y_pos > other_entity.y_pos + other_entity.height:
            return False
        elif self.y_pos + self.height < other_entity.y_pos:
            return False
        
        if self.x_pos > other_entity.x_pos + other_entity.width:
            return False
        elif self.x_pos + self.width < other_entity.x_pos:
            return False

        return True



class Obstacle:
    
    SPEED = 12

    def __init__(self, x, y, width, height):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, bg):
        pygame.draw.rect(bg, WITHE,[self.x_pos, self.y_pos, self.width, self.height])

    def move(self):
        self.y_pos += self.SPEED


pygame.init()

        

EndlessRun = Game("EndlessRun", 600, 400)   
EndlessRun.run_game_loop()    
    

pygame.quit()
quit()

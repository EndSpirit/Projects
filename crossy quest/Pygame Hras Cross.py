import pygame

SC_WIDTH = 800
SC_HEIGHT = 800
color_black = (0, 0, 0)
color = (170, 85, 175)



clock = pygame.time.Clock()


class Game:
    
    TPS = 60
    

    def __init__(self,image_p,width,height,title):
        self.title = title
        self.width = width
        self.height = height
        
        self.game_sc = pygame.display.set_mode((width,height))
        self.game_sc.fill(color)
        pygame.display.set_caption(title)

        bg_image = pygame.image.load(image_p)
        self.image =  pygame.transform.scale(bg_image,(width,height))
        
    def run_game_loop(self, lv_sp, lv):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter("player.png", 375, 750, 50, 50)
        
        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)
        enemy_0.SPEED *= lv_sp
        if lv >= 3:
            enemy_1 = EnemyCharacter('enemy.png', self.width - 20, 150, 50, 50)
            enemy_1.SPEED *= lv_sp
        if lv >= 6:
            enemy_2 = EnemyCharacter('enemy.png', self.width - 20, 650, 50, 50)
            enemy_2.SPEED *= lv_sp
        if lv >= 9:
            enemy_3 = EnemyCharacter('enemy.png',20 , 275, 50, 50)
            enemy_3.SPEED *= lv_sp
        if lv >= 12:
            enemy_4 = EnemyCharacter('enemy.png',self.width - 20 , 525, 50, 50)
            enemy_4.SPEED *= lv_sp
            
        treasure = GameObject("treasure.png", 375, 50, 50, 50)

        
        while not is_game_over:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                

            
            self.game_sc.fill(color)
            self.game_sc.blit(self.image,(0,0))
            

            treasure.draw(self.game_sc)
            
            
            player_character.move(direction,self.height)
            player_character.draw(self.game_sc)
            enemy_0.move(self.width)
            enemy_0.draw(self.game_sc)
            if lv >= 3:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_sc)
                if player_character.detect_collision(enemy_1):
                    is_game_over = True
                    did_win = False
                    break
            if lv >= 6:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_sc)
                if player_character.detect_collision(enemy_2):
                    is_game_over = True
                    did_win = False
                    break
            if lv >= 9:
                enemy_3.move(self.width)
                enemy_3.draw(self.game_sc)
                if player_character.detect_collision(enemy_3):
                    is_game_over = True
                    did_win = False
                    break
            if lv >= 12:
                enemy_4.move(self.width)
                enemy_4.draw(self.game_sc)
                if player_character.detect_collision(enemy_4):
                    is_game_over = True
                    did_win = False
                    break

            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                break
            

            
            
            pygame.display.update()
            clock.tick(self.TPS)

        if did_win:
            self.run_game_loop(lv_sp + 0.1, lv+1)
            
        else:
            self.run_game_loop(lv_sp, lv)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        
        object_image = pygame.image.load(image_path)
        self.texture = pygame.transform.scale(object_image,(width,height))

    def draw(self, background):
        background.blit(self.texture, (self.x_pos,self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 10 

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direct, height):
        if direct > 0:
            self.y_pos -= self.SPEED
        elif direct < 0:
            self.y_pos += self.SPEED


        if self.y_pos >= height -55:
            self.y_pos = height -55

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


class EnemyCharacter(GameObject):

    SPEED = 10 

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= width -60:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        







pygame.init()



crossy_game = Game("background.png",800,800,"Crossy-RPG")
crossy_game.run_game_loop(0.4, 0)


pygame.quit()
quit()

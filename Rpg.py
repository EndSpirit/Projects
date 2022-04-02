import random as r
import os

def sep():
    print("=====================")

# main quest line |X|
""" level system |done|"""
""" random encouters |done|"""
""" turnbased combat |done| """
""" 3 classes |done| """
# side quests |X|
""" random items |done|"""
""" grind zone |done| """
""" save system |done|"""
# player actions |X|
# more monster types |X|
""" status effects |done|"""
""" special abilities |done|"""







 


class Encounter:

    def __init__(self, player, enemy_count):
        self.not_clear = True
        self.died = False
        self.monsters = {}
        for mons in range(enemy_count):
            choice = r.choice(({"SkeletonArcher_{}".format(mons+1):Monster(skeli_atrib, skeli)}, {"Zombie_{}".format(mons+1):Monster(zomb_atrib, zomb)}, {"Slime_{}".format(mons+1):Monster(slime_atrib, slime)}))
            self.monsters[list(choice.keys())[0]] = choice[list(choice.keys())[0]]
        print("You are going against: " + ", ".join(list(self.monsters.keys())))
        sep()
        while True:
            self.player_turn(player)
            self.monsters_turn(player)
            if self.not_clear == False:
                break

    def player_turn(self, player):
        chc = str(input("Do you want to attack(a), heal(h), use a special ability(s) or quit with a save(q): ")).lower()
        if chc == "a":
            sep()
            print("you can attack these monsters: " + ", ".join(list(self.monsters.keys())))
            selected = input("Choose wisely: ")
            sep()
            try:
                attack = player.attack()
                if attack - self.monsters[selected].Def > 0:
                    self.monsters[selected].CurHp -= (attack - self.monsters[selected].Def)
                if self.monsters[selected].is_alive():
                    print("You did " + str((attack - self.monsters[selected].Def)) +" damage!")
                    print("The monster now has: " + str(self.monsters[selected].CurHp) + " HP!")
                    sep()
                else:
                    print("The monster died!")
                    player.exp += self.monsters[selected].exp_reward
                    player.level_up()
                    sep()
                    del self.monsters[selected]
                    if not self.monsters:
                        print("You cleared the encounter!")
                        sep()
                        self.not_clear = False
            except:
                print("That monster doesn't exist!")
                self.player_turn(player)
        elif chc == "s":
            try:
                if player.Lv < 3:
                    print("You don't have any abilities yet!")
                    self.player_turn(player)
                alls = list(player.specials.keys())
                abl = [key for key in alls if key <= player.Lv]
                a = " {} turns, ".format(player._3cool)
                b = " {} turns, ".format(player._7cool)
                b7 = " {} turns!".format(player._7cool)
                a3 = " {} turns!".format(player._3cool)
                if player.Lv >= 3 and player.Lv < 7:
                    print("Cooldowns: " + str(player.specials[abl[0]]) + a3)
                    abl_chc = input("You can choose between: " + str(player.specials[abl[0]]) + "(1)!")
                elif player.Lv >= 7 and player.Lv < 12:
                    print("Cooldowns: " + str(player.specials[abl[0]]) + a + str(player.specials[abl[1]]) + b7)
                    abl_chc = input("You can choose between: " + str(player.specials[abl[0]]) + "(1), " + str(player.specials[abl[1]]) + "(2)!")
                elif player.Lv >= 12:
                    print("Cooldowns: " + str(player.specials[abl[0]]) + a + str(player.specials[abl[1]]) + b + str(player.specials[abl[2]]) + " {} turns!".format(player._12cool))
                    abl_chc = input("You can choose between: " + str(player.specials[abl[0]]) + "(1), " + str(player.specials[abl[1]]) + "(2), " + str(player.specials[abl[2]]) + "(3)!")
                chck = player.cools()
                if chck[int(abl_chc) - 1] > 0:
                    print("That ability is on cooldown!")
                    self.player_turn(player)
                print("You can use it on these monsters: " + ", ".join(list(self.monsters.keys())))
                selected = input("Choose wisely: ")
                player.special_attack(self.monsters[selected], abl_chc)
                if self.monsters[selected].is_alive() and abl_chc != "2":
                    print("The monster now has: " + str(self.monsters[selected].CurHp) + " HP!")
                    sep()
                elif self.monsters[selected].is_alive():
                    sep()
                    pass
                else:
                    print("The monster died!")
                    player.exp += self.monsters[selected].exp_reward
                    player.level_up()
                    sep()
                    del self.monsters[selected]
                    if not self.monsters:
                        print("You cleared the encounter!")
                        sep()
                        self.not_clear = False
            except:
                print("That action doesn't exist!")
                self.player_turn(player)
        elif chc == "h":
            player.heal()
            print("You now have " + str(player.CurHp) + " HP!")
            sep()
        elif chc == "q":
            player.save()
            quit()
        else:
            print("That action doesn't exist!")
            sep()
            self.player_turn(player)
        
    def monsters_turn(self, player):
        player.cool()
        for monster in list(self.monsters.keys()):
            self.monsters[monster].check_conditions(monster)
            if self.monsters[monster].is_alive() and self.monsters[monster].conditions:
                print("The "+ monster +" now has: " + str(self.monsters[monster].CurHp) + " HP!")
                sep()
                print("The " + monster + " attacked!")
                attack = self.monsters[monster].attack()
                if  attack - player.Def > 0:
                    player.CurHp -= (attack - player.Def)
                    print("It did "+ str((attack - player.Def)) +" damage!")
                if player.is_alive():
                    print("You now have: " + str(player.CurHp) + " HP!")
                    sep()
                else:
                    print("You died!")
                    self.not_clear = False
                    self.died = True
                    sep()
            elif self.monsters[monster].is_alive():
                print("The " + monster + " attacked!")
                attack = self.monsters[monster].attack()
                if  attack - player.Def > 0:
                    player.CurHp -= (attack - player.Def)
                    print("It did "+ str((attack - player.Def)) +" damage!")
                if player.is_alive():
                    print("You now have: " + str(player.CurHp) + " HP!")
                    sep()
                else:
                    print("You died!")
                    self.not_clear = False
                    self.died = True
                    sep()
            else:
                print("The " + monster + " died!")
                player.exp += self.monsters[monster].exp_reward
                player.level_up()
                sep()
                del self.monsters[monster]
                if not self.monsters:
                    print("You cleared the encounter!")
                    sep()
                    self.not_clear = False
                

    
class Player:

    def __init__(self, HP, DEF, ATT, Lv, class_mod, wep_arm_mods):
        self.exp = 0
        self.class_mod = class_mod
        self.DEF = DEF
        self.ATT = ATT
        self.HP = HP
        self.wep_arm_mods = wep_arm_mods
        self.CurHp = round((HP * class_mod[0] + (1 + class_mod[0]*(Lv-1))) * wep_arm_mods[1], 0 )
        self.MaxHp = round((HP * class_mod[0] + (1 + class_mod[0]*(Lv-1))) * wep_arm_mods[1], 0 )
        self.Def = round((DEF + (1 + class_mod[2]*(Lv-1))) * wep_arm_mods[1], 0)
        self.Att = round((ATT * class_mod[1] + (1 + class_mod[1]*(Lv-1))) * wep_arm_mods[0], 0)
        self.Lv = Lv
        self.conditions = {}
        self.specials = {}
        self._3cool = 0
        self._7cool = 0
        self._12cool = 0
        self.specs()
        sep()
        
    def stats(self):
        print("You have: "+ str(int(self.Att))+" Att, " + str(int(self.MaxHp))+" MaxHp, ", str(self.Def) + " Defence!")

    def specs(self):
        if self.class_mod[3] == "Ra":
            self.specials = {3:"HeadShot", 7:"FlameArrow", 12:"Voley"}
        if self.class_mod[3] == "Ro":
            self.specials = {3:"BackStab", 7:"PoisonousDagger", 12:"28STABWOUNDS"}
        if self.class_mod[3] == "Wa":
            self.specilas = {3:"MightyBlow", 7:"HolyStand", 12:"FrenziedSwings"}

    
    def is_alive(self):
        if self.CurHp > 0:
            return True
        else:
            return False

    def level_up(self):
        print("You now have: " + str(self.exp) + " exp!")
        if self.Lv * 135  <= self.exp:
            self.exp -= self.Lv * 135
            self.Lv += 1
            print("you have " + str(self.exp) + " exp remaining after level up!")
            print("You are now level " + str(self.Lv))
            self.update_stats()
    
    def special_attack(self, ent, choice):
        if choice == '1':
            print("You use the " + str(self.specials[3]) + "!" )
            dmg = round(self.Att * 1.5, 0)
            ent.CurHp -= dmg
            print("You deal " + str(dmg) + " damage!")
            self._3cool = 3
            print("This ability is now on cooldown for 3 turns")
        
        if choice == '2':
            print("You use the " + str(self.specials[7]) + "!" )
            dmg = round(self.Att * 0.8, 0)
            ent.CurHp -= dmg
            dur = r.randint(2, 6)
            print("You deal " + str(dmg) + " damage and apply an over-time damage effect for " + str(dur) + " turns!")
            ent.conditions[r.randint(0, 5)] = ["tick_dmg", round(self.Att/2, 0), dur]
            self._7cool = 5
            print("This ability is now on cooldown for 5 turns")
        
        if choice == '3':
            print("You use the " + str(self.specials[12]) + "!" )
            amn = r.randint(2, 28)
            dmg = round(self.Att * amn , 0)
            ent.CurHp -= dmg
            print("You violently slash " + str(amn) + " times and...")                                      
            print("You deal " + str(dmg) + " damage!")
            self._12cool = 7
            print("This ability is now on cooldown for 7 turns")
    
    def attack(self):
        return r.randint(int(self.Att) - 2, int(self.Att) + 2)

    def heal(self):
        heal_am =r.randint(int(round(5 + 1 + self.class_mod[0]*(self.Lv-1))),int(round(8 + 1 + self.class_mod[0]*(self.Lv-1))))
        if self.CurHp + heal_am < self.MaxHp:
            self.CurHp += heal_am
        elif self.CurHp + heal_am >= self.MaxHp:
            self.Curhp = self.MaxHp

    def update_stats(self):
        self.CurHp = round((self.HP * self.class_mod[0] + (1 + self.class_mod[0]*(self.Lv-1))) * self.wep_arm_mods[1], 0 )
        self.MaxHp = round((self.HP * self.class_mod[0] + (1 + self.class_mod[0]*(self.Lv-1))) * self.wep_arm_mods[1], 0 )
        self.Def = round((self.DEF + (1 + self.class_mod[2]*(self.Lv-1))) * self.wep_arm_mods[1], 0)
        self.Att = round((self.ATT * self.class_mod[1]  + (1 + self.class_mod[1]*(self.Lv-1))) * self.wep_arm_mods[0], 0)

    def save(self):
        f = open("save_file", "w")
        f.write(str(self.class_mod[:-1]) + "\n")
        f.write(str(self.Lv) + "\n")
        f.write(str(self.exp) + "\n")
        f.write(str(self.wep_arm_mods) + "\n")
        f.write(str(self.class_mod[-1]))
        f.close()

    def load(self):
            f = open("save_file", "r")
            zaznami = f.readlines()
            f.close()
            for i in range(0,4):
                zaznami[i] = zaznami[i][:-1]
            for i in range(0,5):
                zaznami[i] = zaznami[i].strip("[")
                zaznami[i] = zaznami[i].strip("]")
                zaznami[i] = zaznami[i].strip("'")
            zaznami[0] = list(map(float, zaznami[0].split(", ")))
            zaznami[0].append(zaznami[4])
            zaznami[3] = list(map(float,zaznami[3].split(", ")))
            zaznami[2] = float(zaznami[2])
            zaznami[1] = float(zaznami[1])
            self.class_mod = zaznami[0] 
            self.wep_arm_mods = zaznami[3]
            self.exp = zaznami[2] 
            self.Lv = zaznami[1]
            self.update_stats()
            self.stats()

    def cool(self):
        if self._3cool > 0:
            self._3cool -= 1
        if self._7cool > 0:
            self._7cool -= 1
        if self._12cool > 0:
            self._12cool -= 1

    def cools(self):
        return (self._3cool, self._7cool, self._12cool)

    def die(self):
        os.remove("save_file")
        
        
             

class Monster():

    def __init__(self, monster_atrib, monster_mod):
        self.Lv = monster_atrib[3].Lv
        self.CurHp = round(monster_atrib[0] * monster_mod[0] + (1 + monster_mod[0]*(self.Lv-1)), 0 )
        self.MaxHp = round(monster_atrib[0] * monster_mod[0] + (1 + monster_mod[0]*(self.Lv-1)), 0 )
        self.Def = round(monster_atrib[1] + (1 + monster_mod[1]*(self.Lv-1)), 0)
        self.Att = round(monster_atrib[2] * monster_mod[1] + (1 + monster_mod[1]*(self.Lv-1)), 0)
        self.exp_reward = monster_atrib[4] + (1 + 0.5 * (self.Lv - 1))
        self.conditions = {}

    def is_alive(self):
        if self.CurHp > 0:
            return True
        else:
            return False

    def attack(self):
        return r.randint(self.Att - 2, self.Att + 2)

    def check_conditions(self, name):
        for key in list(self.conditions.keys()):
            if self.conditions[key][0] == 'tick_dmg' and self.conditions[key][2] > 0:
                print("The "+ name +" suffered " + str(self.conditions[key][1]) + " tick damage!")
                self.CurHp -= self.conditions[key][1]
                self.conditions[key][2] -= 1
            elif self.conditions[key][0] == 'tick_dmg' and self.conditions[key][2] == 0:
                del self.conditions[key]
                print("The effect wore out!")



if "save_file" not in os.listdir():
    print("Welcome to All the Literature Online or ALO for short!")
    class_chc = input("Select you class: Ranger, Warrior, Rouge: ")
    if class_chc == "Ranger":
        c = [0.85, 1.2, 0.45, "Ra"]
    if class_chc == "Warrior":
        c = [1.35, 0.9, 0.72, "Wa"]  
    if class_chc == "Rouge":
        c = [0.65, 1.6, 0.30, "Ro"]
    if class_chc == "g69d":
        c = (69, 69, 69)
    Pl = Player(30, 3, 6, 1, c, [1, 1])
    Pl.save()
    Pl.stats()   
elif "save_file" in os.listdir():
    Pl = Player(30, 3, 6, 1, [0.65, 1.6, 0.30, "Ro"], [1, 1])
    print("Welcome back you are now playing as your saved character!")
    Pl.load()





zomb = (1.1, 0.9)
zomb_atrib = (20,2,4,Pl,45)
skeli = (0.6, 1.3)
skeli_atrib = (16,1,7,Pl,50)
slime = (1.65, 0.5)
slime_atrib = (19,4,2,Pl,40)



def grind_zone():
    x = -1
    encs = {}
    while True:
        x += 1 
        encs["Encounter{}".format(x)] = Encounter(Pl, r.randint(1, 3))
        if encs["Encounter{}".format(x)].not_clear == False and encs["Encounter{}".format(x)].died == False:
            del encs["Encounter{}".format(x)]
            Pl.save()
            if r.randint(0,2) == 0:
                wep_arms = (round(r.uniform(0,2), 1),round(r.uniform(0,2), 1))
                print(("Currnet weapon modifier is: " + str(Pl.wep_arm_mods[0]) + " and armor modifier is: " + str(Pl.wep_arm_mods[1]) + "!"))
                print("New found weapon modifier is: " + str(wep_arms[0]) + " and armor modifier is: " + str(wep_arms[1]) + "!")
                inp = input("Equip this weapon and Armor y/n? ")
                if inp == "y":
                    Pl.wep_arm_mods = wep_arms
                    Pl.update_stats()
                    print("Your Att is now: " + str(Pl.Att))
                    print("YOur MaxHP is now: " + str(Pl.MaxHp))
            for i in range(8):
                Pl.cool()
            print("Your cooldowns have been reset!")
            q_chc = input("Proceed to the next grinding encounter, if yes press ENTER!")
            sep()
            if q_chc != "":
                break
        else:
            quit()


grind_zone()


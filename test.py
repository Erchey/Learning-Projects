import random
class Enemy():
    
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy =  type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    def talk(self):
        print('I am an enemy')
    
    def get_enemy(self):
        return self.__type_of_enemy
        
    def sleep(self):
        print('Animal sleeping')

class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)
        

    def talk(self):
        print('Grumbling')

    def attack(self):
        print(f'{self.get_enemy()} has {self.health_points} health point and {self.attack_damage} attack')

    def special_skill(self):
        did_special_skill_work = random.random() > 0.5
        if did_special_skill_work:
            self.health_points += 2


zombie = Zombie(100, 10)
zombie.special_skill()
zombie.attack()


    


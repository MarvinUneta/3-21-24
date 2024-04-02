class Player:
    def __init__(self, player_name: str, player_health: int, player_attack_power: int):
        self.__player_name = player_name
        self.__player_health = player_health
        self.__player_attack_power = player_attack_power

    def attack(self):
        pass

    @property
    def player_take_damage(self):
        return self.__player_attack_power
    
    @player_take_damage.setter
    def player_take_damage(self, player_attack_health):
        pass

class Monster:
    def __init__(self, monster_name: str, monster_health: int, monster_attack_power: int):
        self.__monster_name = monster_name
        self.__monster_health = monster_health
        self.__monster_attack_power = monster_attack_power

    def attack(self):
        pass

    @property
    def monster_health(self):
        return self.__monster_health

    @property
    def monster_take_damage(self):
        pass

    @monster_take_damage.setter
    def monster_take_damage(self, monster_new_health: int):
        self.__monster_attack_power-= monster_new_health


Player1 = Player(player_name = 'jaydee', player_health = 100, player_attack_power = 10)
Monster1 = Monster(monster_name = 'james', monster_health = 50, monster_attack_power = 7)

print(f'Monster current health: {Monster1.monster_health}')
Player1.attack()
print(f'Monster updated health: {Monster1.monster_health - Player1.player_take_damage}')
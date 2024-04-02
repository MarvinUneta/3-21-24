Create two classes: Player and Monster

Below are the instructions for the activity.


Player class:
    Attributes:
        - name
        - health
        - attack_power
        - monster
        # these attributes are encapuslated (private)
   
    Methods:
        - attack():
            - this method, when called, reduces the health of the Monster object based on the attack_power attribute of the Player.

        - take_damage():
            - there are two take_damage() methods, getter and setter. this method is the one who operates on reducing the player's health when attacked by the Monster object.

        - is_alive():
            - this method returns True if the player's health is positive, False otherwise.

Monster class:
    Attributes:
        - name
        - health
        - attack_power
        # these attributes are encapuslated (private)
   
    Methods:
        

- attack():
            - this method, when called, reduces the health of the Player object based on the attack_power attribute of the Monster.

        - take_damage():
            - there are two take_damage() methods, getter and setter. this method is the one who operates on reducing the monster's health when attacked by the Player object.

        - is_alive():
            - this method returns True if the player's health is positive, False otherwise.

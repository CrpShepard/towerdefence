import params

class PlayerStats():
    base_lives = None
    gold = None
    towers = None

    def init(self, level):
        self.base_lives, self.gold, self.towers = params.set_level_params(level)

    def receiveDamage(self, damage):
        self.base_lives -= damage
        self.checkHealth()

    def checkHealth(self):
        if self.base_lives < 1:
            self.death()
        else:
            pass
            #print('Base lives remains:', self.base_lives)

    def death(self):
        print('GAME OVER!')

    def receiveGold(self, gold):
        self.gold += gold
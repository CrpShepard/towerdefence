tower_cell_size = 40

screen_width = 1280
screen_height = 720

game_area_width = 1280
game_area_height = 560

def set_level_params(level):
    base_lives = 0
    gold = 0
    towers = set()
    if level == 0:
        base_lives = 999
        gold = 100
        towers = {'Rifle'}
        return (base_lives, gold, towers)

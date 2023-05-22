import pygame
from Entities import Player, enemy
from Display import Block, Coin

#0 - PLAYER, 1 - GRASS, 2 - COIN, 3 - ENEMY, 4 - ICE, 5 - LAVA, 6 - MUD, 7 -TRAMPOLINE, 8 - CRATE, 9 - FINISH


def parseLvl(file, map):
    with open(file, 'r') as f:
        for line in f:
            vars = line.split(" ")
            x = (int(vars[0])-1)*50
            y = map.DISPLAY_H-int(vars[1])*50
            id = int(vars[2])
            #construktors = [block.grass, coin.coin...]
            match id:
                case 0:
                    map.player = Player.Player(x, y)
                case 1:
                    map.blocks.append(Block.Grass(x, y))
                case 2:
                    map.coins.append(Coin.Coin(x, y))
                case 3:
                    map.enemies.append(enemy.EnemyMlee(x, y))
                case 4:
                    map.blocks.append(Block.Ice(x, y))
                case 5:
                    map.blocks.append(Block.Lava(x, y))
                case 6:
                    map.blocks.append(Block.Mud(x,y))
                case 7:
                    map.blocks.append(Block.Trampoline(x, y))
                case 8:
                    map.blocks.append(Block.Crate(x, y))
                case 9:
                    map.finish = Block.Finish(x, y)
                case 10:
                    map.enemies.append(enemy.EnemyArcher(x,y))
            
            
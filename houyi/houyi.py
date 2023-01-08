from aa.game.game import Game
class Houyi(Game):
    # 如果在子类中重新定义了__init__，那么父类的__init__将会被覆盖
    def __init__(self,):
        super().__init__(hp,power)
        self.defense = 3

    def houyi_fight(self,enermy_hp,enermy_power):
        while True:
            print(f"回合计算之前——我的血量是{self.hp}")
            print(f"回合计算之前——敌人的血量是{enermy_hp}")
            self.hp = self.hp - enermy_power + self.defense
            print(f"2-我的血量是{self.hp}")
            enermy_hp = enermy_hp - self.power
            print(f"2-敌人的血量是{enermy_hp}")
            if self.hp<=0:
                print("后裔输了")
                break
            elif enermy_hp <= 0:
                print("后裔赢了")
                break


hp = 5
power = 2
print("--------------这里是第一个game-------------------")
# game = Game(hp,power)
# game.fight(2000,200)

print("--------------这里是后裔的游戏-------------------")
houyi = Houyi()
houyi.houyi_fight(enermy_hp=4,enermy_power=2)

print("--------------这里修改了护甲属性-------------------")
# houyi.defense = 1000
# houyi.houyi_fight(2000,200)
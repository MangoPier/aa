class Game:
    def __init__(self,hp,power): # 将角色的hp、power通过传参传入
        self.hp = hp
        self.power = power

    def fight(self,enermy_hp,enermy_power):
        final_hp = self.hp - enermy_power
        enermy_final_hp = enermy_hp - self.power
        if final_hp > enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("我赢了")
        elif final_hp < enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("敌人赢了")
        else:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("平局")

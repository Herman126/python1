
# 用户



class Card:
    def __init__(self,card_id,password,money,islock=False):
        self.card_id = card_id
        self.password = password
        self.money = money  # 余额
        self.islock = islock

    def __repr__(self):
        return f'卡号:{self.card_id}, 密码:{self.password}, 余额:{self.money}, 状态:{self.islock}'
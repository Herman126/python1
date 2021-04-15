# 用户信息

class User:
    def __init__(self,name,phone,idcard,card):
        self.name = name  # 用户
        self.phone = phone  # 手机号码
        self.idcard = idcard  # 身份证号码
        self.card = card  # 银行卡对象

    def __repr__(self):
        return f'姓名:{self.name},号码:{self.phone},身份证:{self.idcard},银行卡:({self.card})'
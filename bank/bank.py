# 银行的操作
#  开户,查询,存款,取款,改密,锁卡,解锁,补卡,销户
from cards import Card
from users import User
import random
import pickle
import os


class Bank:
    def __init__(self):
        pass
        self.users = []  # 当前银行的所有用户
        self.file_path = 'users.txt'  # 本地文件路径
        # 启动银行系统后,立即获取users.txt文件中所有用户
        self.__get_users()
        print('=>原来的所有用户:', self.users)

    # 保存用户对象到文件中
    def __save_users(self):
        # 写入文件
        fp = open(self.file_path, 'wb')
        pickle.dump(self.users, fp)
        fp.close()
        print('=>原来的所有用户:', self.users)

    # 每次运行项目都要重新获取users.txt文件中的所有用户
    def __get_users(self):
        # 读取文件
        if os.path.exists(self.file_path):
            fp = open(self.file_path, 'rb')
            self.users = pickle.load(fp)
            fp.close()

    # ----------------------------华丽的分割线---------------------

    # 开户
    def create_user(self):
        pass
        # 1.创建卡
        # 卡号
        cardid = self.__create_cardid()
        print('=>成功创建卡号:', cardid)
        # 卡的密码
        passwd = self.__set_password()
        if not passwd:
            return
        # 卡的余额
        money = float(input('请您要预存的金额:'))
        # 创建卡对象
        card = Card(cardid, passwd, money)
        print('=>创建卡成功:', card)

        # 2.创建用户
        name = input('请输入您的真实姓名:')
        idcard = input('请输入您的身份证号码:')
        phone = input('请输入您的手机号码:')
        # 创建用户对象
        user = User(name, phone, idcard, card)
        print('=>创建用户成功:', user)

        # 3.将新用户存储
        # 将新用户加入到银行系统中
        self.users.append(user)
        # 存储
        self.__save_users()

    # 创建随机唯一的卡号
    def __create_cardid(self):
        while True:
            # 生成随机卡号
            cardid = '8888'
            for i in range(4):
                cardid += str(random.randint(0, 9))

            # 如果有一个用户的卡号和cardid相同,则break继续执行while,否则返回cardid
            for user in self.users:
                if user.card.card_id == cardid:
                    break
            else:
                return cardid

    # ----------------------------华丽的分割线---------------------
    # 设置密码
    def __set_password(self):
        # 允许输错3次
        for i in range(3):
            passwd = input('请您输入密码:')
            passwd2 = input('请确认密码:')
            # 验证两次密码是否一致
            if passwd == passwd2:
                return passwd
            print('=>2次密码不一致请重新输入...')
        else:
            print("=>您输错了三次密码,请联系工作人员")
            return False

    # 查询
    def search_monky(self):
        pass
        # 1. 输入卡号
        user = self.__input_cardid()
        if not user:
            print('=>卡号不存在.')
            return

        # 2. 输入密码: 考虑允许输错3次,否则锁卡
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.password:
            print('=>密码错误')
            return

        # 3. 显示余额
        print('=>当前余额:', user.card.money)

    # 输入卡号
    def __input_cardid(self):
        cardid = input('请输入您的银行卡号:')

        # 如果卡号现在,则返回所在的用户对象,否则默认返回None
        for user in self.users:
            if user.card.card_id == cardid:
                return user

    # 输入身份证
    def __input_idcard(self):
        idcard = input('请输入您的身份证:')
        for user in self.users:
            if user.idcard == idcard:
                return user

    # ----------------------------华丽的分割线---------------------
    # 存款
    def save_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.password:
            print('=>密码错误')
            return
        # 3.输入存款金额,并将user.card.money+=
        add_money = float(input('请输入您要存入的金额:'))
        user.card.money += add_money
        print("=>成功存入{add_money}元")
        # 4.self.__save_users()
        self.__save_users()

    # 取款
    def get_money(self):
        pass

        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.password:
            print('=>密码错误')
            return
        # 3.输入取款金额,并将user.card.money-=
        pay_money = float(input('请输入您要取出的金额:'))
        if pay_money > user.card.money:
            print("=>余额不足")
            return
        user.card.money -= pay_money
        print("=>成功取出{pay_money}元")
        # 4.self.__save_users()
        self.__save_users()

    # ----------------------------华丽的分割线---------------------
    # 转账
    def transform_money(self):
        pass

        # 1.输入转出的卡号
        user = self.__input_cardid()
        if not user:
            return
        # 2.输入输出卡号的密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.password:
            print('=>密码错误')
            return
        # 3.对方卡号
        other_cardid = self.__input_cardid()
        if not other_cardid:
            print("=>对不起,查询不到该卡号")
        # 4.输入存款金额,并将自己的user.card.money-=
        money = float(input('请输入转账金额:'))
        if money > user.card.money:
            print('=>余额不足')
            return
        user.card.money -= money
        #     并将对方的user.card.money +=
        other_cardid.card.money += money
        # 5.self.__save_users()
        self.__save_users()

    # 改密:
    def modify_password(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            return
        # 2.输入身份证
        id_card = input('请输入您的身份证:')
        if id_card != user.idcard:
            print('=>身份证有误!')
            return
        # 3.输入旧密码,再输入新密码
        passwd1 = input('请输入旧密码:')
        if passwd1 != user.card.password:
            print('=>密码有误')
            return
        passwd2 = input('请输入新密码:')
        user.card.password = passwd2
        print('=>密码修改成功!')
        # 4.self.__save_users()
        self.__save_users()

    # ----------------------------华丽的分割线---------------------
    # 锁卡
    def lock_card(self):
        pass

        # 1.输入卡号

        user = self.__input_cardid()
        if not user:
            return
        # 2.输入密码
        passwd = input('请输入密码:')
        if passwd != user.card.password:
            print('=>密码有误')
            return
        # 3.锁卡: user.card.islock= True
        user.card.islock = True
        print('=>该卡已锁定')
        # 4.self.__save_users()
        self.__save_users()

    # 解锁
    def unlock_card(self):
        pass

        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            return
        # 2.输入密码
        passwd = input('请输入密码:')
        if passwd != user.card.password:
            print('=>密码有误')
            return
        # 3.解卡: user.card.islock= False
        user.card.islock = False
        print('=>该卡已解锁')
        # 4.self.__save_users()
        self.__save_users()

    # ----------------------------华丽的分割线---------------------
    # 补卡
    def makeup_card(self):
        global user
        pass

        # 1.输入身份证
        user = self.__input_idcard()
        if not user:
            return
        # 2.创建新卡,并替换旧卡
        cardid = self.__create_cardid()
        print('=>成功创建新卡号:', cardid)
        user.card.card_id = cardid
        # 卡的密码
        passwd = self.__set_password()
        if not passwd:
            return
        user.card.password = passwd
        # 3.self.__save_users()
        self.__save_users()

    # 销户
    def delete_user(self):
        pass
    # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            return
    # 2.输入密码
        passwd = input('请输入密码:')
        if passwd != user.card.password:
            print('=>密码有误')
            return
    # 3. 删除该用户所有信息
        self.users.remove(user)
        print('=>您已销户')
    # 4.self.__save_users()
        self.__save_users()
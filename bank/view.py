
# 界面
import time
class View:


    @classmethod
    def welcome_view(cls):
        print('*'*35)
        print("*****                         *****")
        print("*****          世界银行       *****")
        print("*****          V1.0           *****")
        print("*****          欢迎光临       *****")
        print("*****          世界银行       *****")
        print("*****                         *****")
        print("***** 贪玩蓝月:是兄弟就来砍我 *****")
        print("*****                         *****")
        print('*'*35)

        time.sleep(0.2)

    @classmethod
    def login(cls):
        # 模拟用户
        user = {'zhangsan':'123456'}
    # 输入用户名
        user_name = input("请输入用户名:")
        if user_name not in user:
            print("=>用户名不存在")
            return
        # 输入密码
        password = input("请输入密码:")
        if user[user_name] != password:
            print("=>密码错误")
            return
        # 登陆成功
        print("=>恭喜你!登录成功,正在加载主页面...")
        time.sleep(1)
        return True

        # 主界面
    @classmethod
    def main_view(cls):
        # 世界银行
        # 开户,查询,存款,取款,改密,锁卡,解锁,补卡,销户,提出
        print('*'*40)
        print('*'*5," "*20,'*'*5)
        print("*****    世界银行主界面功能      *****")
        print("*****    (1)开户     (2)查询     *****")
        print("*****    (3)存款     (4)取款     *****")
        print("*****    (5)转账     (6)改密     *****")
        print("*****    (7)锁卡     (8)解锁     *****")
        print("*****    (9)补卡     (0)销户     *****")
        print("*****            (q)退出         *****")
        print('*' * 40)
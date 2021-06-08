import os
import pickle
import random
import time


class Account:
    def __init__(self, name, identity_id, card):
        self.name = name
        self.identity_id = identity_id
        self.card = card

    def __str__(self):
        return "名字:" + str(self.name) + " 身份证:" + str(self.identity_id) + " card:" + self.card.__str__()

    def __repr__(self):
        return self.__str__()


class Operation:

    @classmethod
    def check(cls, method='lock') -> Account:
        database = Storage.load()
        print(database)
        count = 0
        while True:
            id: int = int(input("请输入卡号:"))
            if id not in database:
                print("卡号不存在！请重新输入卡号")
                count += 1
                if count == 3:
                    print("卡号输入3次不存在。自动退出！")
                    return None
                continue
            account: Account = database.get(id)
            count: int = 0
            password: str = input("请输入密码:")
            while True:
                if password != account.card.password:
                    count += 1
                    if count == 3:
                        print("输入密码错误超过3次！卡已锁，请解锁后再操作！")
                        account.card.is_lock = True
                        database[id] = account
                        Storage.save(database)
                        return None
                    password = input("密码错误!请重新输入:")
                    continue
                break
            break
        if account.card.is_lock is True and method != 'unlock':
            print("卡已锁，请先解锁后再操作！")
            time.sleep(2)
            return None
        return account

    @classmethod
    def create_account(cls) -> None:
        name = input("请输入姓名:")
        identity_id = input("请输入身份证号:")
        password = input("请输入密码:")
        database = Storage.load()
        id = random.randint(1000000, 9999999)
        while id in database:
            id = random.randint(1000000, 9999999)
        card = Card(id, password, 10)
        account = Account(name, identity_id, card)

        database[id] = account
        Storage.save(database)
        print(database)
        print("卡号是:", id)
        time.sleep(2)

    @classmethod
    def query(cls) -> None:
        account = Operation.check()
        if account is not None:
            print("当前卡的余额是:", account.card.amount)
            time.sleep(2)

    @classmethod
    def storage(cls) -> None:
        account = Operation.check()
        if account is not None:
            card = account.card
            money = int(input('请输入存款金额:'))
            card.amount = card.amount + money
            database = Storage.load()
            database[card.id] = account
            Storage.save(database)
            print('成功存入' + str(money) + ',当前余额为' + str(card.amount))
            time.sleep(2)

    @classmethod
    def put(cls) -> None:
        account = Operation.check()
        if account is not None:
            card = account.card
            money = int(input('请输入取款金额:'))
            count = 0
            while money > card.amount:
                print('卡内余额不足，取款失败')
                count = count + 1
                if count == 3:
                    print('输错3次，自动退出')
                    return
                money = int(input('请再次输入取款金额:'))
            card.amount = card.amount - money
            database = Storage.load()
            database[card.id] = account
            Storage.save(database)
            print('成功存入' + str(money) + ',当前余额为' + str(card.amount))
            time.sleep(2)

    @classmethod
    def transfer(cls) -> None:
        account = Operation.check()
        database = Storage.load()
        database[account.card.id] = account
        if account is not None:
            card = account.card
            transfer_id = int(input('转账人卡号:'))
            count = 0
            while transfer_id not in database:
                print('卡号不存在')
                transfer_id = int(input('请重新输入转账人卡号:'))
                count = count + 1
                if count == 3:
                    print('输错三次，自动退出!')
                    return
            transfer_card = database[transfer_id].card
            print('当前卡号用户名字为 ' + database[transfer_id].name)
            money = int(input('请输入转账金额:'))
            count = 0
            while money > card.amount:
                print('卡内余额不足，转账失败')
                count = count + 1
                if count == 3:
                    print('输错3次，自动退出')
                    return
                money = int(input('请再次输入转账金额:'))
            card.amount = card.amount - money
            transfer_card.amount = transfer_card.amount + money
            Storage.save(database)
            print('成功给 ' + str(transfer_card.id) + '\t ' + database[transfer_id].name + ' 转账' + str(
                money) + ',当前余额为' + str(card.amount))
            time.sleep(2)

    @classmethod
    def change_password(cls) -> None:
        account = Operation.check()
        if account is not None:
            database = Storage.load()
            database[account.card.id] = account
            password = input("请输入新密码")
            # second_password = input("再次输入新密码")
            account.card.password = password
            Storage.save(database)
            print('密码修改成功！')
            time.sleep(2)

    @classmethod
    def lock_card(cls) -> None:
        account = Operation.check()
        if account is not None:
            database = Storage.load()
            database[account.card.id] = account
            account.card.is_lock = True
            Storage.save(database)
            print('锁卡成功！')
            time.sleep(2)

    @classmethod
    def unlock_card(cls) -> None:
        account = Operation.check('unlock')
        if account is not None:
            database = Storage.load()
            database[account.card.id] = account
            account.card.is_lock = False
            Storage.save(database)
            print('解锁成功！')
            time.sleep(2)

    @classmethod
    def destroy(cls) -> None:
        account = Operation.check()
        database = Storage.load()
        database[account.card.id]
        del database[account.card.id]
        Storage.save(database)
        print('销卡成功！')
        time.sleep(2)


class Card:
    def __init__(self, id, password, amount):
        self.id = id
        self.password = password
        self.amount = amount
        self.is_lock = True

    def unlock(self):
        self.is_lock = False

    def lock(self):
        self.is_lock = True

    def __str__(self):
        return "id:" + str(self.id) + " password:" + str(self.password) + " amount:" + str(
            self.amount) + ' is_lock: ' + str(self.is_lock)

    def __repr__(self):
        return self.__str__()


class Storage:
    data_base_path = "../temp/bank_database.txt"

    @classmethod
    def load(cls) -> dict:
        database: dict = {}
        if os.path.exists(cls.data_base_path):
            with open(cls.data_base_path, "rb") as fp:
                # 从文件中将用户列表下载下来
                try:
                    database = pickle.load(fp)
                except Exception as e:
                    print(e)
                    database = {}
        return database

    @classmethod
    def save(cls, database):
        handle = open(cls.data_base_path, "wb")
        pickle.dump(database, handle)
        handle.close()


def main():
    print("欢迎进入银行系统")
    while True:
        print("1:开户    2:查询\n3:存款    4:取款\n5:转账    6:修改密码\n7:锁卡    8:解卡\n9:销户    0:退出")
        key = int(input("请输入操作:"))
        if key not in range(0, 10):
            print("输入错误！请重新输入!")
        if key == 1:
            Operation.create_account()
        if key == 2:
            Operation.query()
        if key == 3:
            Operation.storage()
        if key == 4:
            Operation.put()
        if key == 5:
            Operation.transfer()
        if key == 6:
            Operation.change_password()
        if key == 7:
            Operation.lock_card()
        if key == 8:
            Operation.unlock_card()
        if key == 9:
            Operation.destroy()
        if key == 0:
            break


if __name__ == '__main__':
    main()

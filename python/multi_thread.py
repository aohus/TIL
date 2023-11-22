import threading

"""
ChatGPT가 제공한 Inconsistency 예시
"""


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")


# 공유 은행 계좌 객체 생성
account = BankAccount()


def perform_transactions():
    for _ in range(10000):
        account.deposit(10)
        account.withdraw(10)


# 두 개의 스레드 생성
thread1 = threading.Thread(target=perform_transactions)
thread2 = threading.Thread(target=perform_transactions)

# 스레드 실행
thread1.start()
thread2.start()

# 스레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

# 결과 출력
print("Final Balance:", account.balance)
print("Total Transactions:", len(account.transactions))


"""
ChatGPT가 제공한 Data Corruption 예시
"""

# 공유 데이터 리스트
shared_data = []


def add_to_list(value):
    for _ in range(10000000):
        shared_data.append(value)


# 두 개의 스레드 생성
thread1 = threading.Thread(target=add_to_list, args=(1,))
thread2 = threading.Thread(target=add_to_list, args=(2,))

# 스레드 실행
thread1.start()
thread2.start()

# 스레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

# 결과 출력
print(len(shared_data))
print(shared_data.count(1))
print(shared_data.count(2))

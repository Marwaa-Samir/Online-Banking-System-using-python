#!/usr/bin/env python
# coding: utf-8

# <center>
# 
# # 5- Online Banking System
# 
# </center>
# 

# ##

# In[ ]:





# # Team:
# **1. Esraa Emad Abdelreheem Fakhr**  
# **2. Rahma Tarek Mohamed Ali**  
# **3. Shimaa Abdelaal Mohammed Fawzy**  
# **4. Abdelrahman Mohamed Rabie Mohammdy**  
# **5. Marwa Samir Abdelrahim Hussine**
# 

# In[ ]:





# ##

# ### User Class :

# In[1]:


class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.accounts = []

    def register(self):
        # You can add registration logic here, like storing user details in a database
        print(f"User {self.username} registered successfully!")

    def login(self, entered_password):
        if entered_password == self.password:
            print(f"Welcome, {self.username}! You're logged in.")
        else:
            print("Invalid password. Please try again.")

    def update_profile(self, new_username=None, new_password=None, new_email=None):
        if new_username:
            self.username = new_username
        if new_password:
            self.password = new_password
        if new_email:
            self.email = new_email
        print("Profile updated successfully!")



# ##

# ### Customer Class (Inherits from User):
# 

# In[2]:


class Customer(User):
    def __init__(self, user_id, username, password, email):
        super().__init__(user_id, username, password, email)
        self.account_balances = {}  # Account balances stored as a dictionary
        self.transaction_history = {}


    def view_account_balance(self, account_type):
        if account_type in self.account_balances:
            print(f"Account balance for {account_type}: {self.account_balances[account_type]}")
        else:
            print(f"You don't have a {account_type} account.")

    def view_transaction_history(self, account_type):
        if account_type in self.transaction_history:
            print(f"Transaction history for {account_type}:")
            for transaction in self.transaction_history[account_type]:
                print(transaction)
        else:
            print(f"No transaction history found for {account_type} account.")

    def transfer_money(self, from_account, to_account, amount):
        if from_account in self.account_balances and to_account in self.account_balances:
            if self.account_balances[from_account] >= amount:
                self.account_balances[from_account] -= amount
                self.account_balances[to_account] += amount
                # Record transaction history
                self._record_transaction(from_account, f"Transferred {amount} to {to_account}")
                self._record_transaction(to_account, f"Received {amount} from {from_account}")
                print(f"{amount} successfully transferred from {from_account} to {to_account}.")
            else:
                print("Insufficient balance for the transfer.")
        else:
            print("One or both accounts do not exist.")

    def deposit_money(self, account_type, amount):
        if account_type in self.account_balances:
            self.account_balances[account_type] += amount
            # Record transaction history
            self._record_transaction(account_type, f"Deposited {amount}")
            print(f"{amount} successfully deposited to {account_type}.")
        else:
            print(f"You don't have a {account_type} account.")

    def withdraw_money(self, account_type, amount):
        if account_type in self.account_balances:
            if self.account_balances[account_type] >= amount:
                self.account_balances[account_type] -= amount
                # Record transaction history
                self._record_transaction(account_type, f"Withdrew {amount}")
                print(f"{amount} successfully withdrawn from {account_type}.")
            else:
                print("Insufficient balance for the withdrawal.")
        else:
            print(f"You don't have a {account_type} account.")

    def _record_transaction(self, account_type, transaction):
        if account_type in self.transaction_history:
            self.transaction_history[account_type].append(transaction)
        else:
            self.transaction_history[account_type] = [transaction]



# ##

# ### Bank Staff Class (Inherits from User):
# 

# In[3]:


class BankStaff(User):
    def __init__(self, user_id, username, password, email, staff_id, role):
        super().__init__(user_id, username, password, email)
        self.staff_id = staff_id
        self.role = role

    def approve_account_creation(self, user, account_type):
        user.accounts.append(account_type)
        print(f"Account creation for {user.username} approved. {account_type} account created.")

    def freeze_account(self, user, account_type):
        if account_type in user.accounts:
            print(f"{account_type} account for {user.username} has been frozen.")
        else:
            print(f"{user.username} doesn't have a {account_type} account.")

    def unfreeze_account(self, user, account_type):
        if account_type in user.accounts:
            print(f"{account_type} account for {user.username} has been unfrozen.")
        else:
            print(f"{user.username} doesn't have a {account_type} account.")

    def view_customer_information(self, user):
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Accounts: {', '.join(user.accounts)}")



# ##

# ### Account Class:
# 

# In[4]:


class Account:

# Attributes: Account number, account type (e.g., savings, checking), balance, owner (an instance of the Customer class).
    def __init__(self, account_num, account_type, balance, owner):
        self.account_num = account_num
        self.account_type = account_type
        self.balance = balance 
        self.owner = owner
        self.is_frozen = False


# Methods: Display account information, update account balance.
    def display_account_info(self):
        print(f"Account Number : {self.account_num}")
        print(f"Account Type : {self.account_type}")
        print(f"Balance : {self.balance}")
        print(f"Owner : {self.owner.username}")  # an instance of the Customer class 
        # By passing customer as the value for the owner attribute during the creation of the Account object he will take the username as its owner 

    def update_account_balance(self, amount, transaction_type):
        # Check the status of the account:
        if not self.is_frozen:
            if transaction_type == "deposit":
                self.balance += amount
                print(f"Hi {self.owner.username}, your account Number {self.account_num} balance is updated to: {self.balance}")
                
            elif transaction_type == "withdrawal":
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Hi {self.owner.username}, your account Number {self.account_num} Withdrawal of {amount} and their balance is updated to: {self.balance}")
                else:
                    print(f"Sorry {self.owner.username}, Not Enough Money")
            else:
                print("please choose deposit or withdrawal only ")
        else:
            print(f"Sorry {self.owner.username}, but your Account {self.account_num} is frozen")





# ##

# ### Transaction Class:
# 

# In[5]:


from datetime import datetime
class Transaction:

    def __init__(self, transaction_id, amount, transaction_type, sender, receiver = None):
        self.transaction_id = transaction_id
        self.timestamp = datetime.now()
        self.sender = sender.username
        self.receiver = receiver.username if receiver is not None else ""
        self.amount = amount
        self.transaction_type = transaction_type

    recorded_transactions = {}  # Class attribute to store all transactions

    def record_transaction(self):
        transaction_details = {
            "Transaction ID": self.transaction_id,
            "Timestamp": self.timestamp,
            "Sender": self.sender,
            "Receiver": self.receiver,
            "Amount": self.amount,
            "Transaction Type": self.transaction_type
        }
        self.recorded_transactions[self.transaction_id] = transaction_details

        print("Transaction recorded successfully!")

    def view_transaction_details(self):
        if self.transaction_id not in self.recorded_transactions:
            print("Transaction not found")
            return

        transaction_details = self.recorded_transactions[self.transaction_id]
        print("Transaction Details:")
        print(f"Transaction ID: {transaction_details['Transaction ID']}")
        print(f"Timestamp: {transaction_details['Timestamp']}")
        print(f"Sender: {transaction_details['Sender']}")
        print(f"Receiver: {transaction_details['Receiver']}")
        print(f"Amount: {transaction_details['Amount']}")
        print(f"Transaction Type: {transaction_details['Transaction Type']}")


# ##

# ### Online Banking System Class:
# 

# In[6]:


class OnlineBankingSystem:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []
        self.bank_staff = []
        self.accounts = []

    def display_system_info(self):
        print(f"Welcome to {self.bank_name} online banking system")
        print(f"We have {len(self.customers)} customers, {len(self.bank_staff)} bank staff, "
              f"{len(self.accounts)} accounts")

    def add_customer(self, name):
        customer_id = len(self.customers) + 1
        customer = Customer(customer_id, name, "password", f"{name.lower()}@example.com")
        self.customers.append(customer)
        return customer

    # def remove_customer(self, customer_id):
    #     customer = next((c for c in self.customers if c.user_id == customer_id), None)
    #     if customer:
    #         self.customers.remove(customer)
    #     return customer
    def remove_customer(self, customer_id):
      for customer in self.customers:
          if customer.user_id == customer_id:
              self.customers.remove(customer)
              return customer

      return None


    def add_bank_staff(self, role):
        staff_id = len(self.bank_staff) + 1
        staff = BankStaff(staff_id, f"{role}_staff", "password", f"{role.lower()}_staff@example.com", staff_id, role)
        self.bank_staff.append(staff)
        return staff

    # def remove_bank_staff(self, staff_id):
    #     staff = next((s for s in self.bank_staff if s.user_id == staff_id), None)
    #     if staff:
    #         self.bank_staff.remove(staff)
    #     return staff

    def remove_bank_staff(self, staff_id):
      for staff in self.bank_staff:
          if staff.user_id == staff_id:
              self.bank_staff.remove(staff)
              return staff

      return None


    def add_account(self, account_number,account_type, balance, owner_id):
        owner = next((c for c in self.customers if c.user_id == owner_id), None)
        if owner:
            account = Account(account_number, account_type ,balance, owner)
            owner.accounts.append(account)
            self.accounts.append(account)
            return account
        return None

    # def remove_account(self, account_number):
    #     account = next((a for a in self.accounts if a.account_num == account_number), None)
    #     if account:
    #         owner = account.owner
    #         owner.accounts.remove(account)
    #         self.accounts.remove(account)
        #     return account
    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_num == account_number:
                owner = account.owner
                owner.accounts.remove(account)
                self.accounts.remove(account)
                return account

        return None


# ##

# In[ ]:





# ## Test The Classes

# In[7]:


# # Create an instance of the OnlineBankingSystem
bank_system = OnlineBankingSystem(bank_name="MyBank")

print()

# Display system information
bank_system.display_system_info()

print()
print()

customer_1 = Customer(user_id=1, username="esraa", password="45", email="esraa123@.com")
customer_2 = Customer(user_id=2, username="marwa", password="12", email="marwa@.com")

bank_system.add_customer(name="esraa")
bank_system.add_customer(name="marwa")


# Creating a bank staff instance
bank_staff_1 = BankStaff(
    user_id=2,
    username="Shimaa",
    password="shimaa1232001",
    email="shimaa123@gmail.com",
    staff_id="sh123",
    role="Manager"
)

bank_staff_2 = BankStaff(
    user_id=1,
    username="trtrtr",
    password="sh1",
    email="sh23@gmail.com",
    staff_id="sh1",
    role="emp"
)

bank_system.add_bank_staff(role="Manager")
bank_system.add_bank_staff(role="emp")

account_1 = Account(account_num="1", account_type="Savings", balance=5000, owner=customer_1)
bank_system.add_account("1","Savings", 5000, 1)


account_2 = Account(account_num="2", account_type="checking", balance=1000, owner=customer_2)
bank_system.add_account("2","checking", 5000, 1)


#########################################################################################################


# Adding account balances for the customer
customer_1.account_balances = {'saving': 1000, 'checking': 500}

# Transferring money between accounts
customer_1.transfer_money('saving', 'checking', 200)
# Depositing and withdrawing money
customer_1.deposit_money('saving', 300)
customer_1.withdraw_money('checking', 100)

# print()
# print()
# print()

customer_1.view_transaction_history('checking')
print()

customer_1.view_account_balance('saving')
print()

# print()
# print()
# print()

# Adding account balances for the customer
customer_2.account_balances = {'saving': 2000, 'checking': 502}

# Transferring money between accounts
customer_2.transfer_money('saving', 'checking', 300)
# Depositing and withdrawing money
customer_2.deposit_money('saving', 400)
customer_2.withdraw_money('checking', 200)


customer_2.view_transaction_history('checking')
print()

customer_2.view_account_balance('saving')
print()

###############################################################################################

user_1 = User(user_id=1, username="sara", password="sara123", email="sara23@gmail.com")
user_2= User(user_id=2, username="Rahma", password="Rahma123", email="rahma123@gmail.com")


# Approving account creation for the user by the bank staff
bank_staff_1.approve_account_creation(user_1, "saving")
bank_staff_2.approve_account_creation(user_2, "checking")

print()
print()

# Freezing and unfreezing accounts by bank staff
bank_staff_1.freeze_account(user_1, "saving")
bank_staff_1.unfreeze_account(user_1, "saving")
bank_staff_2.unfreeze_account(user_2, "checking")

print()
print()

# Viewing customer information by bank staff
bank_staff_1.view_customer_information(user_1)
bank_staff_2.view_customer_information(user_2)

########################################################################################################

print()
print()
print()

# Display account information
account_1.display_account_info()
account_2.display_account_info()

print()

# Perform a deposit
account_1.update_account_balance(amount=1500, transaction_type="deposit")

# Display updated account information
account_1.display_account_info()


# Perform a withdrawal
withdrawal_amount = 2000
account_1.update_account_balance(amount=withdrawal_amount, transaction_type="withdrawal")
# Display updated account information
account_1.display_account_info()

print()

# Set the account to be frozen
account_1.is_frozen = True

# Try to perform a deposit on a frozen account
account_1.update_account_balance(amount=1500, transaction_type="deposit")
account_1.display_account_info()

###########################################################################################

print()
print()
print()

transaction_1 = Transaction(
    transaction_id="1",
    sender=customer_1,
    amount=500,
    transaction_type="deposite"
)

print()
print()
print()

transaction_2 = Transaction(
    transaction_id="2",
    sender=customer_1,
    receiver=customer_2,
    amount=100,
    transaction_type="transfer"
)



# Recording the transaction
transaction_1.record_transaction()
transaction_2.record_transaction()
# Viewing transaction details
transaction_1.view_transaction_details()
transaction_2.view_transaction_details()

######################################################




bank_system.display_system_info()

# bank_system.display_system_info()


# In[ ]:





# In[ ]:





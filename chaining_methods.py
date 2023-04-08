# copy of user, adding in chaining and 2 ninja bonus
class User:
    list_of_users = []

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # defaulted attributes
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.list_of_users.append(self)


    # Methods
    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Is a rewards member: {self.is_rewards_member}')
        print(f'Points: {self.gold_card_points}')
        print('------------------------------')
        return self

    def enroll(self):
        for user in User.list_of_users:
            if user.is_rewards_member == True:
                print("User already a  member")
                return False
            else:
                self.is_rewards_member = True
                self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        for user in User.list_of_users:
            if user.gold_card_points < amount:
                print('Insufficient points')
                return False
        self.gold_card_points = self.gold_card_points - amount
        return self

    @classmethod
    def print_all_users( cls ):
        for user in cls.list_of_users:
            user.display_info()



jason = User('Jason', 'Yang', 'jason@email.com', '35')
# nick = User('Nicholas', 'Yang', 'nick@email.com', '14')
# maddy = User('Madeline', 'Moua', "maddy@email.com", '6')

jason.enroll()
jason.enroll()
jason.spend_points(50)
jason.display_info()

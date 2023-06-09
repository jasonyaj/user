# original copy
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0
    # Methods
    def display_info(self):
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        age = self.age
        is_rewards_member = self.is_rewards_member
        gold_card_points = self.gold_card_points
        print(first_name)
        print(last_name)
        print(email)
        print(age)
        print(is_rewards_member)
        print(gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount


jason = User('Jason', 'Yang', 'jason@email.com', '35')
nick = User('Nicholas', 'Yang', 'nick@email.com', '14')
maddy = User('Madeline', 'Moua', "maddy@email.com", '6')

jason.enroll()
jason.spend_points(50)

nick.enroll()
nick.spend_points(80)

jason.display_info()
nick.display_info()
maddy.display_info()

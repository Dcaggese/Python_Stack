class User:
    def __init__(self,first,last,email,age):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail Address: {self.email}\nAge: {self.age}\nRewards Member: {self.is_rewards_member}\nGold Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else:
            print(f"{self.first_name} {self.last_name} is already a member!")
        return self

    def spend_points(self,amount):
        if self.is_rewards_member == True and self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} {self.last_name} doesn't have enough points.")
        return self

member1 = User('John','Doe','jdoe@email.com',32)
member2 = User('Jane','Doe','janedoe@email.com',29)
member3 = User('Jim','Shoe','jshoe@email.com',23)


member1.enroll().spend_points(50).display_info().enroll()
member2.enroll().spend_points(80).display_info()
member3.display_info().spend_points(40)
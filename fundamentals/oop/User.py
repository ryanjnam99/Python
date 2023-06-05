class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
         print(f"{self.first_name}")
         print(f"{self.last_name}")
         print(f"{self.email}")
         print(f"{self.age}")
         print(f"Points: {self.gold_card_points}")
         print("------")
         return self
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member") 
            return False
            # make sure put the if statement at the top or it will reset the points
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("You don't have enough points")
            return False
        self.gold_card_points = self.gold_card_points - amount
        return self

         

ryan = User("Ryan", "Nam", "ryanjnam@yahoo.com", "23")
# ryan.enroll()
# ryan.spend_points(50)
# ryan.display_info()

charles = User("Charles", "Cho", "cnammd@yahoo.com", "59")
# charles.enroll()
# charles.spend_points(80)
# charles.display_info()

kyung = User("Kyung", "Sook", "kyung@gmail.com", "53")
# kyung.display_info()
# kyung.spend_points(40)


ryan.enroll().spend_points(50).display_info()
charles.enroll().spend_points(80).display_info()
kyung.display_info().spend_points(40)

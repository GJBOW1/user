# User Assignment - Gregg Bowen 

# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

# Add the display_info(self) method to the User class (Done)

# In the outer scope, create a user instance and call the display_info method to test. (Done)

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope. (Done)

# Make 2 more instances of the User class.

# Implement the spend_points(self, amount) method (Done)

# Have the first user spend 50 points (Done)

# Have the second user enroll. (Done)

# Have the second user spend 80 points (Done)

# Call the display method on all the users.

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.

class User: 
    all_users = []
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.all_users.append(self)

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return True
        else:
            print("User already a member")
            return False

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            return self.gold_card_points
        else:
            print("Insufficient points.")

# Assignment Actions:

user1 = User("Tom", "Merrilin", "wheeloftime@legend.com", 55)
user2 = User("Rand", "Althor", "dragonmount@legend.com", 20)
user3 = User("Mat", "Cauthon", "wolfnecklace@legend.com", 21)
user1.enroll()
user1.display_info()
user1.spend_points(50)
user1.display_info()
user2.enroll()
user2.display_info()
user2.spend_points(80)
user2.display_info()
user1.display_info()
user2.display_info()
user3.display_info()
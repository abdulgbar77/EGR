
POT_ERROR_SYSTEM = """
You are an expert in math reasoning and python programming. Please solve mathematical problems by writing Python code. I will give you an incorrect method for solving mathematical equations. I will also give you 8 correct programming examples. Make sure that 'ans' is a number.
"""

POT_ERROR_QA = """

Question: {question}
Error formula reasoning process: ‘{reason_eot}’
"""

POT_ERROR = """
Examples of equation reasoning errors for each given question:
{eot_reasoning_errors}.
You can't make the same reasoning mistakes in these equations!



Example of correct reasoning - Please follow the code:
1. Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
# Python code:
money_initial = 23
bagels = 5
bagel_cost = 3
money_spent = bagels * bagel_cost
money_left = money_initial - money_spent
ans = money_left


2. Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
# Python code:
golf_balls_initial = 58
golf_balls_lost_tuesday = 23
golf_balls_lost_wednesday = 2
golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
ans = golf_balls_left


3. Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
# Python code:
computers_initial = 9
computers_per_day = 5
num_days = 4  # 4 days between monday and thursday
computers_added = computers_per_day * num_days
computers_total = computers_initial + computers_added
ans = computers_total


4. Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Python code:
toys_initial = 5
mom_toys = 2
dad_toys = 2
total_received = mom_toys + dad_toys
total_toys = toys_initial + total_received
ans = total_toys


5. Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Python code:
jason_lollipops_initial = 20
jason_lollipops_after = 12
denny_lollipops = jason_lollipops_initial - jason_lollipops_after
ans = denny_lollipops


6. Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
# Python code:
leah_chocolates = 32
sister_chocolates = 42
total_chocolates = leah_chocolates + sister_chocolates
chocolates_eaten = 35
chocolates_left = total_chocolates - chocolates_eaten
ans = chocolates_left


7. Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
# Python code:
cars_initial = 3
cars_arrived = 2
total_cars = cars_initial + cars_arrived
ans = total_cars


8. Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Python code:
trees_initial = 15
trees_after = 21
trees_added = trees_after - trees_initial
ans = trees_added



Question: {question}

# Now please write Python code to solve this question.
""".strip() + "\n"


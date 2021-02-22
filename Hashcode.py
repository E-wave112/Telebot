#python starter code for hashcode 2021
##create a class for the teams
class Team:
	##create a class attribute dictionary with the 
	##key being the number of members in the team while the values being the number of that member team present
	def __init__(self,team_nums):
		self.team_nums = team_nums
		##make some assertions
		assert type(self.team_nums ) == dict
		##assert that the number of member teams must be between 2 and 4
		for nums in self.team_nums.keys():
			assert 2<=nums<=4
			

##create another class for the pizza op
class Pizza:
	##create a class attribute composed of the lizza code the ingredients involved
	def __init__(self,pizza_in):
		self.pizza_in = pizza_in
		assert type(self.pizza_in) == dict
		for piz_code, piz_ing in self.pizza_in.items():
			assert type(piz_code) == int and type(piz_ing) == list
			
##create a new class either using multiple inheritance to perform operations on the above classes
class HashProblem(Team,Pizza):
	def __init__(self,team_nums,pizza_in):
		Team.__init__(self,team_nums)
		Pizza.__init__(self,pizza_in)
		##create an assertion to make sure the same sets of ingredients are not repeated across deliveries
		for list_ing in pizza_in.keys():
			list_ing.sort()
			pass
		#get the total deliveries
		D = sum([i.values() for i in self.team_nums.values()])
	

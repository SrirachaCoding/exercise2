#Character Class Declaration
class Characters(object):
	"""
		Characters Constructor
	"""
	name = ''
	level= 0

	def __init__(self, name, level,class_type):
		self.name = name
		self.level = level
		self.type = class_type

	#I DECLARE THAT I AM A ______ action :)
	def declare(self):
		print("I am a %s level %s named %s" % (self.level,self.type, self.name))

#Actual method to validate/create new characters
def make_character(name,level, class_type):
	character = Characters(name, level,class_type)
	return character

#Accept Input Name
print("Please Enter a name")
name=input()

tracker = False
while tracker == False:
	print("Please Input a level (1-99)")
	t_lvl = input()
	if (t_lvl == ''):
		level = 1
	elif (int(t_lvl) >= 1 and int(t_lvl) <= 99):
		level = t_lvl
		tracker = True
	else:
		print("Input Unacceptable.")

print("finally, what class would you like to play?")
class_type = input()

character = make_character(name,level,class_type)
character.declare()
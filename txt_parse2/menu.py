class menus:

	def menu():
		prompt = ["What would you like to do?", 
			"[1] Break down one student's response.", 
			"[2] Break down all responses.", 
			"[3] Count all responses.", 
			"[4] Exit Program."]

		for i in range(0, len(prompt)):
			print(prompt[i])
		command = input("")
		return command

	#def menu_single():

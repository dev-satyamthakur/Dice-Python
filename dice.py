import random

# dice faces
face_1 = r"""
 -----
|     |
|  o  |
|     |
 -----
"""

face_2 = r"""
 -----
|     |
| o o |
|     |
 -----
"""

face_3 = r"""
 -----
| o o |
|     |
|  o  |
 -----
"""

face_4 = r"""
 -----
| o o |
|     |
| o o |
 -----
"""

face_5 = r"""
 -----
| o o |
|  o  |
| o o |
 -----
"""

face_6 = r"""
 -----
| o o |
| o o |
| o o |
 -----
"""

faces_list = [face_1, face_2, face_3, face_4, face_5, face_6]

# main program loop
while True:
	response = input("Press 'r' to roll the dice, 'e' to exit : ").upper()

	if response == "E":
		break

	if response != "R":
		continue

	number = random.randint(0,5)
	print(faces_list[number])

# last msg
print("Thanks for using our dice! \nHave a nice day!\n\n")

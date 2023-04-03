VAMSI KRISHNA UNNAM  vunnam1@stevens.edu

https://github.com/Vk4140/Adventure.git


I have worked around 55-60 hours on this project from the last week.

I have tested my code using the samples from canvas as provided and made few json maps on my own and have compiled,tested and debugged with IDE such as pycharm and VS code and uploaded in gradescope to test the specified test cases.

# bugs and issues

The bugs or issues found in my code are mostly related to black spaces and case sensitivity, while creating the extensions I had to go through each and every possibility to complete and test it.

# resolved issue

I have resolved the issues of white spacing and extension creation of slicing, drop.




The list of three extensions that i have used:

1 - Help
2 - Slicing 
3 - drop

Help : the help extension used in the code let the user to know the commands and flow of the game.

Slicing: This feature indicates without specifying the total command, we can implement the first character so it gives the full command.

Drop : This extension drops the inventory which gets held by the player or the user.



The json module is used to read and parse the game map data, which is stored in a JSON file.
This function takes the game map data and a room index i (defaulting to 0), and prints out the details for the current room. It first prints the room name and description, then lists any items that are present in the room (if any), and finally lists the available exits.
This code reads in the game map data from a file called "loop.map.json" and stores it in the map variable. The length of the map is also stored in a variable called length.
This code initializes the game loop by setting the current room index to 0, calling the getRoomDetails function to display the details for the first room, initializing an empty inventory list, and prompting the user for their first command.
The rest of the game loop goes as follows with the commands of go, get, look, help, drop, etc.






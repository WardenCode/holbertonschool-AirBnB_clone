# AirBnB Clone - The Console:


<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png">

This project is the beginning of a serie of projects for recreate AirBnb, from the basic like console to deploy it.

<img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png">


# The Console:

This console made it with **Python** is perfect to manage and debug our objects of **AirBnB (CRUD)** in a development environment:

- Create
- Read
- Update
- Delete

## How to start it (Linux):

First of all you have to clone the repository (Download):

```bash
	git clone https://github.com/Soria-c/holbertonschool-AirBnB_clone.git
```

Enter to the repository and excecute the console.py (Execute):

```bash
	cd holbertonSchool-AirBnB_clone
	./console.py
```

You will see something like this:

```bash
(hbnb)
```

## How to use it:

After to execute the console you can see the commands with the command help:

### Interactive-Mode

```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

```bash
(hbnb) help create
Usage: create <class_name>
create: Create a new instance of a class
```

```bash
(hbnb) help all
Usage: all <BaseModel> | all
all: Display all instances or specific one
```

### Non-Interactive Mode:


#### With Echo:
```bash
echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

```bash
echo "help create" | ./console.py

(hbnb) Usage: create <class_name>
create: Create a new instance of a class
(hbnb)
```

```bash
echo "help all" | ./console.py

(hbnb) Usage: all <BaseModel> | all
all: Display all instances or specific one
(hbnb)
```

#### With Files:

File command:
```bash
cat commands
help
help create
help all
```

```bash
cat commands | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) Usage: create <class_name>
create: Create a new instance of a class
(hbnb) Usage: all <BaseModel> | all
all: Display all instances or specific one
(hbnb)
```

### Classes:

- BaseModel
- User
- City
- State
- Amenity
- Place
- Review

## Topics:

- OOP (Object Oriented Programming)
- File Storage (JSON)
- File I/O
- Unit Test
- Regex
- Modules

# Authors:

- Carlos Soria <soriac367@gmail.com>
- Diego Linares <diegojeanluck@hotmail.com>

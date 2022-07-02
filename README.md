# AirBnB Clone - The Console:

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220701T214234Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=68342049c867a0816e8243c6a22c56b87d1b8c26e930d703c3888584da750814">

This project is the beginning of a serie of projects for recreate AirBnb, from the basic like console to deploy it.

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220701T214234Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=16ca13631edd3ed4a7d91162d970f021d351bfb56f9be1e56bae818dafc8a545">

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
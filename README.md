# Ticket Shuffler

This application solves the following problem. Having a file with a list of students, you should distribute a certain number of examination tickets among them as evenly and deterministically as possible. At the same time, the distribution should be strongly dependent on some parameter, the change of which would have the greatest impact on the distribution of tickets.

This program takes a file with a list of students, the number of tickets and the distribution parameter, and then it displays the ticket numbers for each student.

## Example

```
$ echo -e "Иванов Иван Иванович\nПетров Петр Петрович\nВладимиров Владимир Владимирович\nАлександров Александр Александрович" > students.txt
$ ./shuffler --file students.txt --numbilets 4 --parameter 1
Иванов Иван Иванович 2
Петров Петр Петрович 1
Владимиров Владимир Владимирович 3
Александров Александр Александрович 4
```

## Implementation

The implementation is in the file `shuffler.py` . It uses the keccak hashing algorithm.

## Algorithm properties and their demonstration

The properties of the resulting distributions are clearly demonstrated in a separate notebook - `src/shuffler.ipynb`.

* The distribution tries to be uniform;
* The distribution deterministically depends on the student's full name and the distribution parameter;
* Even with a slight change in the distribution parameter, distribution tries to change as much as possible.

## Running

### Using python

#### Ubuntu

To run this application using Python, you will need python version 3 (compatibility with versions prior to 3.8 is not guaranteed).
Follow these steps:

1. Optional: create and activate a virtual environment:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
2. Install dependencies:
```
$ pip install -r requirements.txt
```
3. Run the script using python:
```
$ python src/shuffler.py
usage: shuffler [-h] -f FILE -n NUMBILETS -p PARAMETER
shuffler: error: the following arguments are required: -f/--file, -n/--numbilets, -p/--parameter
```

### Using executable

#### Ubuntu

Just run the `shuffler` executable file in the root of the repository.

#### Windows

Just run the `shuffler.exe` executable file in the root of the repository.

## Building

To compile the application for other platforms, it is recommended to use the `pyinstall` utility.

For example, to compile an application on Ubuntu, you can use the following commands:
```
$ pip install pyinstaller
$ pyinstaller src/shuffler.py --onefile # this command will create one executable file - dist/shuffler
```

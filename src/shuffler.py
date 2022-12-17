from typing import Iterable, List
from Crypto.Hash import keccak

import binascii
import argparse

HEXADECIMAL_SYSTEM_BASE = 16
""" A constant equal to 16 is the base of the hexadecimal number system. """

KECCAK_DIGEST_BITS = 512
""" Hash bitness. """

DEFAULT_ENCODING = 'utf8'
""" Default file encoding. """


class Shuffler:
    """
    A class encapsulating the logic of shuffling tickets between students.
    """

    def __init__(self, number_of_tickets: int, distribution_parameter: int):
        """
        Creates a shuffler with a fixed number of tickets and distribution.
        """

        self._number_of_tickets = number_of_tickets
        self._distribution_parameter = distribution_parameter.to_bytes(byteorder='little', length=32)

    def get_tickets_of_students(self, students_data: Iterable) -> List:
        """
        Returns a list of students' tickets according to their data.
        """

        return [
            student_data + [self._get_student_ticket(student_data)]
            for student_data in students_data
        ]

    def _get_student_ticket(self, student_data: Iterable):
        """
        Returns a ticket number for student with provided data.
        """

        return self._get_student_hash(student_data) % self._number_of_tickets + 1

    def _get_student_hash(self, student_data: Iterable) -> int:
        """
        Returns a numerical representation of the student's hash based on his data.
        """

        student_hash = keccak.new(digest_bits=KECCAK_DIGEST_BITS)
        student_hash.update(self._distribution_parameter)
        for value in student_data:
            student_hash.update(value.encode(DEFAULT_ENCODING))
        hash_as_bytes = binascii.hexlify(student_hash.digest())
        return int(hash_as_bytes, HEXADECIMAL_SYSTEM_BASE)


def _get_command_line_arguments():
    """
    Returns an object containing command line arguments.

    List of arguments:

    * file -- the name of the file containing the list of students;
    * numbilets -- number of tickets;
    * parameter -- parameter that changes the distribution.
    """

    parser = argparse.ArgumentParser(
        prog='shuffler',
        description='The program takes a file with student data, the number '
                    'of tickets and a special parameter and prints the ticket '
                    'number of each student'
    )
    parser.add_argument('-f', '--file',
                        help='the name of the file containing the list of students',
                        required=True,
                        type=argparse.FileType(mode='r', encoding=DEFAULT_ENCODING))
    parser.add_argument('-n', '--numbilets',
                        help='number of tickets',
                        required=True,
                        type=int)
    parser.add_argument('-p', '--parameter',
                        help='parameter that changes the distribution',
                        required=True,
                        type=int)

    return parser.parse_args()


def main():
    """
    Entry point to the program: takes three command-line arguments and
    prints the ticket numbers for students specified in the file to the
    console (see the help page)
    """
    arguments = _get_command_line_arguments()

    shuffler = Shuffler(
        number_of_tickets=arguments.numbilets,
        distribution_parameter=arguments.parameter
    )

    students = [line.split() for line in arguments.file.readlines()]
    ticket_distribution = shuffler.get_tickets_of_students(students)

    for student_data in ticket_distribution:
        print(*student_data)


if __name__ == '__main__':
    main()

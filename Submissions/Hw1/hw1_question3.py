# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:26:02 2018

@author: ron
"""

def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    result = {}
    subjects = [data.pop('subject') for data in
                (subj1_all_students, subj2_all_students)]
    for student in subj1_all_students:
        if student in subj2_all_students:
            if max(subj1_all_students[student]) > max(subj2_all_students[student]):
                result[student] = subjects[0]
            else:
                result[student] = subjects[1]
    return result

if __name__ == '__main__':
    history = {'Leo': (65, 80),
               'Raphy': (82, 98),
               'Michael': (12, 63),
               'Jimmy': (73, 86),
               'Robert': (56, 84),
               'subject': 'History'}

    math = {'Leo': (80, 92),
            'Donny': (95, 100),
            'Jimmy': (70, 85),
            'Robert': (85, 85),
            'John': (63, 92),
            'subject': 'Math'}
    res = compare_subjects_within_student(history, math)
    print(res)
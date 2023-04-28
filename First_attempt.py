# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:51:32 2023

@author: bwb16179
"""

import numpy as np
import pandas as pd
from hungarian_algorithm import algorithm

Projects_avail = "Data/ProjectList.csv"
Student_choices = "Data/StudentChoices.csv"

Project_avail_arr = pd.read_csv(Projects_avail, delimiter=',', encoding='windows-1252', index_col='ProjectNumber')
Student_choice_array  = pd.read_csv(Student_choices, delimiter=',', encoding='windows-1252', index_col='Student Number')

# Sort out Projects that have a capacity of more than 1

Student_choice_array = Student_choice_array.replace(np.nan, 0)

numerous_projs = []

for index, row in Project_avail_arr.iterrows():
    x = [i for i in range(1, row['Capacity'] + 1)]
    for i in x:
        numerous_projs.append([index, row['Section']])
        
Proj_avail_arr_sorted = pd.DataFrame(numerous_projs, columns = ['ProjectName', 'Section'])

# Create Graph of Students and their choices


student_choices_list = []

for index, row in Student_choice_array.iterrows():
    tenth = int(row['10th'])
    ninth = int(row['9th'])
    eighth = int(row['8th'])
    seventh = int(row['7th'])
    sixth = int(row['6th'])
    fifth = int(row['5th'])
    fourth = int(row['4th'])
    third = int(row['3rd'])
    second = int(row['2nd'])
    first = int(row['1st'])
    
    #choices = {index: {'1': first, '2': second, '3': third, '4': fourth, '5': fifth, '6': sixth, '7': seventh, '8': eighth, '9': ninth, '10': tenth}}
    
    student_row = [index, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
    
    student_choices_list.append(student_row)
    


def greedy_algo(projects, students):
    
    Proj_avail_arr_sorted = projects
    student_choices_list = students
    assigned_choices = []
    
    for x in range(0, len(student_choices_list)):
        choice = 1
        student = x
    
        if student_choices_list[student][choice] in Proj_avail_arr_sorted['ProjectName']:
            #print(f"Student {x} has been assigned Project Number {student_choices_list[student][choice]}")
            Proj_avail_arr_sorted.drop(labels=[student_choices_list[student][choice]])
            print(len(Proj_avail_arr_sorted.index))
            assigned_choices.append([x, student_choices_list[student][choice]])
            continue
        else:
            choice += 1
            continue
        
greedy_algo(Proj_avail_arr_sorted, student_choices_list)
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:51:32 2023

@author: bwb16179
"""

import numpy as np
import pandas as pd
import random
from datetime import datetime
import csv

data_in = "Data/Project-Data.xlsx"
max_epoch = 100000


Project_avail_arr = pd.read_excel(data_in, sheet_name=0, header=0, names=['ProjectNumber', 'Section', 'Capacity'])
Student_choice_array = pd.read_excel(data_in, sheet_name=1, header=0, names=['Student Number', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th'], index_col=None)

Student_choice_array = Student_choice_array.replace(np.nan, 0)

numerous_projs = []
projs = []

# Sort out Projects that have a capacity of more than 1
for index, row in Project_avail_arr.iterrows():
    x = [i for i in range(1, row['Capacity'] + 1)]
    for i in x:
        numerous_projs.append([index, row['Section']])
        projs.append(index)
        
Proj_avail_arr_sorted = pd.DataFrame(numerous_projs, columns = ['ProjectName', 'Section'])



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
        
    student_row = [index, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
    
    student_choices_list.append(student_row)

def greedy_algo(projects, students):
    
    student_choices_list = students
    random.shuffle(student_choices_list)
    assigned_choices = []
    
    score = 0
    score_list = []
    
    
    for x in student_choices_list:
        
        choice = 1
        student = x[0]
        #print(student)
        pick = x[choice]
        
        if pick in projs:
            assigned_choices.append([student, pick])
            projs.remove(pick)
            score += 1
            score_list.append(1)
            continue
        elif pick not in projs and x[choice + 1] in projs:
            assigned_choices.append([student, x[choice + 1]])
            projs.remove(x[choice + 1])
            score += 2
            choice = 1
            score_list.append(2)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] in projs:
            assigned_choices.append([student, x[choice + 2]])
            projs.remove(x[choice + 2])
            score += 3
            choice = 1
            score_list.append(3)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3]  in projs:
            assigned_choices.append([student, x[choice + 3]])
            projs.remove(x[choice + 3])
            score += 4
            choice = 1
            score_list.append(4)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] in projs:
            assigned_choices.append([student, x[choice + 4]])
            projs.remove(x[choice + 4])
            score += 5
            choice = 1
            score_list.append(5)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] not in projs and x[choice + 5] in projs:
            assigned_choices.append([student, x[choice + 5]])
            projs.remove(x[choice + 5])
            score += 6
            choice = 1
            score_list.append(6)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] not in projs and x[choice + 5] not in projs and x[choice + 6] in projs:
            assigned_choices.append([student, x[choice + 6]])
            projs.remove(x[choice + 6])
            score += 7
            choice = 1
            score_list.append(7)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] not in projs and x[choice + 5] not in projs and x[choice + 6] not in projs and x[choice + 7] in projs:
            assigned_choices.append([student, x[choice + 7]])
            projs.remove(x[choice + 7])
            score += 8
            choice = 1
            score_list.append(8)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] not in projs and x[choice + 5] in projs and x[choice + 6] not in projs and x[choice + 7] not in projs and x[choice + 8] in projs:
            assigned_choices.append([student, x[choice + 8]])
            projs.remove(x[choice + 8])
            score += 9
            choice = 1
            score_list.append(9)
            continue
        elif pick not in projs and x[choice + 1] not in projs and x[choice + 2] not in projs and x[choice + 3] not in projs and x[choice + 4] not in projs and x[choice + 5] in projs and x[choice + 6] not in projs and x[choice + 7] not in projs and x[choice + 8] not in projs and x[choice + 9] in projs:
            assigned_choices.append([student, x[choice + 9]])
            projs.remove(x[choice + 9])
            score += 10
            choice = 1
            score_list.append(10)
            continue
            
            
    return assigned_choices, score, score_list



score_list_training_cycles = []

best = 0
best_score_list = 0
best_score = 0
best_epoch = 0

start = datetime.now()

for epoch in range(max_epoch):
    
    print(f"Epoch {epoch} is underway")
    
    projs = []
    for index, row in Project_avail_arr.iterrows():
        x = [i for i in range(1, row['Capacity'] + 1)]
        for i in x:
            numerous_projs.append([index, row['Section']])
            projs.append(index)
    
    assigned_choices, score, score_list = greedy_algo(projs, student_choices_list)
    
    score_list_training_cycles.append(score)
    
    print(f"The score for Epoch {epoch} is: {score}\n")
    
    if score != 0:
        if score <= np.min(score_list_training_cycles):
            best = assigned_choices
            best_score_list = score_list
            best_score = score
            best_epoch = epoch
            #print(best)
            continue
        else:
            continue
    else:
        continue

for x in best:
    x[0] = x[0] + 1
    
best.sort()    
with open("Best_allocation.csv", "w+", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Student", "Allocated Project Number"])
    writer.writerows(best)
    f.close()

number_of_students = len(student_choices_list)

MCCB = 0
CaS = 0
MaCC = 0
BAC = 0
PACERS = 0

for x in best:
    if x[1] >= 1 and x[1] <= 14:
        MCCB += 1
    if x[1] == 40:
        MaCC += 1
    if x[1] >= 15 and x[1] <= 39:
        CaS += 1
    if x[1] >= 41 and x[1] <= 63:
        BAC += 1
    if x[1] >= 64 and x[1] <= 86:
        MaCC += 1
    if x[1] >=87 and x[1] <= 88:
        PACERS += 1
        
print("========================================================================")
print(f"The best score achieved was {best_score} and was acheived on epoch {best_epoch}")
print("========================================================================")
print("========================================================================")
print("The following shows how the distribution of projects by order of choice:")
print([[x, best_score_list.count(x)] for x in set(best_score_list)])
print("========================================================================")
print("========================================================================")
print(f"Of {number_of_students} students, {round((best_score_list.count(1)/number_of_students)*100,2)}% of students got their first pick")
print(f"Of the remaining {number_of_students - best_score_list.count(1)} students, {round((best_score_list.count(2)/(number_of_students - best_score_list.count(1)))*100, 2)}% of students got their second pick")
print(f"Of the remaining {number_of_students - best_score_list.count(1) - best_score_list.count(2)} students, {round((best_score_list.count(3)/(number_of_students - best_score_list.count(1) - best_score_list.count(2)))*100, 2)}% of students got their third pick")
print(f"Of the remaining {number_of_students - best_score_list.count(1) - best_score_list.count(2) - best_score_list.count(3)} students, {round((best_score_list.count(4)/(number_of_students - best_score_list.count(1) - best_score_list.count(2) - best_score_list.count(3)))*100, 2)}% of students got their fourth pick")
print("========================================================================")
print("========================================================================")
print("The following is the split of allocated projects by section:")
print(f"{MCCB} projects in MCCB")
print(f"{CaS} projects in CaS")
print(f"{MaCC} projects in MaCC")
print(f"{BAC} projects in BAC")
print(f"{PACERS} projects in PACERS")
print("========================================================================\n")

fin = datetime.now()

time_diff = fin - start

print("Time elapsed = {:02}s".format(time_diff.seconds))
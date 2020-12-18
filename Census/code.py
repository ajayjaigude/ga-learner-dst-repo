# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

## Step 1
census = np.concatenate((data,new_record),axis=0)
data.shape
census.shape

## Step 2
age=np.asarray(census[0:1001, 0])

max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

## Step 3
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]

for element in census[0:1001, 2]:
    if element == 0:
        race_0.append(0)
    if element == 1:
        race_1.append(1)
    if element == 2:
        race_2.append(2)
    if element == 3:
        race_3.append(3)
    if element == 4:
        race_4.append(4)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

minority_race = 3

## Step 4
senior_citizens = age[age>60]
senior_citizens_len=len(senior_citizens)
hours_per_week = census[0:1001, 6]
working_hours_sum=sum(hours_per_week[np.where(census[0:1001, 0]>60)])
senior_citizens_len=len(senior_citizens)
print(working_hours_sum)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

### Step 5
high = []
low = []
for element in census[0:1001, 1]:
    if element>10:
        high.append(element)
    else:
        low.append(element)

income = census[0:1001, 7]
avg_pay_high = np.mean(income[np.where(census[0:1001, 1]>10)])
avg_pay_low = np.mean(income[np.where(census[0:1001, 1]<=10)])
print(avg_pay_high)
print(avg_pay_low)




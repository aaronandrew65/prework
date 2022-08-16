# Question 1

def hello_name(user_name):
    print("hello_"+ user_name + "!")
user_name= input('Enter Username: ')
hello_name(user_name)

# Question 2

def first_odd():
    for i in range(1,101):
        if i % 2 == 1:
            print(i)
first_odd()

# Question 3

def max_num_in_a_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [36,34,43,65,47]
print(max_num_in_a_list(a_list))

# Question 4
def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif a_year % 100 ==0:
        return False
    elif a_year % 4 ==0:
        return True
    else:
        return False
a_year = int(input())
print(is_leap_year(a_year))

# Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))

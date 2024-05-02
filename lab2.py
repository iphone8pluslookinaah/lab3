import math
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu(): 
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    return

def get_user_input():
    print("get_user_input")
    temp = input("input? ")
    temp_split = temp.split(",")
    for i in temp_split:
        temp_split[temp_split.index(i)] = float(i)
    return temp_split

def calc_average_temperature(temp):
    print("To return a float value of the calculated average value of all temperature readings.")
    calc = sum(temp) / len(temp)
    return calc

def calc_min_max_temperature(temp):
    print("To return an integer list with 2 values for minimum and maximum temperature.")
    temp.sort()
    result = [temp[0], temp[-1]]
    return result

def sort_temperature(list):
    result = sorted(list)
    return result

def calc_median_temperature(list):
    print("calc_median_temperature")
    temp = sorted(list)
    if ((len(temp)/2) == int(len(temp)/2)):
        middleindex = (len(temp) / 2)
        median = ((temp[middleindex] + temp[middleindex - 1]) / 2)
    else:
        middleindex = math.floor(len(temp) / 2)
        median = temp[middleindex]
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("List entered:", num_list)
    print("Average temperature:", calc_average_temperature(num_list))
    print("Minimum and maximum temperature:", calc_min_max_temperature(num_list))
    print("List sorted:", sort_temperature(num_list))
    print("Median temperature:", calc_median_temperature(num_list))

if __name__ == "__main__":
    main()
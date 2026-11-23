def display_main_menu():
    print("Enter some numbers separated by commas (e.g 5,6,7,8,9,10):")

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    num_list = []
    for s in str_list:
        num_list.append(float(s))
    return num_list


def calc_average(temp_list):
    return sum(temp_list) / len(temp_list)

def find_min_max(temp_list):
    return min(temp_list), max(temp_list)

def main():
    display_main_menu()
    user_list = get_user_input()
    average = calc_average(user_list)
    minimum, maximum = find_min_max(user_list)

    print("Average: " + str(average))
    print("Minimum: " + str(minimum))
    print("Maximum: " + str(maximum))


if __name__ == "__main__":
    main()
my_list=[15,20,26,260,249,3365,4452,8]
if my_list[0] > my_list[1]:
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp

print("sorted", my_list)
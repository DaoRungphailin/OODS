print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
lst = list(map(int,input().split()))

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

winner = mode(lst)

if winner[0] >= 1  and winner[0] <= 20:
    print(winner[0])
else:
    print("*** No Candidate Wins ***")

# print("***Election***")
# n = int(input("Enter a number of voter(s) : "))
# input_string = input()
# user_list = input_string.split()
# my_list = []
# for i in range(21) :
#     my_list.append('0')
#     my_list[i] = int(my_list[i])

# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     user_list[i] = int(user_list[i])
#     if user_list[i] >=0 and user_list[i] <=20 :
#         my_list[user_list[i]] += 1

# if max(my_list) == 0 :
#     print("***No Candidate Wins***")
# else :
#     print(my_list.index(max(my_list)))

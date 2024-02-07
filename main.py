#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        output = sum(int(list1_num) * int(list2_num) for list1_num, list2_num in zip(list1, list2))
        return output
    else:
        return "error"



if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE

    
    list1 = input()
    list2 = input()

final_output = sum_of_products(list1, list2)
print(final_output)

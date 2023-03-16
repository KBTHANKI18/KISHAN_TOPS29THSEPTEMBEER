# Write a Python function to get the largest number, smallest num and sum of all from a list.
def list(input_list):
    if len(input_list) == 0:
        return None, None, None
    else:
        max_num = max(input_list)
        min_num = min(input_list)
        total_sum = sum(input_list)
        return max_num, min_num, total_sum
input_list = [22,33,44,55,66]
max_num, min_num, total_sum = list(input_list)
print("Max number:", max_num)  
print("Min number:", min_num)  
print("Total sum:", total_sum) 

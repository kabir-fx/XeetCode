## Approach 1 [Bubble Sort]
Check for each condition whther nums[i] <= nums[i+1], else check whether bits of 1 are equal are not; if equal perfom swap and if not return False

## Apprach 2
Initialize 2 variables cur_min and cur_max both to 1 val of arr., we hv to check arr in groups, instead of 2 pointers - first we will check whther cur bin val = cur_min/cur_max,if not it means it belongs to a different group. Then We will check whether prev_max(prev intialized to -inf) is > cur_min or not if so return False else change the both current pointer to i and prev_max to cur_max. These 2 statements will only be executed when a new group is identified.
Lastly there is no check to identify whether last group's cur_min > preV_max as the group never reaches to 2 part of the loop so return that.

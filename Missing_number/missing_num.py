def find_missing(list1, list2):
    missing = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
	"""
       set1 = set(list1)
	   set2 = set(list2)
	   missing = set1 ^ set2
    """
	if missing == []:
		return 0
	for i in missing:
		return i
print find_missing([1,2,3],[1,2,3,4,5])

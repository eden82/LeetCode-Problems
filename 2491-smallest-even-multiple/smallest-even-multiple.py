class Solution:
    def smallestEvenMultiple(self, n):
        multiple_of_2 = []
        multiple_of_n = []
        if 1<= n <= 150:
            for i in range(150):
                a = n*(i+1)
                multiple_of_n.append(a)
            for i in range (150):
                b = 2*(i +1)
                multiple_of_2.append(b)
            common_element = list(set(multiple_of_2) & set(multiple_of_n))
            min_value = min(common_element)
            return min_value
        else:
            print ("error")

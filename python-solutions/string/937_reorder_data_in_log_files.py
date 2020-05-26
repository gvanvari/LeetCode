import operator
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        result = []

        # split logs by spaces and sort them out in two buckets
        for _ in logs:
            split_it = _.split(" ")
            if split_it[1].isdigit():
                '''
                - Add as a string ,  appends - Adds an element at the end of the list
                - The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
                Example - 
                string.join(iterable)
                x = "#".join(myTuple)
                '''
                digit_logs.append(" ".join(split_it[:]))
            else:
                letter_logs.append([split_it[0], " ".join(split_it[1:])])  # add log id and digits separately

        '''
        - First add strings to the result being sorted with
        - The operator module functions allow multiple levels of sorting. We need this because "The letter-logs are
        ordered lexicographically ignoring identifier, with the identifier used in case of ties." 
        Example : logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        there will be a tie because of "art"
        '''
        for i in sorted(letter_logs, key=operator.itemgetter(1, 0)):  # sorted is a built in function
            result.append(" ".join(i))

        return result + digit_logs
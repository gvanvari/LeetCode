class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0

        steps = 0
        power_of_two = 1

        while power_of_two <= num:
            # Apply the bit mask to check if the bit at "power_of_two" is a 1.
            if (power_of_two & num) != 0:
                steps = steps + 2
            else:
                steps = steps + 1
            power_of_two = power_of_two * 2

        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1

        """
        steps = 0
        while num:
            if num%2 == 0:
                num = num/2
                steps = steps + 1
            else:
                num = num -1
                steps = steps + 1

        return steps
        """
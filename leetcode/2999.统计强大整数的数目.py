class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        num_digits_s = len(s)
        
        def count_powerful_numbers(num_str):
            result = 0
            if int(num_str) < int(s):
                return 0
            if int(num_str) >= int(s):
                result += 1

            tail = num_str[-num_digits_s:]
            num_str = num_str[:-num_digits_s]
            
            if int(tail) < int(s):
                num_str = str(int(num_str) - 1)
            @cache
            def recursive_count(i, is_lim, is_num):
                res = 0
                if i == len(num_str):
                    return int(is_num)
                if not is_num:
                    res += recursive_count(i + 1, False, is_num)
                
                upper_limit = int(num_str[i]) if is_lim else limit
                upper_limit = min(upper_limit, limit)

                for digit in range(1 - int(is_num), upper_limit + 1):
                    res += recursive_count(i + 1, is_lim and digit == int(num_str[i]), True)

                return res
            return recursive_count(0, True, False) + result
        return count_powerful_numbers(str(finish)) - count_powerful_numbers(str(start - 1))

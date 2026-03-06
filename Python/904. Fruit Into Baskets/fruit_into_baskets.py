from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # if len(set(fruits)) <= 2:
        #     return len(fruits)
        
        # basket = []
        # count = 0
        # for fruit in fruits:
        #     if len(set(basket)) == 2 and fruit not in basket:
        #         count = max(count, len(basket))
        #         while len(set(basket)) == 2:
        #             basket.pop(0)
        #         basket.append(fruit)
        #     else:
        #         basket.append(fruit)
        #     print(basket)
        # return max(count, len(basket))

        # count = 0
        # basket = {}
        # for fruit in fruits:
        #     if fruit not in basket and len(basket.keys()) == 2:
        #         count = max(count, sum(basket.values()))
        #         rem_fruit = list(basket.keys())[0]
        #         # print(rem_fruit)
        #         del basket[rem_fruit]
        #         basket[fruit] = 1
        #     elif fruit in basket:
        #         basket[fruit] +=1
        #     else:
        #         basket[fruit] = 1
        # return max(count, sum(basket.values()))

        # queue = []
        # count = 0
        # for fruit in fruits:
        #     if fruit not in queue and len(set(queue)) == 2:
        #         count = max(count, len(queue))
        #         while len(set(queue)) == 2:
        #             queue.pop(0)
        #         queue.append(fruit)
        #     else:
        #         queue.append(fruit)
        # return max(count, len(queue)) 
                
        count = {}
        l , total, res = 0 , 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            total += 1
            while len(count) > 2:
                f= fruits[l]
                count[f] -= 1
                l += 1
                total -=1

                if not count[f]:
                    del count[f] 
            res = max(res, total)
        return res

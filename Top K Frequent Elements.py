class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elem_map = {}
        el = []
        for num in nums:
            if num not in elem_map:
                elem_map[num] = 1
            else:
                elem_map[num]+=1
            
        sorted_dict_desc = dict(sorted(elem_map.items(), key=lambda item: item[1], reverse=True))
        for i, key in enumerate(sorted_dict_desc.keys()):
            if i < k:  
                el.append(key)
        return el
           


        


        

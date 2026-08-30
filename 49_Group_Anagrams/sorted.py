class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            key ="".join(sorted(word))
            if key not in output:
                output[key] = []
            output[key].append(word)
        
        return list(output.values())

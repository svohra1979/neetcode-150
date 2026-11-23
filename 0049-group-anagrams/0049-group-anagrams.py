class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen={}
        
        for i in strs:
            
            t=tuple(sorted(i))
            if t not in seen:
                seen[t]=[]
                
                
            seen[t].append(i)
        return list(seen.values()) 
       
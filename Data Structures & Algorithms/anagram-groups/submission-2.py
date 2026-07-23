class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups - list of strings in a dictionary 
        # itterate through every string 
        # look at every string, char by char - assign freq
        # store the freq as key - str as value, keep appending 

        groups = defaultdict(list) 

        for str in strs:
            count= [0]* 26 
            for ch in str:
                count[ord(ch)- ord('a')]+=1

            groups[tuple(count)].append(str)

        return(list(groups.values()))
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        # read every string from the list of strings 
        for string in strs:
            encoded+= str(len(string)) + "#" +string
        return(encoded)

        # save in one ended string as length + "#" + string 

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        
        while i < len(s):
            j=i
            while(s[j]!= '#'):
                j+=1

            length1= int(s[i:j])
            j+=1
            word= s[j:j+length1]

            result.append(word)
            i= j+length1
        return(result)

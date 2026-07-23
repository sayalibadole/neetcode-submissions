class Solution:

    def encode(self, strs: List[str]) -> str:
        # get each string - calculate length
        encoded=""
        for string in strs:
            encoded+= str(len(string)) + "#" + string

        return(encoded)

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0

        while i< len(s):
            j=i

            while(s[j]!= '#'):
                j+=1
            
            length= int(s[i:j])
            j+=1

            word= s[j:j+length]
            result.append(word)

            i=j+length
        return(result)

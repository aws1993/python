class StringOperations:
    def reverse(self,str = None):
        return str[::-1]
      
class ReversedString (StringOperations) : 
      rs = ReversedString();
      print(rs.reverse("aws"));
   

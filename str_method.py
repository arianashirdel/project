class CustomStr:
     def __init__(self,string):
         self.string=string
         
         
     def custom_split(self,*arg):
       result=[self.string]
       for i in arg:
           new_result=[]
           for item in result:
               new_result.extend(item.split(i))
           result=new_result
       return result
    
     def remove_duplicate(self):
        name=self.string
        result=''
        for char in name:
            if char not in result:
                result=result+char
        return result
    
      
     def set(self,index,new):
         name=self.string
         index=index
         new=new
         lst=list(name)
         lst[index]=new
         result=''
         new_name=result.join(lst)
         return new_name
               
     def isfloat(self):
         num=self.string
         try:
            float(num)
            return True
         except:
             return False
     
     def ispalindrome(self):
         string=self.string
         lst=list(string)
         lst.reverse()
         res=''
         rev_string=res.join(lst)
         if rev_string==string:
             return True
         else:
            return False
        
        
        
        
    
x=CustomStr('ariana shirdel')
print(x.custom_split('n','s'))
print(x.remove_duplicate())
print(x.set((0),('s')))

y=CustomStr(12)
print(y.isfloat())
z=CustomStr('a')
print(z.isfloat())

t=CustomStr('asa')
print(t.ispalindrome())
a=CustomStr('sara')
print(a.ispalindrome())

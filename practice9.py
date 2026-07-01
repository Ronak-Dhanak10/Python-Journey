sentancce = "I like codeing"

vovle = 'a,e,i,o,u'
count = 0   
for ch in sentancce:
  if ch in vovle:
        count+=1
        print(ch.casefold(), end=' ',)
        print( count)
        
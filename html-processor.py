import re



rexp1 = re.compile(r'<title>(.+?)</title>') #εξαγωγή τίτλου

rexp2 = re.compile(r'<!--.*?-->',re.DOTALL)  #απαλοιφή σχολίων 

rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) #απαλοιφή των script και style tags 

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #εξαγωγή και εκτυποση href απο <a> tags 

rexp5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) #απαλοιφή ολων των tags
rexp5_2 = re.compile(r'<.+?/>',re.DOTALL) 

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #μετατροπή των HTML entities

rexp7 = re.compile(r'\s+') #μετατροπή των συνεχόμενων χαρακτήρων whitespace σε ένα κενο


def function(m): #η συνάρτηση μετατρέπει τα html entities όπως τα περιγράφει ο πίνακας

    if (m.group(0)=='&amp;'):
        return '&'
    elif (m.group(0)=='&gt;'):
        return '>'
    elif (m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '

        
with open('testpage.txt','r',encoding='utf-8') as fp: 
  text = fp.read()
  m = rexp1.search(text)
  print(m.group(1)) 
  
  text = rexp2.sub(' ',text) 
  
  text = rexp3.sub(' ',text) 
  
  for m in rexp4.finditer(text): 
    print('{} {}'.format(m.group(1),m.group(2)))
    
  text = rexp5_1.sub(' ',text) 
  text = rexp5_2.sub(' ',text) 
  text = rexp6.sub(function,text) 

  text = rexp7.sub(' ',text) 

  print(text)

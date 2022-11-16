import spacy
import sys
from jinja2 import Template

nlp = spacy.load("en_core_web_sm")

text = ''.join([row for row in sys.stdin])
print(text)
doc = nlp(text)
#doc = nlp("we need 2 tickets to Dublin, and 1/2 a spoon of milk")
#for line in sys.stdin:
#    print(line.strip())

dic = {}

for tok in doc:
    if tok.pos_ == 'PROPN':
        dic[tok.text] = dic.get(tok.text, 0) + 1
    elif tok.pos_ == 'NUM':
        for n in tok.text:
            if n.isdigit():
                dic[n] = dic.get(n, 0) + 1

#print(tok, tok.pos_)
#print(dic)


template = Template("""
<!DOCTYPE html>
<html>
<head>
<title>HTML p align Attribute</title>
</head>
<body>
    <h1>GeeksforGeeks</h1>
<table style="border:2px black solid" align="right">
  <thead>
    <tr>
      <th>toc</th>
      <th>count</th>
    </tr>
  </thead>
<tr>
{% for item in table %}
<tr>
<td>{{item[0]}}</td>
<td>{{item[1]}}</td>
</tr>
{% endfor %}
</table>
</body> 
</html>""")
#my_array = [[0,1], [1,1], [2,7], [3,3]]
print(template.render(table=dic.items()))

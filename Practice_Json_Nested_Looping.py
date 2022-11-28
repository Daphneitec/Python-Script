import json
import pandas as pd

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
myjson = json.loads(sampleJson)
print(myjson['company']['employee']['payble']['salary'])

sampleJson2 = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

#data = []
#Loop thru json
try:
    data = json.loads(sampleJson2)
except Exception as e:
    print(e)

for i in data:
    for k in i:
       if  type(i[k]) == list: 
            for l in i[k]:
              print(k,l)
       else:
         print(k,":",i[k])



#Load into Pandas dataframe
mydf = pd.json_normalize(data, record_path=['color'],meta=['id','name'])
print(mydf)    

s_data = json.dumps(sampleJson2, sort_keys = True)     
print(s_data)

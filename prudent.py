import json
from datetime import datetime 
import re
from re import match
import pandas as pd
import numpy as np
import csv


# 
f = open('E:/task_input_list.json')

data = json.load(f)

#date match
match_date = re.compile('^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$')
date_list = list(filter(match_date.match, data))
# print(date_list)  


#dollar amount 
dollar_amount_check = re.compile('\$\d+(?:\.\d+)?')
dolar_amount_list = list(filter(dollar_amount_check.match,data))


neg_dollar_amount_check = re.compile('^-\$\d+(?:\.\d+)?')
neg_dolar_amount_list = list(filter(neg_dollar_amount_check.match,data))

doller_list = dolar_amount_list+neg_dolar_amount_list
# print(doller_list)
removetable = str.maketrans('', '', '$,')
doller_list = [s.translate(removetable) for s in doller_list]

dolor_list = []
for x in doller_list:
    x = float(x)
    dolor_list.append(round(x*73))

# print(newamountlist)  
#end

amount_check = re.compile('[0-9]*[.,][0-9]*')
amount_list = list(filter(amount_check.match,data))

neg_amount_check = re.compile('^-[0-9]*[.,][0-9]*')
neg_amount_list = list(filter(neg_amount_check.match,data))
amount_list = amount_list+neg_amount_list

removetable = str.maketrans('', '', ',')
inr_list = [round(float(s.translate(removetable))) for s in amount_list]
overall_amount = dolor_list+inr_list
max_amount = max(overall_amount)
min_amount = min(overall_amount)


##phone matching
phone_list = []
for x in data:
   ss = re.findall("[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}", x)
   if len(ss) >0:
     phone_list.append(ss)  

##end     



# matching email

match_email=re.compile('[^@]+@[^@]+\.[^@]+')
email_list = list(filter(match_email.match,data))
#end

string_overall_amount = [str(int) for int in overall_amount]
# single_phone_list = item for item in phone_list

phone_singlelist = []
for sublist in phone_list:
    for item in sublist:
        phone_singlelist.append(item)



Deposits_transaction =[]
withdrawals_transaction = []

for item in overall_amount:
    if item>0:
        Deposits_transaction.append(str(item))

    else:
        withdrawals_transaction.append(str(item))

dic = {}
dic['key'] = 'Value'
dic['Date'] = ','.join(date_list)
dic['Amount'] = ','.join(string_overall_amount)
dic['Phone Number'] = ','.join(phone_singlelist)
dic['Email'] = ','.join(email_list)
dic['Max Amount'] = max_amount
dic['Min Amount'] = min_amount
dic['Deposits Transaction'] =','.join(Deposits_transaction)
dic['withdrawals Transaction'] =','.join(withdrawals_transaction)






df = pd.DataFrame(data=dic, index=[0])


df = (df.T)
# df.replace(r'', np.NaN)
df = df.replace(r'^\s*$', np.NaN, regex=True)

print (df)

df.to_excel('E:/Task1.xlsx')
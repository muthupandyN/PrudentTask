import pandas as pd



xls = pd.ExcelFile('E:/task2_data_processing.xlsx')
data_f1 = pd.read_excel(xls, sheet_name=0)
data_f2 = pd.read_excel(xls, sheet_name=1)
data_f3 = pd.read_excel(xls,sheet_name=2)
# print(data_f1)
# print(data_f2)
# print(data_f3)
# for item in data_f2.User:

##Filter Invoices in Sheet 3 if User is not found in Sheet 2
invoice_dataframe = data_f3[data_f3['User'].isin(data_f2['User'])]
# print(invoice_dataframe)


##filter all invoices posted by unauthorised users in sheet 3
unauth_dataFrame  =data_f2.loc[data_f2['A/P Invoice'].isin(['No Authorization','Read-Only'])]
# print(unauth_dataFrame)


# print(data_f3.User)
# print(unauth_dataFrame.User)


# for item1 in   data_f3.User:
#    if item1 == unauth_dataFrame.User:
#       print('muthu')

merged_left = pd.merge(left=data_f3, right=unauth_dataFrame, how='left', left_on='User', right_on='User')
data = 'Authorized'
merged_left = merged_left.fillna(data)
print(merged_left)


merged_left.to_excel(r'E:/Task2.xlsx', index = False)

from util import * 

sales=[] 

for count in range(1,11): 
    prompt='Enter the sales for stand ' + str(count) + ': ' 
    sales.append(read_int(prompt)) 

print('-' * 40)
print(sales)
print('-' * 40)

# print a heading
print('Sales figures')
# initialise the stand counter
count=1
# work through the sales figures and print them
for sales_value in sales:
    # print an item
    print('Sales for stand', count,'are',sales_value)
    # advance the stand counter
    count = count + 1      
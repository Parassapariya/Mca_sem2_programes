#write a progeame to create a bar chart for product sale using two coloums 1 product names,product sal(in thousands)

import matplotlib.pyplot as plt

product_names = ['TATA', 'BMW', 'HERO', 'ODI', 'MAHENDRA']
product_sales = [25, 40, 15, 30, 20]

plt.bar(product_names, product_sales, color='skyblue', edgecolor='black')

plt.title('Product Sales', fontsize=16)
plt.xlabel('Products', fontsize=14)
plt.ylabel('Sales (in Thousands)', fontsize=14)

output_path = r'C:\MCA2_Lab\DAV\chart images\product_sales_chart.png'
plt.savefig(output_path, format='png', dpi=300)
plt.show()

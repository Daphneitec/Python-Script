import pandas as pd
import pandasql
from pandasql import sqldf
missing_values = ["NaN", "n.a", "?"]
df = pd.read_csv(r"C:\\Users\\liud\\Documents\\Machine Learning\\Automobile_data.csv", na_values=missing_values)
##df = pd.read_csv(r"C:\\Users\\liud\\Documents\\Machine Learning\\Automobile_data.csv", na_values=missing_values)
print(df.head().to_string())
print(df.tail().to_string())
print(df.describe().to_string())
df1  = df [['company','price']][df.price==df['price'].max()]
print(df1.to_string())
df2 = df.query("company == 'toyota'")
print(df2.to_string())
print(df['company'].value_counts().to_string())
print(df.groupby('company')['price'].max().to_string())
myquery ="select company, \"body-style\",\"wheel-base\", price from df order by price"
mysqdf = sqldf(myquery)
print(mysqdf.to_string())
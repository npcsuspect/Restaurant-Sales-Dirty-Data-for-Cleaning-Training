import pandas as pd
import numpy as np

path = "D:/PP/datasets_csv/restaurant_sales_data.csv"
df = pd.read_csv(path)

#Привів у порядок типи даних
df["Order Date"] = pd.to_datetime(df["Order Date"])             #змінив тип даних з str на datetime
df['Quantity'] = df['Quantity'].fillna(0).astype(int)           #заповнив пусті значення в колонці Quantity на 0 та змінив тип даних з float на int (тому що кількість замовлених страв не може бути дробовим числом)
df["Order Total"] = df["Order Total"].fillna(0).astype(int)     #змінив тип даних з float на int (тому що сума замовлення не може бути дробовим числом)
df["Payment Method"] = df["Payment Method"].fillna("Unknown")   #заповнив пусті значення в колонці Payment Method на Unknown (не видаляючи, бо інші дані доступні для аналізу)

#Видалив пусті значення в колонках Item та Price (тому що вони є обов'язковими для аналізу в цьому випадку)
df = df.dropna(subset = ["Item", "Price"])                      #видалив пусті значення в колонках Item та Price(тому що вони є обов'язковими для аналізу в цьому випадку)

"""   Перевірка на розбіжності в даних між колонками Price та Quantity та Order Total
#df["Check Total"] = df["Price"] * df["Quantity"]               створив нову колонку Check Total, яка є добутком ціни та кількості замовлених страв
#df["Difference"] = df["Check Total"] - df["Order Total"]       створив нову колонку Difference, яка є різницею між Check Total та Order Total
#mismatches = df[df["Difference"] != 0]                         створив новий датафрейм mismatches, який містить рядки, де різниця між Check Total та Order Total не дорівнює нулю
#print(len(mismatches))                                         вивів кількість рядків у mismatches
"""

duplicates_count = df.duplicated().sum()                        #визначив кількість дублікатів у датафреймі
df["Item"] = df["Item"].str.strip().str.lower()                 #очистив колонку Item від пробілів та перевів всі значення в нижній регістр для уникнення дублювання через різні регістри
unique_items = df["Item"].unique()                              #визначив унікальні значення в колонці Item (перевірив в якому стані типи даних після цих маніпуляцій з даними df.dtypes)

# Визначив топ-5 найпопулярніших страв за кількістю замовлень
top_items = df.groupby("Item")["Quantity"].sum().sort_values(ascending=False).head(5)           

# Визначив топ-5 найпопулярніших страв за загальним виторгом 
top_items_revenue = df.groupby("Item")["Order Total"].sum().sort_values(ascending=False).head(5)

# Визначив продажі по дням тижня
df["Day of Week"] = df["Order Date"].dt.day_name()                  #створив нову колонку Day of Week, яка містить назви днів тижня на основі колонки Order Date
sales_by_day_0 = df.groupby("Day of Week")["Order Total"].sum()     #визначив загальний виторг по дням тижня

# Також можна виставити дні в правильному порядку, якщо потрібно, бо Pandas сортує дні як звичайні об'єкти в алфавітному порядку.
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]         #Створюємо правильний порядок днів тижня
df["Day of Week"] = pd.Categorical(df["Day of Week"], categories=days_order, ordered=True)          #Перетворюємо в категоріальний тип з правильним порядком днів тижня
sales_by_day_1 = df.groupby("Day of Week", observed=True)["Order Total"].sum()                      #Групуємо та сортуємо за порядком який встановили вище





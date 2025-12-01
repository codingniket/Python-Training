import pandas as pd

s = pd.DataFrame([1,2,3,4,5,6])
print(s)


df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)

df = pd.DataFrame(df)
print(df)


df.to_csv("student.csv",index=False)


df = pd.read_csv("student.csv")
print(df)

print(df.shape)

print(df.columns)

print(df.describe())

filter = df[(df["Marks"] > 70) & (df["Age"] > 22)]
print(filter)

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x > 60 else "Fail")

sorted = df.sort_values(by="Marks", ascending=False)
print(sorted)

df2 = df.copy()

df2.loc[2,"City"] = None

print(df2.isnull().sum())

df2 = df2.fillna("Unknown")

print(df2)

city = df2.groupby("City")["Name"].count()

avg = df2.groupby("City")["Marks"].mean()

print(avg,city)
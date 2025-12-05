import pymysql
import pandas as pd
from datetime import date, datetime

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root123",
    database="subscription_app"
)

def days_before_expiry(df):
    df["expiry_date"] = pd.to_datetime(df["expiry_date"])
    df["days_left"] = (df["expiry_date"] - pd.Timestamp.today()).dt.days
    return df

def subscription_age(df):
    df["age_days"] = (pd.Timestamp.today() - pd.to_datetime(df["start_date"])).dt.days
    return df

def status_sub(row):
    if row["days_left"] < 0:
        return "Expired"
    elif row["days_left"] <= 7:
        return "ExpiringSoon"
    else:
        return "Active"

# Load data
df = pd.read_sql("SELECT * FROM subscriptions", conn)

# Add calculated columns
df = days_before_expiry(df)
df["status"] = df.apply(status_sub, axis=1)
df = subscription_age(df)

print("Report 1")
print(df["status"].value_counts())

print("Report 2")
print(df[df["days_left"].between(0, 7)])

print("Report 3")
print(df[df["days_left"] < 0])

print("Report 4")
def renewal_value(df):
    price_map = {
    "Monthly": 1000,
    "Quarterly": 2700,
    "Yearly": 10000
    }
    df["renewal_value"] = df["plan_type"].map(price_map)
    forecast = df[df["days_left"] <= 30]["renewal_value"].sum()
    return forecast


# 1.
ten_days = df[(df["days_left"] <= 10) & (df["days_left"] > 0)]
print(ten_days)

# 2.
today = date.today()
today_month = today.month
comm = f"SELECT * FROM subscriptions WHERE MONTH(start_date) = {today_month}"
curr_month_sub = pd.read_sql(comm, conn)
print(curr_month_sub)

# 3.
comm = "SELECT * FROM subscriptions WHERE plan_type = 'Yearly' ORDER BY start_date DESC"
sorted_yearly_plan = pd.read_sql(comm, conn)
print(sorted_yearly_plan)

# 4.
comm = "SELECT * FROM subscriptions WHERE plan_type = 'Yearly' OR plan_type = 'Quarterly'"
more_than_monthly = pd.read_sql(comm, conn)
more_than_monthly = days_before_expiry(more_than_monthly)
more_than_monthly["status"] = more_than_monthly.apply(status_sub, axis=1)
active_more_than_monthly = more_than_monthly[more_than_monthly["status"] == "Active"]
print(active_more_than_monthly)

# 5.
comm = "SELECT * FROM subscriptions WHERE 'expiry_date' < 'start_date'"
check_data = pd.read_sql(comm, conn)
print(check_data)

# 6.Load data
df = pd.read_sql("SELECT * FROM subscriptions", conn)

#7.
df["created_at"] = pd.to_datetime(df["created_at"], format="%y-%m-%d %H:%M")
print(df.info())
print(df)

# 8.
df["expiry_date"] = pd.to_datetime(df["expiry_date"], format="%Y-%m-%d")
today = datetime.today()
df["days_overdue"] = (df["expiry_date"] - today).dt.days
days_overdue = df[df["days_overdue"] < 0]
print(days_overdue)

# 9.
df["next_billing_date"] = df["expiry_date"] + pd.Timedelta(days=1)
print(df)

# 10.
billing_unpaid = df[df["days_overdue"] < 0]
print(billing_unpaid)

# 11.
df = days_before_expiry(df)
df["status"] = df.apply(status_sub, axis=1)
df = subscription_age(df)


active = df[df["status"] == "Active"]
expired = df[df["status"] == "Expired"]
expiring_soon = df[df["status"] == "ExpiringSoon"]

print(active)
print(expired)
print(expiring_soon)

# 12.
remainder = df[(df["days_left"] <= 5) & (df["days_left"] > 0)]
for name in remainder['customer_name']:
    print(f"Hello {name} please resubscribe soon")

# 13.
df1 = subscription_age(df)
print(df1)


# 14.
total_customers = df.groupby("plan_type").count().reset_index()
print("Total Customers",total_customers)
age = df.groupby("plan_type")["age_days"].mean().reset_index()
print(age)
rev = renewal_value(df)
print(rev)


# 15.
df.to_csv("subscription_report.csv",index=False)
print("Exported successfully")

conn.close()
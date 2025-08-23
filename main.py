import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("advertising.csv")


df = df.drop(columns=["Radio","Newspaper"])
# plt.scatter(x = df["TV"], y = df["Sales"])
# plt.show()

# print(df)

# def loss_func(m,b, points):
#     total_error = 0
#     for i in range(len(points)):
#         x = points.iloc[i].TV
#         y = points.iloc[i].Sales
#         total_error += (y - (m *x + b)) ** 2
#     total_error / float(len(points))


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].TV
        y = points.iloc[i].Sales


        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b


m = 0
b = 0
L = 0.000001
epochs = 10000

for i in range(epochs):
    if (i % 50 == 0):
        print(i)
    m,b = gradient_descent(m, b, df, L)



print(m, b)
print(f"m: {m}")

plt.scatter(df.TV, df.Sales, color = "Black")
plt.plot(list(range(0, 300)), [m * x + b for x in range(0, 300)], color = "Red")
plt.show()

def r2_score(m, b, points):
    y_true = points["Sales"]
    y_pred = points["TV"] * m + b
    ss_res = ((y_true - y_pred) ** 2).sum()
    ss_tot = ((y_true - y_true.mean()) ** 2).sum()
    return 1 - (ss_res / ss_tot)

print("R²:", r2_score(m, b, df))



import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Đọc dữ liệu từ file CSV
file_path = 'real_estate.csv'
df = pd.read_csv(file_path)

# Tách đặc trưng (X) và nhãn (y)
x = df[["X1 transaction date", "X2 house age", "X3 distance to the nearest MRT station", 
        "X4 number of convenience stores", "X5 latitude", "X6 longitude"]]
y = df["Y house price of unit area"]

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Huấn luyện mô hình RandomForestRegressor
model = RandomForestRegressor(random_state = 42)
model.fit(X_train_scaled, y_train)

# Tạo giao diện người dùng với Streamlit
st.title("Dự đoán Giá Nhà")

st.write("""
    Nhập thông tin về một bất động sản để dự đoán giá của nó.
""")

# Giao diện nhập thông tin
transaction_date = st.number_input("Transaction Date", min_value=2000.0, max_value=2100.0, step=0.1, value=2013.5)
house_age = st.number_input("House Age", min_value=0.0, max_value=100.0, step=0.1, value=6.5)
distance_to_mrt = st.number_input("Distance to the nearest MRT station", min_value=0.0, max_value=5000.0, step=0.1, value=90.45606)
num_stores = st.number_input("Number of convenience stores", min_value=0, max_value=50, step=1, value=9)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.0001, value=24.97433)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.0001, value=121.5431)

# Tạo dữ liệu mới từ các giá trị nhập vào
new_data = [[transaction_date, house_age, distance_to_mrt, num_stores, latitude, longitude]]

# Chuẩn hóa dữ liệu mới
new_data_scaled = scaler.transform(new_data)

# Dự đoán giá nhà
if st.button('House Price'):
    predicted_price = model.predict(new_data_scaled)
    st.write(f"House price of unit area: {predicted_price[0]:.2f} (đơn vị: giá trên mỗi m²)")

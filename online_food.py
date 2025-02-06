import streamlit as st

# Online Food Delivery System
menu = {
    "Burger": (5.99, "Fast Food"),
    "Pizza": (8.99, "Fast Food"),
    "Pasta": (7.49, "Italian"),
    "Salad": (4.99, "Healthy"),
    "Sushi": (12.99, "Japanese")
}

orders = []
unique_customers = set()

# Function to place an order
def place_order(customer_name, selected_items):
    total_bill = sum(menu[item][0] for item in selected_items)
    order_id = len(orders) + 1
    orders.append((order_id, customer_name, selected_items, total_bill))
    unique_customers.add(customer_name)
    return order_id, total_bill

# Function to calculate total revenue
def total_revenue():
    return sum(order[3] for order in orders)

# Streamlit UI
st.title("Online Food Delivery System")

menu_display = {item: f"${price} ({category})" for item, (price, category) in menu.items()}
st.sidebar.header("Menu")
st.sidebar.write(menu_display)

menu_items = list(menu.keys())

choice = st.sidebar.selectbox("Menu", ["Place Order", "View Total Revenue", "View Unique Customers"])

if choice == "Place Order":
    customer_name = st.text_input("Enter Customer Name")
    selected_items = st.multiselect("Select Items", menu_items)
    
    if st.button("Place Order"):
        if customer_name and selected_items:
            order_id, bill = place_order(customer_name, selected_items)
            st.success(f"Order {order_id} placed! Total Bill: ${bill:.2f}")
        else:
            st.error("Please enter a name and select items.")

elif choice == "View Total Revenue":
    if st.button("Show Revenue"):
        revenue = total_revenue()
        st.write(f"Total Revenue: ${revenue:.2f}")

elif choice == "View Unique Customers":
    if st.button("Show Customers"):
        st.write(unique_customers if unique_customers else "No customers yet.")

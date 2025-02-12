import streamlit as st

# ---- FUNCTIONS ----
def calculate_new_rating(current_rating, total_reviews, target_rating):
    """
    Calculates the number of 5-star reviews needed to reach the target rating.
    """
    current_total = current_rating * total_reviews
    new_reviews_needed = 0

    while (current_total + (5 * new_reviews_needed)) / (total_reviews + new_reviews_needed) < target_rating:
        new_reviews_needed += 1

    return new_reviews_needed

def estimate_revenue_increase(new_reviews_needed, clv):
    """
    Estimates the additional revenue generated by acquiring more reviews.
    Assumes each review gets ~50 views per month and influences potential buyers.
    """
    estimated_revenue = new_reviews_needed * 50 * 0.02 * clv  # 50 views/month * 2% conversion * CLV
    return estimated_revenue


# ---- STREAMLIT UI ----
st.set_page_config(page_title="Review Impact Calculator", page_icon="⭐", layout="centered")

# Title (smaller for cleaner look)
st.markdown("<h2 style='text-align: center;'>⭐ Review Impact Calculator</h2>", unsafe_allow_html=True)

# Instructions
st.markdown(
    """
    🔹 Enter your **current Google rating**, **number of reviews**, and **target rating**.  
    🔹 Adjust your **customer lifetime value** to see how increasing your rating impacts revenue.  
    """,
    unsafe_allow_html=True
)

# 📌 Sidebar for Inputs
st.sidebar.header("🔢 Enter Your Business Data")
current_rating = st.sidebar.slider("⭐ Current Google Rating", 1.0, 5.0, 4.00, 0.01)
total_reviews = st.sidebar.number_input("📌 Current Number of Google Reviews", min_value=1, value=50, step=1)
target_rating = st.sidebar.slider("🎯 Desired Google Rating", 1.0, 5.0, 4.6, 0.01)
clv = st.sidebar.number_input("💰 Customer Lifetime Value ($)", min_value=10, value=100, step=10)

# 🧮 Calculations
reviews_needed = calculate_new_rating(current_rating, total_reviews, target_rating)
revenue_increase = estimate_revenue_increase(reviews_needed, clv)
new_views = reviews_needed * 50
new_customers = reviews_needed * 50 * 0.02

# 📊 Display results with a two-column layout
st.markdown("---")
st.subheader("📊 Results")

col1, col2 = st.columns(2)
col1.metric(f"⭐ Reviews Needed to Get to {target_rating}", f"{reviews_needed} more 5-stars")
col2.metric("💰 Estimated Monthly Revenue Increase", f"${revenue_increase:,.2f}")

# Revenue explanation below the metric
st.markdown(
    f"""
    <p style="text-align: center; font-size: 16px; color: gray;">
    Increase if you achieve the reviews needed.
    </p>
    """,
    unsafe_allow_html=True
)

# 📌 How It Is Calculated Section
st.markdown("---")
st.subheader("📊 How It Is Calculated")
st.markdown(
    f"""
    - To reach **{target_rating} stars**, you need **{reviews_needed} more 5-star reviews**.
    - Each **new review** brings in **~50 more views per month**.
    - **2% of those views** (1 out of every 50 people) will take action (call, visit, book, or buy).
    - If your **average customer lifetime value is** **${clv}**, then every **new review** contributes to measurable revenue growth.
    """
)

# 📌 Results Using Your Input Section
st.markdown("---")
st.subheader("📊 Results Using Your Input")
st.markdown(
    f"""
    - **{reviews_needed} more 5-star reviews** → Generates **{new_views:,.0f} new views per month**.  
    - **2% conversion rate** → Leads to **{new_customers:,.0f} new paying customers**.  
    - **At** ${clv} **per customer** → You could add **${revenue_increase:,.2f}** in monthly revenue.
    """,
    unsafe_allow_html=True
)

# 🎯 Call-To-Action Section
st.markdown("---")
st.subheader("🚀 Want to Increase Your Google Rating?")

st.markdown(
    """
    📈 More **5-star reviews** = More **visibility**, More **trust**, and More **customers**.  
    🔥 Get **expert guidance** to improve your online reputation and **maximize revenue**.
    
    **Book a 30-minute session for $40 USD** and learn:  
    ✅ How to **get more 5-star reviews efficiently**  
    ✅ How to **handle negative reviews** without hurting your business  
    ✅ How to **optimize your Google Business Profile** for better rankings  
    """,
    unsafe_allow_html=True
)

# 🔗 Clickable CTA Button (Mobile-Optimized)
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://tidycal.com/m52nvnm/30-minute-meeting" target="_blank">
            <button style="background-color:#28a745; border:none; color:white; padding:14px 28px;
            text-align:center; text-decoration:none; display:inline-block; font-size:18px;
            margin:12px 2px; cursor:pointer; border-radius:8px; width:90%;">
            📅 Book a 30-Minute Reputation Growth Session – $40
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

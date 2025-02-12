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
    Assumes each review gets ~100 views per month and influences potential buyers.
    """
    estimated_revenue = new_reviews_needed * 100 * 0.02 * clv  # 100 views/month * 2% conversion * CLV
    return estimated_revenue


# ---- STREAMLIT UI ----
st.set_page_config(page_title="Google Reviews Impact Calculator", page_icon="⭐")

# 🔥 Persuasive Header
st.title("🚀 Google Reviews & Revenue Impact Calculator")
st.subheader("See how improving your online reviews can boost your business revenue!")

# 📌 Sidebar for Inputs
st.sidebar.header("Step 1 of 2: Input Your Business Data")
current_rating = st.sidebar.slider("⭐ Current Google Rating", 1.0, 5.0, 4.2, 0.1)
total_reviews = st.sidebar.number_input("📌 Current Number of Google Reviews", min_value=1, value=100, step=1)
target_rating = st.sidebar.slider("🎯 Desired Google Rating", 1.0, 5.0, 4.6, 0.1)
clv = st.sidebar.number_input("💰 Lifetime Customer Value ($)", min_value=10, value=1000, step=10)

# 🧮 Calculations
reviews_needed = calculate_new_rating(current_rating, total_reviews, target_rating)
revenue_increase = estimate_revenue_increase(reviews_needed, clv)

# 📊 Display results with better formatting
st.markdown("---")
st.subheader("🔍 Review Growth Insights")

col1, col2 = st.columns(2)
col1.metric(f"⭐ Reviews Needed to Get to {target_rating}", f"{reviews_needed} more 5-stars", delta=f"+{reviews_needed}")
col2.metric("💰 Estimated Monthly Revenue Increase", f"${revenue_increase:,.2f}")

st.progress(min(reviews_needed / 100, 1.0))  # Simple progress bar for visuals

# 📌 Explanation Behind the Calculation
st.markdown("---")
st.subheader("📈 How We Calculate Revenue Increase")
st.write(
    f"""
    - Each **new review** brings in **~100 more views per month**.
    - **2% of those views** (2 out of every 100 people) will take action (call, visit, book, or buy).
    - If your average customer lifetime value is **${clv}**, then every **new review** can bring measurable revenue growth.
    
    **Why 2% Conversion Rate?**  
    - Based on local business benchmarks, a **2% conversion rate** from new views generated by reviews is a **solid estimate**.
    - Businesses with **optimized Google Business Profiles** and **active reviews** often reach **5-10% conversion rates**.
    - **High-intent searches ("best near me")** make users more likely to convert.
    """
)

# 🎯 Call-To-Action Section
st.markdown("---")
st.subheader("🚀 Ready to Get More 5-Star Reviews?")

st.markdown(
    """
    **Imagine what just a few more 5-star reviews could do for your business.**  
    More **trust**. More **visibility**. More **customers**. More **revenue**.  

    **On this free 30-minute strategy call, we will:**  
    ✅ Show you exactly how to **get more 5-star reviews effortlessly**  
    ✅ Reveal how **Google’s algorithm rewards recent, high-quality reviews**  
    ✅ Help you build a **simple action plan** to grow your business through reputation management  

    **Don't leave revenue on the table.** Click below to book your free session now!  
    """
)

# 🔗 Clickable CTA Button to Your TidyCal Booking Page
st.markdown(
    """
    <a href="https://tidycal.com/m52nvnm/30-minute-meeting" target="_blank">
        <button style="background-color:#28a745; border:none; color:white; padding:12px 24px;
        text-align:center; text-decoration:none; display:inline-block; font-size:18px;
        margin:12px 2px; cursor:pointer; border-radius:6px;">📅 Book a Free 30-Minute Strategy Call</button>
    </a>
    """,
    unsafe_allow_html=True
)

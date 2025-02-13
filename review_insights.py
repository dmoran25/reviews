import streamlit as st

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Star Rating Calculator", page_icon="⭐", layout="centered")

# Session State for Managing Visibility
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Show title & new description only if form has NOT been submitted
if not st.session_state.submitted:
    st.markdown(
        """
        <div style="background-color: #08bf81; padding: 20px; border-radius: 8px; text-align: center;">
            <h2 style="color: #FFFFFF; font-weight: bold;">⭐ Star Rating Calculator</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        **Calculate how many 5-star Google reviews your business needs to improve your rating and see the impact these reviews will have on your revenue.**
        """,
        unsafe_allow_html=True
    )

# FORM: User enters data
if not st.session_state.submitted:
    with st.form("review_calculator_form"):
        st.markdown("### Step 1 of 2")
        current_rating = st.number_input("Current Google Rating", min_value=1.0, max_value=5.0, value=4.0, step=0.01)
        total_reviews = st.number_input("Current Number of Google Reviews", min_value=1, value=50, step=1)
        target_rating = st.number_input("Desired Google Rating", min_value=1.0, max_value=5.0, value=4.6, step=0.01)
        clv = st.number_input("Customer Lifetime Value ($)", min_value=10, value=100, step=10)

        # Centered & Bigger Calculate Button (Styled)
        st.markdown(
            """
            <style>
                .calculate-button-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 20px;
                }
                div.stButton > button:first-child {
                    background-color: #08bf81;
                    color: white;
                    padding: 20px 50px;
                    border-radius: 12px;
                    font-size: 24px;
                    font-weight: bold;
                    width: 100%;
                    text-align: center;
                }
                div.stButton > button:first-child:hover {
                    background-color: #06a56f;
                }
            </style>
            <div class="calculate-button-container">
            """,
            unsafe_allow_html=True
        )

        submitted = st.form_submit_button("Calculate my rating")

        if submitted:
            st.session_state.submitted = True
            st.session_state.current_rating = current_rating
            st.session_state.total_reviews = total_reviews
            st.session_state.target_rating = target_rating
            st.session_state.clv = clv
            st.rerun()

# Show results if submitted
if st.session_state.submitted:
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
        return new_reviews_needed * 50 * 0.02 * clv  # 50 views/month * 2% conversion * CLV

    # Retrieve stored values
    reviews_needed = calculate_new_rating(st.session_state.current_rating, st.session_state.total_reviews, st.session_state.target_rating)
    revenue_increase = estimate_revenue_increase(reviews_needed, st.session_state.clv)

    # 📊 Results Display: Reviews Needed
    st.markdown("---")
    st.markdown(
        f"""
        <div style="background-color: #EFF8F0; padding: 16px; border-radius: 8px; text-align: center;">
            <h4 style="color: #28a745;">Your Results</h4>
            <h1 style="font-size: 72px; font-weight: bold;">{reviews_needed}</h1>
            <p style="font-size: 20px; color: #555;">5-star reviews needed to achieve a <strong>{st.session_state.target_rating}</strong> star rating.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 📈 Styled Revenue Impact
    st.markdown("---")
    st.markdown(
        f"""
        <div style="background-color: #FFF3CD; padding: 16px; border-radius: 8px; text-align: center;">
            <h4 style="color: #D39E00;">Revenue Impact</h4>
            <h1 style="font-size: 72px; font-weight: bold;">${revenue_increase:,.2f}</h1>
            <p style="font-size: 20px; color: #555;">Estimated monthly revenue increase.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🔄 Calculate Again Button (Centered & Styled)
    if st.button("🔄 Calculate Again"):
        st.session_state.submitted = False
        st.rerun()

    # 🎯 Call-To-Action Section
    st.markdown("---")
    st.subheader("🚀 Want a Custom Plan to Increase Your Google Ranking?")

    st.markdown(
        """
        **Book a 30-minute strategy session for $40 USD and get:**  
        
        📍 **Google My Business Audit**: Find out what’s holding back your ranking and how to fix it.  
        🔍 **Keyword Research**: Discover the top search terms potential clients are using.  
        🗓 **90-Day Content Strategy**: A simple roadmap to attract more local clients.  
        ⭐ **Review Growth Plan**: The easiest way to get more 5-star reviews—without awkward asks.  
        """,
        unsafe_allow_html=True
    )

    # 🔗 Clickable CTA Button (Mobile-Optimized)
    st.markdown(
        """
        <div style="text-align:center;">
            <a href="https://tidycal.com/m52nvnm/30-minute-meeting" target="_blank">
                <button style="background-color:#08bf81; border:none; color:white; padding:20px 50px;
                text-align:center; text-decoration:none; display:inline-block; font-size:24px;
                font-weight: bold;
                margin:12px 2px; cursor:pointer; border-radius:12px; width:100%;">
                📅 Book Your $40 Strategy Session Now
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

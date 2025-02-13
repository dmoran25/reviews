import streamlit as st

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Revenue Impact Calculator", page_icon="💰", layout="centered")

# Detect if the app is embedded in an iframe
query_params = st.query_params
is_embedded = query_params.get("embedded", "false").lower() == "true"

# Hide Streamlit toolbar, footer, and menu when embedded
if is_embedded:
    hide_streamlit_style = """
        <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Session State for Managing Visibility
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Show title & new description only if form has NOT been submitted
if not st.session_state.submitted:
    st.markdown(
        """
        <div style="background-color: #08bf81; padding: 20px; border-radius: 8px; text-align: center;">
            <h2 style="color: #FFFFFF; font-weight: bold;">💰 Revenue Impact Calculator</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        **See how increasing your 5-star Google reviews can drive more revenue for your business.**  
        Find out how many reviews you need and how much additional revenue you could generate.
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
            """,
            unsafe_allow_html=True
        )

        submitted = st.form_submit_button("Calculate Revenue Impact")

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
        current_total = current_rating * total_reviews
        new_reviews_needed = 0
        while (current_total + (5 * new_reviews_needed)) / (total_reviews + new_reviews_needed) < target_rating:
            new_reviews_needed += 1
        return new_reviews_needed

    def estimate_revenue_increase(new_reviews_needed, clv):
        return new_reviews_needed * 50 * 0.02 * clv  # 50 views/month * 2% conversion * CLV

    reviews_needed = calculate_new_rating(st.session_state.current_rating, st.session_state.total_reviews, st.session_state.target_rating)
    revenue_increase = estimate_revenue_increase(reviews_needed, st.session_state.clv)

    # 📊 Results Display
    st.markdown("---")
    st.markdown(f"<h1 style='text-align:center; font-size:72px;'>{reviews_needed}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-size:20px;'>More 5-star reviews needed to reach {st.session_state.target_rating} stars.</p>", unsafe_allow_html=True)

    # 📈 Revenue Impact
    st.markdown("---")
    st.markdown(f"<h1 style='text-align:center; font-size:72px;'>${revenue_increase:,.2f}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-size:20px;'>Potential additional monthly revenue.</p>", unsafe_allow_html=True)

    # 🔄 Recalculate Button
    if st.button("🔄 Recalculate Your Revenue Potential"):
        st.session_state.submitted = False
        st.rerun()

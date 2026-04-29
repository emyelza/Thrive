"""
Thrive — Student Financial Companion
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import datetime, timedelta
import io
import html
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Thrive — Student Finance",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# STYLESHEET
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,400;1,9..144,700&family=League+Spartan:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');

html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #FAFAF7;
    background-image:
        linear-gradient(rgba(214, 211, 240, 0.35) 1px, transparent 1px),
        linear-gradient(90deg, rgba(214, 211, 240, 0.35) 1px, transparent 1px);
    background-size: 40px 40px;
    color: #1A1A2E;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* ── Typography Elements ── */
.fraunces { font-family: 'Fraunces', serif; }
.dm-sans { font-family: 'DM Sans', sans-serif; }

/* ── Hero section ── */
.hero {
    position: relative;
    padding: 4rem 1rem 3rem;
    margin-bottom: 1rem;
}

.brand {
    position: absolute;
    top: 10px;
    right: 20px;
    font-family: 'Fraunces', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #555;
}

.bonjour {
    font-family: 'stella aesta', serif;
    font-style: italic;
    font-size: 4rem;
    font-weight: 700;
    color: #111;
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
    line-height: 1.1;
}

.tagline {
    font-family: 'League Spartan', sans-serif;
    font-size: 1.1rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 0;
}

.cta {
    font-family: 'League Spartan', sans-serif;
    font-size: 1rem;
    color: #333;
    margin-top: 0.8rem;
    font-weight: 500;
    margin-bottom: 0;
}

.subline {
    font-family: 'League Spartan', sans-serif;
    font-size: 0.9rem;
    color: #777;
    margin-top: 1rem;
    margin-bottom: 2rem;
}

/* Base button defaults reset */
div[data-testid="stButton"] button {
    border-radius: 50px;
    font-weight: 500;
    padding: 0.5rem 1.5rem;
}

/* The actual "Primary" Streamlit Button Override */
div[data-testid="stButton"] button[kind="primary"] {
    background-color: #5B4FCF !important;
    color: #FFFFFF !important;
    border: none !important;
}

/* ── Cards ── */
.card {
    background: #FFFFFF;
    border: 1px solid #EBEBEB;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px rgba(26, 26, 46, 0.03);
}

.section-head {
    font-family: 'Fraunces', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #1A1A2E;
    margin-bottom: 1.5rem;
}

/* ── Metric tiles ── */
.metric-grid { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem; }
.metric-tile {
    flex: 1; min-width: 200px;
    background: #FFFFFF;
    border: 1px solid #EBEBEB;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(26, 26, 46, 0.03);
}

/* Left borders */
.border-red    { border-left: 4px solid #E8503A; }
.border-indigo { border-left: 4px solid #5B4FCF; }

.metric-label { 
    font-family: 'DM Sans', sans-serif;
    font-size: 0.8rem; 
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #7A7A9A; 
    margin-bottom: 0.5rem; 
}

.metric-value {
    font-family: 'Fraunces', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #1A1A2E;
    line-height: 1;
}

.metric-sub { 
    font-size: 0.85rem; 
    color: #7A7A9A; 
    margin-top: 0.5rem; 
}

/* ── Banner / Survival ── */
.survival-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 2.5rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    border: 1px solid #EBEBEB;
}

.survival-banner.safe    { background: #E8F7EE; }
.survival-banner.warning { background: #FDF6E3; }
.survival-banner.danger  { background: #FFF0EE; }

.survival-block {
    display: flex;
    flex-direction: column;
}

.survival-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 500;
    color: #7A7A9A;
    margin-bottom: 0.3rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.survival-value {
    font-family: 'Fraunces', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #1A1A2E;
}

/* ── Risk badge ── */
.risk-badge {
    display: inline-block;
    padding: 0.4rem 1.2rem;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 1px;
}
.risk-safe    { background: #3DAA6E; color: #FFFFFF; }
.risk-warning { background: #F0A500; color: #FFFFFF; }
.risk-danger  { background: #E8503A; color: #FFFFFF; }

/* ── Insight rows ── */
.insight-row {
    display: flex; align-items: center; gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid #EBEBEB;
}
.insight-row:last-child { border-bottom: none; }
.insight-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: #5B4FCF;
    flex-shrink: 0;
}
.insight-dot.amber { background: #F0A500; }
.insight-dot.red   { background: #E8503A; }
.insight-text { font-size: 1.05rem; color: #1A1A2E; line-height: 1.5; font-weight: 500; }

/* ── Advisory ── */
.advisory-item {
    background: rgba(91, 79, 207, 0.05);
    border-left: 4px solid #5B4FCF;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    border-radius: 0 12px 12px 0;
    font-size: 1.05rem;
    color: #1A1A2E;
    font-weight: 500;
}

/* ── Table ── */
.stDataFrame { border: 1px solid #EBEBEB !important; border-radius: 12px; overflow: hidden; }

/* ── Landing Area ── */
.landing-steps {
    display: flex;
    gap: 2rem;
    margin-top: 2rem;
}
.step-card {
    flex: 1;
    background: #FFFFFF;
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid #EBEBEB;
    box-shadow: 0 4px 20px rgba(26, 26, 46, 0.03);
}
.step-number {
    font-family: 'Fraunces', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #D6D3F0;
    margin-bottom: 1rem;
    line-height: 1;
}
.step-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: #1A1A2E;
    margin-bottom: 0.5rem;
}
.step-desc {
    font-size: 0.95rem;
    color: #7A7A9A;
    line-height: 1.5;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
CATEGORY_RULES = {
    "Food & Dining":           ["swiggy","zomato","instamart","zepto","restaurant",
                                "cafe","coffee","tea","hotel","dominos","mcdonalds","kfc"],
    "Shopping":                ["amazon","flipkart","meesho","nykaa","myntra","ajio",
                                "mart","store","bigbasket","reliance"],
    "Entertainment":           ["bookmyshow","movie","cinema","netflix","spotify",
                                "hotstar","pub","bar","club","district"],
    "Transport":               ["uber","ola","rapido","fuel","petrol","diesel",
                                "metro","bus","irctc","redbus"],
    "Essentials":              ["grocery","supermarket","pharmacy","medical",
                                "electricity","water","gas","hospital"],
    "Subscriptions & Digital": ["recharge","mobile","data","google","apple",
                                "subscription","jio","airtel","vi"],
}

CATEGORY_PALETTE = {
    "Food & Dining": "#cdb4db",
    "Shopping": "#ffc8dd",
    "Entertainment": "#ffafcc",
    "Transport": "#bde0fe",
    "Essentials": "#a2d2ff",
    "Subscriptions & Digital": "#a8dadc",
    "Unknown UPI / Needs Tagging": "#f1faee"
}

SAMPLE_CSV = """Date,Description,Amount,Type,Balance
2024-03-01,SALARY CREDIT,15000,Credit,15000
2024-03-02,SWIGGY ORDER 8812,320,Debit,14680
2024-03-03,UBER TRIP BLR,180,Debit,14500
2024-03-04,AMAZON PURCHASE BOOK,499,Debit,14001
2024-03-05,UPI/rk9182@ybl,500,Debit,13501
2024-03-06,NETFLIX SUBSCRIPTION,199,Debit,13302
2024-03-07,ZOMATO ORDER 4421,450,Debit,12852
2024-03-08,MEDICAL PHARMACY,230,Debit,12622
2024-03-09,METRO CARD RECHARGE,200,Debit,12422
2024-03-10,UPI/unknown8821@okaxis,300,Debit,12122
2024-03-11,BOOKMYSHOW TICKET,350,Debit,11772
2024-03-12,SWIGGY ORDER 9922,280,Debit,11492
2024-03-13,AIRTEL RECHARGE,299,Debit,11193
2024-03-14,FLIPKART ORDER,1299,Debit,9894
2024-03-15,UBER TRIP,95,Debit,9799
2024-03-16,UPI/pay2314@okhdfc,400,Debit,9399
2024-03-17,ZOMATO ORDER,320,Debit,9079
2024-03-18,GROCERY STORE,650,Debit,8429
2024-03-19,COFFEE SHOP,180,Debit,8249
2024-03-20,OLA RIDE,120,Debit,8129
"""

# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def categorize(desc: str) -> str:
    d = desc.lower()
    for cat, keywords in CATEGORY_RULES.items():
        if any(k in d for k in keywords):
            return cat
    return "Unknown UPI / Needs Tagging"


def parse_dataframe(df: pd.DataFrame):
    """Normalize columns and extract key fields safely."""
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]

    desc_col = next((c for c in df.columns if any(k in c for k in
                     ["desc","narr","remark","detail","particular","particulars"])), df.columns[1] if len(df.columns) > 1 else None)
    amt_col  = next((c for c in df.columns if "amount" in c or "amt" in c or "debit" in c), df.columns[2] if len(df.columns) > 2 else None)
    type_col = next((c for c in df.columns if "type" in c or "cr_dr" in c), None)
    date_col = next((c for c in df.columns if "date" in c), df.columns[0] if len(df.columns) > 0 else None)
    bal_col  = next((c for c in df.columns if "balance" in c or "bal" in c), None)

    if not date_col or not amt_col or not desc_col:
        return pd.DataFrame(), None, None, None, 0.0

    df[amt_col] = pd.to_numeric(
        df[amt_col].astype(str).str.replace(",","").str.replace("₹",""), errors="coerce"
    ).fillna(0).abs()

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", dayfirst=True)
    df = df.dropna(subset=[date_col])

    if type_col:
        debits = df[df[type_col].astype(str).str.lower().str.contains("debit|dr|withdrawal", na=False)].copy()
    else:
        debits = df.copy()

    balance = 0.0
    if bal_col:
        valid_bal = pd.to_numeric(df[bal_col].astype(str).str.replace(",",""), errors="coerce").dropna()
        if not valid_bal.empty:
            balance = valid_bal.iloc[-1]

    if not debits.empty:
        debits["Category"] = debits[desc_col].astype(str).apply(categorize)

    return debits, desc_col, amt_col, date_col, balance


def compute_survival(debits, amt_col, date_col, balance):

    # Use last 30 days safely
    max_date = debits[date_col].max()

    if pd.isna(max_date):
        return None

    cutoff = max_date - pd.Timedelta(days=30)
    recent = debits[debits[date_col] >= cutoff]

    if recent.empty:
        recent = debits.copy()

    total_spent = recent[amt_col].sum()
    if pd.isna(total_spent):
        total_spent = 0.0

    n_days = recent[date_col].dt.date.nunique()
    burn_rate = total_spent / n_days if n_days > 0 else 0

    #  THESE MUST ALIGN WITH burn_rate (same indentation level)
    days_left = int(balance / burn_rate) if burn_rate > 0 else 999
    zero_date = datetime.today() + timedelta(days=days_left)
    today      = datetime.today()
    month_end  = today.replace(day=28)
    days_to_me = (month_end - today).days

    if days_left > days_to_me + 7:
        risk = "SAFE"
    elif days_left >= days_to_me - 3:
        risk = "WARNING"
    else:
        risk = "DANGER"

    return {
        "total_spent":  total_spent,
        "balance":      balance,
        "burn_rate":    burn_rate,
        "days_left":    days_left,
        "zero_date":    zero_date,
        "risk":         risk,
        "n_days":       n_days,
    }


def behavioral_insights(debits, amt_col, date_col):
    """Return list of (color, text) insight tuples."""
    insights = []

    small = debits[debits[amt_col] < 200]
    if len(small) >= 3:
        pct = round(small[amt_col].sum() / debits[amt_col].sum() * 100, 1)
        insights.append(("amber",
            f"Lots of small purchases — individually fine, but they add up to {pct}% of what you've spent."))

    debits_cpy = debits.copy()
    debits_cpy["_dow"] = debits_cpy[date_col].dt.dayofweek
    weekend = debits_cpy[debits_cpy["_dow"] >= 5][amt_col].sum()
    weekday = debits_cpy[debits_cpy["_dow"] < 5][amt_col].sum()
    if weekend > weekday * 0.4:
        insights.append(("amber",
            f"You spend noticeably more on weekends — ₹{weekend:,.0f} versus ₹{weekday:,.0f} on weekdays. Worth keeping an eye on."))

    rep = debits[amt_col].value_counts()
    rep = rep[rep >= 2]
    if not rep.empty:
        val = rep.index[0]
        insights.append(("indigo",
            f"You've paid ₹{val:.0f} exactly {int(rep.iloc[0])} times. Might be a subscription or a habit."))

    food_spend = debits[debits["Category"] == "Food & Dining"][amt_col].sum()
    food_pct   = food_spend / debits[amt_col].sum() * 100 if debits[amt_col].sum() else 0
    if food_pct > 25:
        insights.append(("red",
            f"Nearly {food_pct:.0f}% of your spending goes to food and dining. That's on the higher side for a student budget."))

    if not insights:
        insights.append(("indigo", "No noticeable spending quirks this time. You're keeping it pretty standard."))

    return insights


def smart_advisory(survival, debits, amt_col):
    """Return list of advisory strings."""
    advs = []
    risk = survival["risk"]

    if risk in ("WARNING","DANGER"):
        advs.append("Cut back on non-essentials by even 15% and your money lasts noticeably longer.")

    small_count = (debits[amt_col] < 200).sum()
    if small_count >= 3:
        advs.append("Group those frequent coffee and transport costs into a weekly spending limit. It stops the slow drain.")

    food_pct = debits[debits["Category"]=="Food & Dining"][amt_col].sum() / debits[amt_col].sum() * 100 if debits[amt_col].sum() else 0
    if food_pct > 25:
        advs.append("Cooking a few more meals at home could save you 20–35% on food each month. Swiggy adds up faster than you think.")

    debits_copy = debits.copy()
    debits_copy["_dow"] = pd.to_datetime(debits[debits.columns[0]], errors="coerce").dt.dayofweek
    weekend_spend = debits_copy[debits_copy["_dow"] >= 5][amt_col].sum()
    if weekend_spend > survival["total_spent"] * 0.35:
        advs.append("Your weekends are where a lot of the budget goes. A spending limit for Saturdays alone could make a real difference.")

    if risk == "DANGER":
        advs.append("Things are looking a bit tight. You might want to pause any non-essential subscriptions until the next recharge.")

    if not advs:
        advs.append("Keep doing what you're doing. Your spending habits look well balanced.")

    return advs

# ─────────────────────────────────────────────────────────────────────────────
# UI — HERO SECTION
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="brand">Thrive</div>

  <h1 class="Helo">Helo.</h1>

  <p class="tagline">
    Your money should last the month.<br>
    We make sure it does.
  </p>

  <p class="cta">
    Upload your bank statement to see where your money is going.
  </p>

  <p class="subline">
    Thrive — your financial companion for getting through the semester.
  </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# BUTTONS & UPLOAD LOGIC
# ─────────────────────────────────────────────────────────────────────────────
col_upload, col_sample, _ = st.columns([1.5, 1.5, 4])

with col_upload:
    uploaded = st.file_uploader(
        "Upload your statement",
        type=["csv"],
        label_visibility="collapsed"
    )

with col_sample:
    if st.button("Try with sample data", key="sample_btn"):
        st.session_state["sample"] = True

# ─────────────────────────────────────────────────────────────────────────────
# DATA PROCESSING
# ─────────────────────────────────────────────────────────────────────────────
df_raw = None
if uploaded:
    try:
        df_raw = pd.read_csv(uploaded)
    except Exception as e:
        st.error(f"Could not parse file: {e}")
elif st.session_state.get("sample"):
    df_raw = pd.read_csv(io.StringIO(SAMPLE_CSV))

# ─────────────────────────────────────────────────────────────────────────────
# MAIN DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
if df_raw is not None:
    req_cols = ['date', 'amount']
    df_raw_cols = [str(c).lower() for c in df_raw.columns]
    if not all(any(req in c for c in df_raw_cols) for req in req_cols):
        st.error("This doesn't look like a standard bank statement. Could not find 'Date' and 'Amount' columns.")
        st.stop()
        
    st.markdown('<hr style="border: 0; border-top: 1px dashed #D6D3F0; margin-bottom: 2rem;"/>', unsafe_allow_html=True)
    
    current_hash = hash(df_raw.to_string())
    if "raw_data_hash" not in st.session_state or st.session_state["raw_data_hash"] != current_hash:
        debits, desc_col, amt_col, date_col, balance = parse_dataframe(df_raw.copy())
        st.session_state["debits"] = debits
        st.session_state["desc_col"] = desc_col
        st.session_state["amt_col"] = amt_col
        st.session_state["date_col"] = date_col
        st.session_state["balance"] = balance
        st.session_state["raw_data_hash"] = current_hash
    else:
        debits = st.session_state["debits"]
        desc_col = st.session_state["desc_col"]
        amt_col = st.session_state["amt_col"]
        date_col = st.session_state["date_col"]
        balance = st.session_state["balance"]

    if debits.empty:
        st.warning("We couldn't find any withdrawals in this file. Make sure it's a valid statement.")
        st.stop()

    if balance == 0.0:
        st.markdown("<div style='margin-bottom: 1rem'>We couldn't automatically find your current balance.</div>", unsafe_allow_html=True)
        balance = st.number_input(
            "What's your current account balance? (₹)",
            min_value=0.0, value=0.0, step=100.0
        )

    survival = compute_survival(debits, amt_col, date_col, balance)

    if not survival:
        st.warning("Not enough data to crunch the numbers just yet.")
        st.stop()

    # SECTION: SUMMARY METRICS
    st.markdown(f"""
    <div class="metric-grid">
      <div class="metric-tile border-indigo">
        <div class="metric-label">Current Balance</div>
        <div class="metric-value">₹{balance:,.0f}</div>
      </div>
      <div class="metric-tile border-red">
        <div class="metric-label">Total Spent</div>
        <div class="metric-value">₹{survival['total_spent']:,.0f}</div>
        <div class="metric-sub">over {survival['n_days']} days</div>
      </div>
      <div class="metric-tile">
        <div class="metric-label">Daily Burn</div>
        <div class="metric-value">₹{survival['burn_rate']:,.0f}</div>
        <div class="metric-sub">per day</div>
      </div>
      <div class="metric-tile">
        <div class="metric-label">Avg Transaction</div>
        <div class="metric-value">₹{(survival['total_spent'] / len(debits) if len(debits) else 0):,.0f}</div>
        <div class="metric-sub">{len(debits)} transactions</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # SECTION: SURVIVAL PREDICTION
    st.markdown('<div class="section-head">How long will it last?</div>', unsafe_allow_html=True)

    cls_map = { "SAFE": "safe", "WARNING": "warning", "DANGER": "danger" }
    banner_class = cls_map.get(survival["risk"], "safe")
    badge_class = f"risk-{banner_class}"

    st.markdown(f"""
    <div class="survival-banner {banner_class}">
        <div class="survival-block">
            <div class="survival-label">Risk Level</div>
            <div><span class="risk-badge {badge_class}">{survival['risk']}</span></div>
        </div>
        <div class="survival-block" style="text-align: center;">
            <div class="survival-label">Days Remaining</div>
            <div class="survival-value" style="font-style: italic;">{survival['days_left']}</div>
        </div>
        <div class="survival-block" style="text-align: right;">
            <div class="survival-label">Gone by (if nothing changes)</div>
            <div class="survival-value" style="font-size: 2rem;">{survival['zero_date'].strftime('%d %b %Y')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # SECTION: CATEGORY CHART
    st.markdown('<div class="section-head">Where did it go?</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    cat_totals = debits.groupby("Category")[amt_col].sum().sort_values(ascending=True)

    c1, c2 = st.columns([1.2, 0.8])

    with c1:
        fig, ax = plt.subplots(figsize=(6, 4), facecolor="#FFFFFF")
        ax.set_facecolor("#FFFFFF")
        colors = [CATEGORY_PALETTE.get(c, "#f1faee") for c in cat_totals.index]
        bars = ax.barh(cat_totals.index, cat_totals.values, color=colors, height=0.6, edgecolor="none", zorder=3)
        
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x:,.0f}"))
        ax.tick_params(axis="x", labelsize=9, colors="#7A7A9A")
        ax.tick_params(axis="y", labelsize=10, colors="#1A1A2E")
        
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_color("#EBEBEB")
        
        ax.grid(axis='x', linestyle='--', alpha=0.5, color='#EBEBEB', zorder=0)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with c2:
        pct_df = pd.DataFrame({
            "Category": cat_totals.index[::-1],
            "Amount (₹)": cat_totals.values[::-1].round(0).astype(int),
            "% Share": (cat_totals.values[::-1] / cat_totals.sum() * 100).round(1)
        }).reset_index(drop=True)
        st.dataframe(pct_df, use_container_width=True, hide_index=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION: MANUAL TAGGING
    unknown = debits[debits["Category"] == "Unknown UPI / Needs Tagging"].copy()
    if not unknown.empty:
        st.markdown('<div class="section-head" style="margin-top: 2rem;">Help us sort these</div>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #7A7A9A; margin-bottom: 1.5rem;">We couldn\'t figure out what these were. Give them a label and we\'ll include them in your breakdown.</p>', unsafe_allow_html=True)
        
        tag_options = ["— Select —", "Food & Dining", "Shopping", "Transport", "Entertainment", "Essentials", "Subscriptions & Digital", "Other"]
        updated_cats = {}

        for idx, row in unknown.iterrows():
            st.markdown('<div class="card" style="padding: 1rem 1.5rem; margin-bottom: 0.8rem;">', unsafe_allow_html=True)
            t1, t2 = st.columns([3, 1])
            with t1:
                st.markdown(f"""
                <div style="font-size:1.05rem;font-weight:500;color:#1A1A2E;">{html.escape(str(row[desc_col]))}</div>
                <div style="font-family:'Fraunces', serif;font-weight:700;color:#1A1A2E;margin-top:0.2rem;">₹{row[amt_col]:,.0f}</div>
                """, unsafe_allow_html=True)
            with t2:
                chosen = st.selectbox("Category", tag_options, key=f"tag_{idx}", label_visibility="collapsed")
                if chosen != "— Select —":
                    updated_cats[idx] = chosen
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Update my spending", type="primary"):
            for idx, cat in updated_cats.items():
                st.session_state["debits"].at[idx, "Category"] = cat
            st.success("Nice. Your spending breakdown has been updated.")
            st.rerun()

    # SECTION: BEHAVIORAL INSIGHTS
    st.markdown('<div class="section-head" style="margin-top: 2.5rem;">Things we noticed</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    insights = behavioral_insights(debits, amt_col, date_col)
    for color, text in insights:
        dot_cls = color
        st.markdown(f"""
        <div class="insight-row">
          <div class="insight-dot {dot_cls}"></div>
          <div class="insight-text">{text}</div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # SECTION: SMART ADVISORY
    st.markdown('<div class="section-head" style="margin-top: 2.5rem;">What you can do</div>', unsafe_allow_html=True)
    advs = smart_advisory(survival, debits, amt_col)
    for adv in advs:
        st.markdown(f'<div class="advisory-item">{adv}</div>', unsafe_allow_html=True)

    # SECTION: FULL LOG EXPANDER
    st.markdown('<div style="margin-top: 3rem;"></div>', unsafe_allow_html=True)
    with st.expander("See everything"):
        log_df = debits[[date_col, desc_col, amt_col, "Category"]].copy()
        log_df.columns = ["Date", "Description", "Amount (₹)", "Category"]
        log_df["Date"] = log_df["Date"].dt.strftime("%d %b %Y")
        
        # Prevent CSV injection
        def sanitize_for_csv(val):
            val_str = str(val)
            if val_str.startswith(('=', '+', '-', '@')):
                return "'" + val_str
            return val_str
            
        log_df["Description"] = log_df["Description"].apply(sanitize_for_csv)
        st.dataframe(log_df, use_container_width=True, hide_index=True)

        csv = log_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Export as CSV",
            data=csv,
            file_name='thrive_statement.csv',
            mime='text/csv',
        )

else:
    # ── LANDING STATE ──────────────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-top: 4rem;">
      <div style="font-family: 'Fraunces', serif; font-size: 1.8rem; font-weight: 700; color: #1A1A2E; margin-bottom: 0.5rem;">How it works</div>
      <div class="landing-steps">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-title">Upload your bank statement CSV</div>
          <div class="step-desc">Simply drop your monthly statement into the upload box above.</div>
        </div>
        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-title">We categorise automatically</div>
          <div class="step-desc">Our engine neatly sorts out where everything is going.</div>
        </div>
        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-title">You see the real picture</div>
          <div class="step-desc">Know exactly where your money goes and how long it will last.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 2rem; max-width: 600px;">
      <a href="data:text/csv;charset=utf-8," download="sample_statement.csv" style="color: #5B4FCF; font-weight: 500; text-decoration: none; border-bottom: 1px dotted #5B4FCF;" onclick="event.preventDefault(); document.getElementById('hidden_download').click();">Download sample CSV to try it out</a>
    </div>
    """, unsafe_allow_html=True)
    st.download_button("hidden_dl", data=SAMPLE_CSV, file_name="sample_statement.csv", mime="text/csv", key="hidden_download_btn_internal_use_only")

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:3rem 0 1rem;color:#7A7A9A;font-size:0.8rem;margin-top:4rem;">
  Thrive · Built for students · All data is processed locally. Nothing is stored or shared.
</div>
""", unsafe_allow_html=True)

# CSS trick to hide the hidden download button since st.download_button places a physical element.
st.markdown("""
<style>
div:has(> button[kind="secondary"][aria-label="hidden_dl"]) {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(layout = "wide",page_title="Startup Analysis")
st.title("Startup Dashboard")


def load_investor_details(investor_name):
    st.title(investor_name,text_alignment="center")
    #load recent 5 investment of investor
    last5_df = (df[df["investor"].str.contains(investor_name, na=False)].sort_values("date", ascending=False).head(5)[["date", "startup", "vertical", "city", "round", "amount"]])
    st.subheader("Recent Investment")
    st.dataframe(last5_df)



    #biggest investments
    cols1, cols2 = st.columns(2)
    with cols1:
        big_series = df[df["investor"].str.contains(investor_name)].groupby("startup")["amount"].sum().sort_values(
            ascending=False).head(5)
        st.subheader("biggest investment")
        # bar chart
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)

        st.pyplot(fig)

    #genrally invested in

    with cols2:
        verical_series = df[df["investor"].str.contains(investor_name)].groupby("vertical")["amount"].sum()
        st.subheader("Sectors Invested In")
        # pie chart
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct= "%0.01f%%")
        st.pyplot(fig1)

    cols3, cols4 = st.columns(2)

    with cols3:
        verical_stage = df[df["investor"].str.contains(investor_name)].groupby("round")["amount"].sum()
        st.subheader("Investment Distribution by Funding Stage")
        # pie chart
        fig2, ax2 = plt.subplots()
        ax2.pie(verical_stage, labels=verical_stage.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    with cols4:
        verical_city = df[df["investor"].str.contains(investor_name)].groupby("city")["amount"].sum()
        st.subheader("Investment Distribution by City")
        # pie chart
        fig3, ax3 = plt.subplots()
        ax3.pie(verical_city, labels=verical_city.index, autopct="%0.01f%%")
        st.pyplot(fig3)


    cols5, cols6 = st.columns(2)

    with cols5:
        yoy = df[df["investor"].str.contains(investor_name)].groupby("year")["amount"].sum()
        st.subheader("Year on Year Investment")
        # line chart
        fig4, ax4 = plt.subplots()
        ax4.plot(yoy.index, yoy.values, marker="o")
        ax4.set_xticks(yoy.index)
        ax4.set_xlabel("Year")
        ax4.set_ylabel("Investment Amount")


        st.pyplot(fig4)

    with cols6:
        st.subheader("similar investors")
        top_vertical = (
            df[df["investor"].str.contains(investor_name, na=False)].groupby("vertical")["amount"].sum().sort_values(
                ascending=False).head(5).index)
        total_amount_spend = (df[df["investor"].str.contains(investor_name, na=False)].groupby("vertical")["amount"].sum()
            .sort_values(ascending=False).head(5).values.sum()
        )
        lower_range = total_amount_spend - 10
        upper_range = total_amount_spend + 10

        # Total investment by each investor in the same top 3 verticals
        investor_amount = (df[df["vertical"].isin(top_vertical)].groupby("investor")["amount"].sum())
        similar_investor = investor_amount[(investor_amount > lower_range) | (investor_amount < upper_range)]
        # Remove investor name himself
        similar_investors = similar_investor[~ similar_investor.index.str.contains(investor_name, na=False)]
        # Top 3 similar investors
        similar_investors = similar_investors.sort_values(ascending=False).head(5)
        st.dataframe(similar_investors)

def load_overall_analysis():
    st.write("welcome to overall analysis")
    #show total invested amount
    total = round(df["amount"].sum())

    # max amount infused in startup
    max_amt = df.groupby("startup")["amount"].max().sort_values(ascending = False).head(1).iloc[0]

    #mean of  investment in startups
    mean_amt_invested = round(df.groupby("startup")["amount"].sum().mean())
    #count of funded startups
    count_startups = df["startup"].nunique()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric("Total",str(total) + ' Cr')
    with col2:
        st.metric("Max", str(max_amt) + ' Cr')
    with col3:
        st.metric("Mean",str(mean_amt_invested)+ ' Cr')
    with col4:
        st.metric("Funded Startup", str(count_startups) )

    block1, block2, = st.columns(2)
    block3, block4 = st.columns(2)
    ##mom graph
    with block1:
        st.subheader("Mom Graph")
        option = st.selectbox("Select",["Total","count"])
        if option == "Total":
            temp = df.groupby(["year", "month"])["amount"].sum().reset_index()
        else:
            temp = df.groupby(["year", "month"])["amount"].count().reset_index()

        temp["x_axis"] = temp["month"].astype(str) + '-' + temp["year"].astype("str")
        fig1, ax1 = plt.subplots()
        ax1.plot(temp["x_axis"], temp["amount"])
        ax1.set_xticks(range(0, len(temp), 3))
        ax1.set_xticklabels(temp["x_axis"].iloc[::3], rotation=45)

        st.pyplot(fig1)

    with block2:
        st.subheader("TOP SECTOR ANALYSIS")
        option1 = st.selectbox("Select",['Count',"Sum"])
        #top sector sum of amount spent by investors
        if option1 == 'Sum':
            topsector = df.groupby("vertical")["amount"].sum().sort_values(ascending=False).head(5)
            fig2, ax2 = plt.subplots()
            ax2.pie(topsector, labels=topsector.index, autopct="%0.01f%%")
        #count of companies in each sector
        else:
            topsector = df.groupby("vertical")["startup"].nunique().sort_values(ascending = False).head(5)
            fig2, ax2 = plt.subplots()
            ax2.pie(topsector,labels=topsector.index,autopct=lambda pct: round(pct * total / 100))

        st.pyplot(fig2)
    with block3:
        #too funding types
        st.subheader("top funding types")
        top_fund =df.groupby("round")["amount"].sum().sort_values(ascending=False).head(5)
        fig3, ax3 = plt.subplots()
        ax3.bar(top_fund.index, top_fund.values)
        ax3.set_xlabel("Top funding rounds")
        ax3.set_ylabel("Investment Amount")

        st.pyplot(fig3)

    with block4:
        # funding amount by city
        st.subheader("funding amount by city")
        top_city = df.groupby("city")["amount"].sum().sort_values(ascending=False).head(5)
        fig4, ax4 = plt.subplots()
        ax4.barh(top_city.index, top_city.values)
        ax4.set_xlabel("funding amount")
        ax4.set_ylabel("city")

        st.pyplot(fig4)

    #top startup yearwise + overall
    st.subheader("Yearwise/Overall Top Startups")
    st1 = st.selectbox("Select",["Overall","Yearwise"] )
    if st1 == "Yearwise":
        # st.subheader("top startup yearwise")
        temp = df.groupby(["year", "startup"])["amount"].sum().reset_index()
        temp1 = temp.groupby("year")["amount"].idxmax()
        result = temp.loc[temp1]
    else:
        # st.subheader("top startup overall")
        result = df.groupby("startup")["amount"].sum().sort_values(ascending=False).head(5)
    st.dataframe(result)


    #top investors
    st.subheader("Top Investors")
    st.dataframe(df.groupby("investor")["amount"].sum().sort_values(ascending=False).head(5))

def load_startup_analysis(name) :
    st.header("Welcome to startup analysis")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6=st.columns(2)


    vertical_name = df[df["startup"].str.contains(name)]["vertical"].iloc[0]
    sub_vertical = df[df["startup"].str.contains(name)]["subvertical"].iloc[0]
    city = df[df["startup"].str.contains(name)]["city"].iloc[0]
    funding_rounds = df[df["startup"] == startup_name]["round"].count()

    with col1:
        st.metric("Startup Name", name)
    with col2:
        st.metric("Industry Name", vertical_name)
    with col3:
        st.metric("Sub-Vertical Name", sub_vertical)
    with col4:
        st.metric("Location Name", city)

    with col5:
        st.metric("Funding Rounds",funding_rounds)

    with col6:
        startup_year_funding = (df[df["startup"] == startup_name].groupby("year")["amount"].sum().sort_index())
        fig1, ax1 = plt.subplots()
        ax1.plot(startup_year_funding.index, startup_year_funding.values, marker="o")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Funding Amount")
        ax1.set_title(f"{startup_name} - Year-wise Funding Trend")

        st.pyplot(fig1)


##driver code starts
#reading the file
df = pd.read_csv("startup_cleaned.csv")
df["date"] = pd.to_datetime(df["date"],errors="coerce")
df['month'] = df["date"].dt.month



st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])




if option == "Overall Analysis":
    st.title("Overall Analysis")
    load_overall_analysis()
if option == "Startup":
    startup_name = st.sidebar.selectbox("Select StartUp",df["startup"].unique().tolist())
    btn1 = st.sidebar.button("Find Startup Details")
    st.title("Startup Analysis")
    if btn1 :
        load_startup_analysis(startup_name)
if option == "Investor":
    selected_investor = st.sidebar.selectbox("Select Investor",sorted(set(df["investor"].str.split(",").sum())))
    btn2 = st.sidebar.button("Find Investor Details")
    st.title("Investor Analysis",text_alignment="center")
    if btn2:
        load_investor_details(selected_investor)


import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")
st.title("Seaborn App")
st.write("This is a simple app to demonstrate Seaborn visualizations.")

def display_plot(plot_type):
    if plot_type == "Bar Plot":
        fig, ax = plt.subplots()
        sns.barplot(x="day", y="total_bill", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Box Plot":
        fig, ax = plt.subplots()
        sns.boxplot(x="day", y="total_bill", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Scatter Plot":
        fig, ax = plt.subplots()
        sns.scatterplot(x="total_bill", y="tip", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Histogram":
        fig, ax = plt.subplots()
        sns.histplot(tips["total_bill"], bins=30, kde=True, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Pair Plot":
        fig = sns.pairplot(tips)
        st.pyplot(fig)  
    elif plot_type == "Violin Plot":
        fig, ax = plt.subplots()
        sns.violinplot(x="day", y="total_bill", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Facet Grid":
        g = sns.FacetGrid(tips, col="time")
        g.map(sns.histplot, "total_bill")
        st.pyplot(g.fig)
    elif plot_type == "Joint Plot":
        fig = sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
        st.pyplot(fig)
    elif plot_type == "Count Plot":
        fig, ax = plt.subplots()
        sns.countplot(x="day", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Line Plot":
        fig, ax = plt.subplots()
        sns.lineplot(x="total_bill", y="tip", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Strip Plot": 
        fig, ax = plt.subplots()
        sns.stripplot(x="day", y="total_bill", data=tips, ax=ax)
        st.pyplot(fig)
    elif plot_type == "Heatmap":
        fig, ax = plt.subplots()
        corr =tips[['total_bill', 'tip','size']].corr()
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.write("Select a valid plot type.")
st.subheader("Select a plot type")
plot_type = st.selectbox("Choose a plot type", 
    ["Bar Plot", "Box Plot", "Scatter Plot", "Histogram", "Pair Plot", 
    "Heatmap", "Violin Plot", "Facet Grid", "Joint Plot", "Count Plot",
    "Line Plot", "Strip Plot"])
if st.button("Display Plot"):
    display_plot(plot_type) 


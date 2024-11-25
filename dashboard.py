import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Customizing the Streamlit:
st.markdown(
    """
    <style>
    .custom-link a {
        color: #CB99C9;
        text-decoration: none;
    }
    .custom-link a:hover {
        color: purple;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("2024 AHI - HHA 507 Streamlit Dashboard Assignment")

## Custom link to my GitHub Repository: (Streamlit doesn't offer a way to customize the link color so I did some research to make it work)
st.markdown('<div class="custom-link"><a href="https://github.com/raqssoriano/streamlit-dashboard-enhanced" target="_blank">👩🏻‍💻 Visit my GitHub Repository: github.com/raqssoriano</a></div>', unsafe_allow_html=True)

st.header("*School Learning Modalities, 2020-2021*")

# loading the data:
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") 

## data cleaning (recode week to datetime and zip code to string):
df['week_df'] = pd.to_datetime(df['week'], errors='coerce')
df = df.dropna(subset=['week_df'])
df['zip_code'] = df['zip_code'].astype(str)

## To display the available rows and columns of the original data:
st.subheader("The Original Data Overview:")
st.page_link("https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data", label="For more information, visit the data source link: HealthData.gov - School Learning Modalities 2020-2021", icon="🌎")
st.text("The dashboard provides weekly estimates of school learning modalities (in-person, remote, or hybrid) for U.S. K-12 public and independent charter school districts during the 2020-2021 school year (Aug 2020-June 2021).")

col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Unique Districts/Schools:", df['district_name'].nunique())

## Display the first 1k of NCES 20-21 data:
#st.dataframe(df)

## Calculate total learning modality:
total_modality = df.groupby('learning_modality')['student_count'].sum().reset_index()
total_modality = total_modality.sort_values('student_count', ascending=False)

# Ensure the DataFrame includes all required columns
df['week'] = df['week']
df['operational_schools'] = df['operational_schools']
df['district_name'] = df['district_name']
df['city'] = df['city']
df['state'] = df['state']

# Filter the DataFrame to include only the specified columns
filtered_df = df[['week', 'learning_modality', 'student_count', 'district_name', 'city', 'state', 'operational_schools']]

# To display the filtered DataFrame
st.header("Modified Dashboard:")
st.text("The table below shows the modified dataframe with selected columns (Learning Modalities, Number of Students, Week, Operational Schools, City, and State).")
st.dataframe(filtered_df)

# calculate percentages of students in each learning modality:
total_students = total_modality['student_count'].sum()
total_modality['percentage'] = (total_modality['student_count'] / total_students) * 100

# filter data to exclude 'unknown' learning modality:
filter_df = df[df['learning_modality'] != 'unknown']

# Group data and Count operational schools by learning modality:
grouped_data = filter_df.groupby(['state', 'learning_modality'])['operational_schools'].sum().reset_index()

# Convert the 'week' column to datetime format:
df['week_df'] = pd.to_datetime(df['week_df'])

# Create a combined column for state and city:
df['city_state'] = df['state'] + " - " + df['city']

# min and max dates for the date input widget:
min_date = df['week_df'].min().date()
max_date = df['week_df'].max().date()

## Widget (1) - Sidebar for filtering data and customizing the dashboard:
st.sidebar.write("# Use this Sidebar to Modify Display Options")
st.sidebar.write("### *Feel free to filter or adjust the data based on your preferences.*")

## Widget (2) - Date input for selecting a week range:
st.sidebar.header("☞ Select Week Range")
start_date, end_date = st.sidebar.date_input("Set the week range below", value=(min_date, max_date), min_value=min_date, max_value=max_date)

## Widget (3) - Radio buttons for selecting learning modality:
#st.sidebar.header("Select Learning Modality - Radio Button")
#select_learning_modality = st.sidebar.radio("Learning Modality Option", options=df['learning_modality'].unique(), key="learning_modality")

## Widget (3) - Multiselect for selecting learning modality:
st.sidebar.header("☞ Select Learning Modality")
selected_modality = st.sidebar.multiselect("Select all the learning modalities you want to display or choose them individually.", options=df['learning_modality'].unique(), default=df['learning_modality'].unique(), key="selected_modality")

## Widget (4) - Checkbox for selecting a state:
st.sidebar.header("☞ Select State(s)")
selected_states = []
for state in df['state'].unique():
    if st.sidebar.checkbox(state, key=f"state_{state}"):
        selected_states.append(state)

## Widget (5) - Text input for entering a custom filter:
st.sidebar.header("☞ Custom Filter")
custom_filter = st.sidebar.text_input("Apply Custom Filter in this field:", key="custom_filter")

## Visualization (1) - Pie chart showing the percentage breakdown of school learning modalities:
st.subheader("Total Percentage of Students in Each Learning Modality")
st.text("The pie chart below shows the percentage of students in each learning modality. You may hover over the data points to see more information, such as the number of students in each learning modality.") 

st.write("#### *Important Note:*")
st.write("The pie chart shows how students are spread across different learning modalities. It helps dashboard app users see the proportion of students in each type and highlights the main modes of learning during the given period.")


pastel_colors = px.colors.qualitative.Pastel
pie_chart = px.pie(grouped_data, names='learning_modality', values='student_count', title='Percentage of Students in each Learning Modality', color_discrete_sequence=pastel_colors)
pie_chart.update_traces(textposition='inside', textinfo='percent+label', texttemplate='%{label} (%{percent})<br>%{value:,.0f} students')
st.plotly_chart(pie_chart)


## Visualization (2) - Bar chart showing the number of students in each learning modality:
st.subheader("Total Number of Students in Each Learning Modality")

st.write("#### *Important Note:*")
st.write("The bar chart displays the number of students in each learning modality, making it easy to compare and see which ones are most and least common. You may hover over the data points to see more information.")

bar_chart = px.bar(total_modality, x='learning_modality', y='student_count', title='Student Count and Learning Modality', color='learning_modality', color_discrete_sequence=pastel_colors, labels={'learning_modality': 'Learning Modality', 'student_count': 'Number of Students'}, text='student_count')
bar_chart.update_traces(texttemplate='%{text:,.0f}', textposition='inside')
bar_chart.update_layout(showlegend=False)
st.plotly_chart(bar_chart)

## Visualization (3) - Bar chart showing the number of students in each learning modality AND state:
st.subheader("Total Number of Students in Each Learning Modality by State")

st.write("#### *Important Note:*")
st.write("The grouped bar chart below shows the number of students in each learning modality by state. It lets dashboard app users compare how different states distribute learning modalities, highlighting regional differences and trends. ou may hover over the data points to see more information.")

bar_grouped = px.bar(df, title='Learning Modality and State', x='state', y='student_count', color='learning_modality', barmode='group', labels={'student_count': 'Number of Students', 'learning_modality': 'Learning Modality'}, color_discrete_sequence=pastel_colors, category_orders={'state': sorted(df['state'].unique()), 'learning_modality': sorted(df['learning_modality'].unique())})
bar_grouped.update_layout(title_x=0.9, xaxis_title='State', yaxis_title='Number of Students', legend_title='Learning Modality', width=1000, height=700)
st.plotly_chart(bar_grouped)


# filter data based on selected states and date range:
start_datetime = pd.to_datetime(start_date)
end_datetime = pd.to_datetime(end_date)
filter_df = df[(df['week_df'] >= start_datetime) & (df['week_df'] <= end_datetime)]


# define a function to group data by learning modality:
modalities = filter_df['learning_modality'].unique()
line_chart2 = go.Figure()

# colors for the line chart (to match the other charts I created)
pastel_colors = px.colors.qualitative.Pastel

for i, modality in enumerate(modalities):
    modality_data = filter_df[filter_df['learning_modality'] == modality]
    line_chart2.add_trace(go.Scatter(x=modality_data['week_df'], y=modality_data['student_count'], mode='lines+markers', name=modality, line=dict(color=pastel_colors[i % len(pastel_colors)])))

## Visualization (4) - Line chart of learning modalities over time:
## update the line chart layout:
st.subheader("Weekly Trends in Student Learning Modalities")

st.write("#### *Important Note:*")
st.write("The line chart below displays the weekly trends in student learning modalities over time. It reveals how the distribution of modalities changed each week, helping dashboard app users identify patterns, peaks, and shifts in learning modes during the specificied period. You may hover over the data points to see more information.")

line_chart2.update_layout(title='Student Count Over Time by Learning Modality (Weekly)', xaxis_title='Week', yaxis_title='Number of Students', legend_title='Learning Modality', template='plotly_white')
st.plotly_chart(line_chart2)

# Group data and Count operational schools by learning modality:
grouped_data = filter_df.groupby(['state', 'learning_modality'])['operational_schools'].sum().reset_index()


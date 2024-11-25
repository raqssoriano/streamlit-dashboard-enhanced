---
# **HHA507 || Dashboards with Streamlit**
---
---

#### **🎯** In this assignment, I am learning how to [enhance a Streamlit dashboard](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/) by [updating and modifying example code](https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboard.py) from an [existing repository](https://github.com/raqssoriano/streamlit-dashboard-enhanced/tree/main). This project allowed me to gain hands-on experience with Streamlit by [creating visualizations, adding text, and integrating interactive components](https://github.com/raqssoriano/streamlit-dashboard-enhanced/tree/main#-dashboard-enhancements-and-interactive-visualizations).

#### **🔗** Link to my newly modified Streamlit Dashboard: [**https://app-dashboard-enhanced-hha507-sch-learning-modalities-2021-2022.streamlit.app/**](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/)
---

## ☞ *Data Overview*

#### The dashboard provides weekly estimates of school learning modalities (in-person, remote, or hybrid) for U.S. K-12 public and independent charter school districts during the 2020-2021 school year (Aug 2020-June 2021) based on data from the [National Center for Educational Statistics (NCES)](https://nces.ed.gov/ccd/files.asp#Fiscal:2,LevelId:5,SchoolYearId:35,Page:1).

#### Learning Modality Types:
- _**In-Person**_: All schools within the district offer face-to-face instruction 5 days per week to all students at all available grade levels.
- _**Remote**_: Schools within the district do not offer face-to-face instruction; all learning is conducted online/remotely to all students at all available grade levels.
- _**Hybrid**_: Schools within the district offer a combination of in-person and remote learning; face-to-face instruction is offered less than 5 days per week, or only to a subset of students.

##### • For further information and a link to the data used: [HealthData.gov - School Learning Modalities 2020-2021](https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data)

##### • Courtesy of Professor Hants Williams' GitHub Repository: [streamlit-dashboard-enhanced](https://github.com/hantswilliams/507-streamlit-demo)

##### • Other links used to perform the data visualizations/widgets: A combination of [Streamlit Documentation](https://docs.streamlit.io/) and **`GitHub Copilot`** within **`Visual Studio Code`**, which I modified to make it more personalized. Also, I watched several **YouTube videos** to complete the visualizations/widgets section.

---
---

## ☞ _**Dashboard Enhancements and Interactive Visualizations**_

### ➤ Data Visualizations Overview:

1. Total Percentage of Students in Each Learning Modality
    - [**`Pie Chart`**](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/~/+/#total-percentage-of-students-in-each-learning-modality): It shows the percentage in each learning modality.
    - **`Importance`**: It helps in understanding the proportion of students in each type and highlights the main modes of learning during the given period.
      
      <img src="https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboards/1%20-%20pie%20chart.png" width="550" />

2. Total Number of Students in Each Learning Modality
    - [**`Bar Chart`**](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/~/+/#total-number-of-students-in-each-learning-modality): It displays the number of students in each learning modality.
    - **`Importance`**: Makes it easy to compare which modalities are most and least common.
      
      <img src="https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboards/2%20-%20bar%20chart.png" width="550" />

3. Total Number of Students in Each Learning Modality by State
    - [**`Grouped Bar Chart`**](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/~/+/#total-number-of-students-in-each-learning-modality-by-state): It shows the number of students in each learning modality by state.
    - **`Importance`**: It allows for the comparison of the distribution of learning modalities across different states, highlighting regional differences and trends.
      
      <img src="https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboards/3%20-%20grouped%20bar%20chart.png" width="600" />

4. Weekly Trends in Student Learning Modalities
    - [**`Line Chart`**](https://app-dashboard-enhanced-hha507-sch-learning-modalities-2020-2021.streamlit.app/~/+/#weekly-trends-in-student-learning-modalities): It displays the weekly trends in student learning modalities over time, showing how the distribution changed each week.
    - **`Importance`**: It helps identify patterns, peaks, and shifts in learning modes during the specificied period.
      
      <img src="https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboards/4%20-%20line%20chart.png" width="600" />

### ➤ Sidebar Widgets:

   - It provides innovative features for filtering and customizing data analysis. Dashboard app users can select week (date) ranges, learning modalities, states, and custom filters, allowing for a more detailed and personalized analysis of the dataset. This flexibility can significantly influence our decision-making based on the data, if necessary.
     
     <img src="https://github.com/raqssoriano/streamlit-dashboard-enhanced/blob/main/dashboards/5%20-%20widgets.png" width="600" />






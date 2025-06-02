## Blue Bike Data Analysis with Azure


---

## ⚙️ Tools & Technologies

- **Azure Blob Storage** – Data lake architecture (Bronze → Silver → Gold)
- **Azure Data Factory** – Pipeline to clean and transform ride data
- **Databricks (PySpark)** – Advanced transformations & weather data integration
- **Power BI** – Visualization dashboard
- **Python** – Scripting for fetching and cleaning weather data

---

## 🧠 Objectives

- Combine Bluebikes usage data with weather parameters
- Analyze patterns across time, station usage, and weather
- Build a scalable data pipeline using cloud technologies
- Visualize key insights using Power BI

---

## 🔄 Data Flow Overview

![Data Flow]("https://github.com/GandharvaTatkare/BlueBikesProject/blob/5aab7c46e19d4177cae00ea0c8596fa1d629cb86/data_flow.png")

1. **Raw Files Zipped & Merged** (locally)
2. **Uploaded to Azure Blob (Bronze)**
3. **Azure Data Factory** – Clean & transform data into Silver layer
4. **Databricks (PySpark)** – Further transformation and weather join → stored in Gold layer
5. **Power BI** connects to the Gold layer for dashboards

---


## 📬 Contact

**Gandharva Sudhir Tatkare**  
[LinkedIn](https://www.linkedin.com/in/gandharva-tatkare/)  
Email: [tatakare.gandharva@gmail.com]



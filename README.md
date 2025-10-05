🧠 Customer Segmentation Dashboard

A Machine Learning–powered web dashboard built with Flask, Python, and Chart.js that helps businesses analyze and segment their customers based on uploaded datasets.
It automatically clusters customers into groups using K-Means Clustering and visualizes results interactively.

🚀 Features

📁 Upload any CSV dataset (e.g., customer data with age, income, spending score, etc.)

🤖 Perform automatic customer segmentation using K-Means

📊 View interactive charts and cluster summaries

📄 Preview and download segmented data

🎨 Modern, responsive UI with sidebar navigation

💾 Built entirely with Flask + Bootstrap + Chart.js

🧰 Tech Stack
Component	Technology
Backend	Flask (Python)
Frontend	HTML, CSS, Bootstrap 5
Charts	Chart.js
Machine Learning	Scikit-learn (KMeans)
Data Handling	Pandas, NumPy




▶️ Run the Application
python app.p

🧩 Folder Structure
customer-segmentation-dashboard/
│
├── app.py                   # Main Flask backend
├── templates/
│   └── index.html            # Dashboard UI (Jinja2 template)
├── static/                   # (Optional) CSS/JS files if separated
├── uploads/                  # Temporary uploaded files
├── segmented_data/           # Saved segmented outputs
└── requirements.txt          # Python dependencies

📈 How It Works

Upload a .csv dataset

Choose number of clusters (default = 4)

Flask processes data using KMeans

Clustered results are displayed with counts and a Chart.js doughnut chart

Download the full segmented dataset as CSV

💡 Example Use Case
CustomerID	Age	Annual Income	Spending Score
1	19	15000	39
2	35	45000	81
3	27	57000	6
...	...	...	...

→ App will cluster these customers into groups like:

🟢 High Income - High Spend

🔵 Low Income - Low Spend

🟣 Young Budget Spenders, etc.

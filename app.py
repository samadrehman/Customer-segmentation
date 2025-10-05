from flask import Flask, render_template, request, send_file, url_for
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import io

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html", tables=None)

# Segmentation route
@app.route("/segment", methods=["POST"])
def segment():
    try:
        # 🧩 1. Validate file input
        file = request.files.get("file")
        if not file:
            return render_template("index.html", tables=None, error="⚠️ Please upload a CSV file.")

        # 🧠 2. Read CSV safely
        df = pd.read_csv(file, encoding="latin1").dropna()
        if df.empty:
            return render_template("index.html", tables=None, error="⚠️ Uploaded CSV is empty or invalid.")

        # 🔢 3. Select only numeric columns
        num_df = df.select_dtypes(include="number")
        if num_df.empty:
            return render_template("index.html", tables=None, error="❌ No numeric columns found in your CSV.")

        # ⚙️ 4. Get number of clusters safely
        cluster_input = request.form.get("clusters", "").strip()
        k = int(cluster_input) if cluster_input.isdigit() and int(cluster_input) > 0 else 4

        # 🧮 5. Auto-adjust cluster count if data is small
        if len(num_df) < k:
            k = len(num_df)
            notice = f"⚠️ Only {len(num_df)} data points available — adjusted cluster count to {k}."
        else:
            notice = None

        # 📊 6. Scale data for better clustering
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(num_df)

        # 🤖 7. Run KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(scaled_data)

        # 📈 8. Count members per cluster
        counts = df["Cluster"].value_counts().sort_index().to_dict()

        # 💾 9. Save output to memory for download
        output = io.BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)

        global segmented_file
        segmented_file = output

        # ✅ 10. Return response to frontend
        return render_template(
            "index.html",
            tables=[df.head().to_html(classes="table table-bordered table-striped text-center", index=False)],
            download_link=url_for("download"),
            counts=counts,
            notice=notice
        )

    except Exception as e:
        return render_template("index.html", tables=None, error=f"❌ Error: {str(e)}")

# Download segmented CSV
@app.route("/download")
def download():
    global segmented_file
    return send_file(segmented_file, as_attachment=True, download_name="segmented_customers.csv")

if __name__ == "__main__":
    app.run(debug=True)

# 🤔 WhatTheData

**Stop staring at spreadsheets. Start understanding them.**

Ever opened a CSV and thought... *"what the data is going on here?"* 

WhatTheData is a dead-simple tool that tells you everything you need to know about your dataset in seconds. Upload a CSV, get instant insights. No PhD required.

---

## ✨ What it does

Drop in any CSV and instantly see:

- 📊 **Shape & Size:**    How big is this thing anyway?
- 🕳️ **Missing Values:**  Where are the gaps?
- 📈 **Distributions:**   What do your numbers actually look like?
- 🔗 **Correlations:**    Which columns are secretly related?
- 🚨 **Outliers:**        Spot the weird stuff automatically
- 🏷️ **Data Types:**      Numbers, text, dates... sorted

---

## 🚀 Try it live

👉 [**Launch WhatTheData**](https://your-app-url-here.streamlit.app)

---

## 🛠️ Run it yourself

```bash
# Clone the repo
git clone https://github.com/zertidana/whatthedata.git
cd whatthedata

# Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch
streamlit run app.py
```

Then open `http://localhost:8501` and start profiling!

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | The engine |
| Streamlit | The interface |
| Pandas | The data wrangling |
| Plotly | The pretty charts |
| ydata-profiling | The deep dives |

---

## 🗺️ Roadmap

- [x] Basic data profiling
- [x] Distribution visualisations
- [x] Correlation matrix
- [x] Outlier detection
- [ ] Export reports as PDF
- [ ] Support for Excel files
- [ ] Column-level recommendations
- [ ] Dark mode 🌙

---

## 🤝 Contributing

Found a bug? Got an idea? PRs and issues are welcome!

1. Fork it
2. Create your branch (`git checkout -b feature/cool-thing`)
3. Commit (`git commit -m 'Add cool thing'`)
4. Push (`git push origin feature/cool-thing`)
5. Open a PR

---

## 📄 License

MIT — do whatever you want with it.

---

## 👋 About

Built by [Dana Zerti](https://github.com/zertidana) as part of a data portfolio project.

If this helped you, give it a ⭐ — it makes my day!

---

<p align="center">
  <i>Because every dataset deserves a proper introduction.</i>
</p>

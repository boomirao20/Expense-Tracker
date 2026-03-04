# 💰 AI Expense Tracker

<div align="center">

A modern, intelligent expense tracking application that transforms how you manage your finances with stunning visualizations and AI-powered predictions.

[![Streamlit](https://img.shields.io/badge/Streamlit-Expense%20Tracker-brightgreen?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

</div>

---

## 🌟 Why Choose AI Expense Tracker?

<div align="center">

*Track smarter, not harder. Your financial journey, beautifully simplified.*

</div>

<br>

## ✨ Features

<div align="center">

| 📊 Dashboard | 📈 Analytics | ➕ Management | 🎨 Experience |
|--------------|--------------|---------------|---------------|
| Real-time KPIs | AI Predictions | Easy Entry | Dark/Light Mode |
| Date Filtering | Beautiful Charts | Quick Delete | Responsive Design |
| Data Export | Trend Analysis | Category Management | Modern UI |

</div>

---

### 🚀 **Core Capabilities**

#### 📊 **Smart Dashboard**
- 🎯 **Real-time Metrics**: Live KPI cards showing total spending, average expense, and entry count
- 📅 **Date Range Filtering**: Focus on specific time periods with intuitive date pickers
- 📋 **Interactive Tables**: Sortable, searchable expense history with full details
- 💾 **Export Options**: Download your data in CSV or Excel formats with one click
- 💼 **Monthly Budget Tracker**: Set budget limits and track spending with alerts
- 🗑️ **Easy Deletion**: Remove expenses with simple ID-based deletion

#### 📈 **Advanced Analytics**
- 🥧 **Category Distribution**: Beautiful donut charts showing where your money goes
- 📊 **Spending Comparison**: Interactive colored bar charts for category-wise analysis
- 📈 **Trend Analysis**: Monthly expense patterns with smooth line charts
- 🤖 **AI Predictions**: Machine learning forecasts for next month's expenses
- 🧠 **AI Spending Insights**: Intelligent analysis of your spending patterns with recommendations

#### ➕ **Effortless Management**
- ⚡ **Quick Entry**: Add expenses in seconds with intuitive forms
- 🏷️ **Smart Categories**: Pre-defined categories (Food, Travel, Shopping, Bills, Other)
- 🗑️ **Easy Deletion**: Remove expenses with simple ID-based deletion
- 📱 **Mobile Friendly**: Works perfectly on all device sizes

#### 🎨 **Premium Experience**
- 🌓 **Theme Switching**: Toggle between elegant dark and light modes
- ✨ **Modern Design**: Clean, professional interface with smooth animations
- 🔄 **Real-time Updates**: Instant feedback on all your actions
- 🎯 **User-Friendly**: Intuitive navigation and clear visual hierarchy

## 🚀 Quick Start

<div align="center">

### 📋 Prerequisites
- Python 3.8 or higher
- pip package manager

</div>

---

### 🛠️ Installation Guide

<div align="center">

```bash
# Step 1: Clone the repository
git clone <repository-url>
cd expense-tracker

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run the application
streamlit run app.py
```

</div>

---

### 🌐 Launch

<div align="center">

🚀 **Open your browser and navigate to:** `http://localhost:8501`

✨ *Your expense tracking journey begins here!*

</div>

## 📦 Dependencies

<div align="center">

| 📦 Package | 🎯 Purpose | ⚡ Power |
|------------|------------|----------|
| `streamlit` | Web Framework & UI | 🚀 Fast & Interactive |
| `pandas` | Data Manipulation | 📊 Powerful Analytics |
| `plotly` | Interactive Visualizations | 📈 Stunning Charts |
| `scikit-learn` | Machine Learning | 🤖 AI Predictions |
| `numpy` | Numerical Operations | ⚡ Lightning Fast |
| `openpyxl` | Excel Support | 📄 Office Integration |

</div>

---

## 🗂️ Project Structure

<div align="center">

```
expense-tracker/
├── 📄 app.py              # Main application file
├── 🗄️ database.db         # SQLite database (auto-created)
├── 📋 requirements.txt    # Python dependencies
├── 📖 README.md          # This beautiful file
├── 🚫 .gitignore         # Git ignore rules
└── 📁 venv/              # Virtual environment
```

</div>

## 💾 Database Schema

<div align="center">

🗄️ **Simple & Efficient SQLite Structure**

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL
);
```

</div>

---

## 🎯 Usage Guide

<div align="center">

### 📝 Adding Expenses
1. 🎯 Navigate to **"Add Expense"** from the sidebar
2. 📅 Select date, choose category, enter amount
3. ✅ Click **"Add Expense"** to save

### 📊 Viewing Dashboard
1. 📈 Go to **"Dashboard"** section
2. 📅 Use date filters for specific periods
3. 🎯 View KPI cards and expense table
4. 💾 Download reports in CSV or Excel format
5. 💼 Set and track your monthly budget
6. 🗑️ Delete expenses using ID-based removal

### 📈 Analytics & Insights
1. 🔍 Explore **"Analytics"** section
2. 🥧 View category distribution donut charts
3. 📊 Analyze monthly spending trends with colored bar charts
4. 🤖 Check AI predictions for next month
5. 🧠 Get AI spending insights and recommendations

### 🗂️ Managing Data
- 🗑️ Delete expenses using ID in Dashboard
- 📤 Export data for external analysis
- 📅 Filter by date ranges for focused insights

</div>

## 🔧 Technical Details

<div align="center">

### 🏗️ Architecture Overview

| 🎨 Frontend | ⚙️ Backend | 🤖 ML Model | 📊 Visualization |
|-------------|------------|-------------|------------------|
| Streamlit | Python + SQLite | Linear Regression | Plotly Charts |

</div>

---

### 🚀 Key Features Implementation

<div align="center">

| ✨ Feature | 🛠️ Technology | 🎯 Purpose |
|-----------|---------------|------------|
| 🌓 Theme System | Custom CSS | Dark/Light Mode Toggle |
| 💾 Data Export | BytesIO | In-memory File Generation |
| 🤖 ML Integration | scikit-learn | Predictive Analytics |
| 📱 Responsive Design | Streamlit Components | Cross-device Compatibility |

</div>

---

## 🤖 AI Prediction Feature

<div align="center">

🧠 **Intelligent Expense Forecasting & Insights**

The application uses Linear Regression to predict next month's expenses and provides intelligent spending insights:

- 📊 **Training Data**: Monthly aggregated expense history
- 🔮 **Prediction**: Forecast for upcoming month using Linear Regression
- 💡 **Spending Insights**: AI-powered analysis of your top spending category
- ⚠️ **Smart Recommendations**: Alerts when you overspend on specific categories
- 📈 **Pattern Recognition**: Identifies spending patterns and provides actionable insights
- ⚡ **Technology**: scikit-learn Linear Regression model with intelligent analysis

</div>

---

## 🎨 Customization

<div align="center">

### 🏷️ Adding New Categories

```python
# Edit app.py - line 132
category = col2.selectbox(
    "Category",
    ["Food","Travel","Shopping","Bills","Other","Your New Category"]
)
```

### 🎨 Theme Customization

Modify the CSS sections in `app.py` to customize colors and styling for your brand.

</div>

## 🐛 Troubleshooting

<div align="center">

### 🔧 Common Issues & Solutions

| ⚠️ Issue | ✅ Solution | 💡 Tip |
|----------|------------|-------|
| 🗄️ Database not found | Auto-created on first run | Ensure write permissions |
| 📦 Dependencies missing | Re-run `pip install -r requirements.txt` | Check virtual environment |
| 🌐 Port already in use | Streamlit finds available port | Check console output |
| 🐍 Python version error | Use Python 3.8+ | Check with `python --version` |

</div>

---

## 🤝 Contributing

<div align="center">

🚀 **We Welcome Contributions!**

1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

</div>

---

## 📄 License

<div align="center">

📜 **MIT License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</div>

---

<div align="center">

## 🎉 Made with ❤️ using Streamlit

*Track your expenses, visualize your spending, predict your future!*

---

⭐ **If you like this project, give it a star!** ⭐

</div>

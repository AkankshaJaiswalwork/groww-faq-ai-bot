# 📈 Groww Mutual Fund AI Bot

A beautifully-designed, high-performance Streamlit dashboard mimicking the official Groww design system, combined with an intelligent financial advisor bot powered by the **Groq Llama-3** model and **LangChain**.

---

## ✨ Features

- 🎨 **Groww Design Aesthetic:** Custom styled header, navigation elements, metrics, risk tags, and cards matching Groww's white/green brand identity.
- 📉 **Interactive Dashboard:** Switch between different mutual funds (Nippon India, HDFC, Quant) and visualize interactive price charts (NAV).
- 💬 **In-Process AI Advisor:** A responsive chat advisor that answers questions about fund details (NAV, expense ratio, AUM), holdings, and fund managers based on real, scraped data.
- ⚡ **Direct Integration:** Consolidated code structure with the LLM pipeline running inside Streamlit using `@st.cache_resource` for maximum speed and simplicity. No external FastAPI service needed!

---

## 📁 Repository Structure

```
Groww FAQ ai bot/
├── .streamlit/
│   └── config.toml          # Custom theme configuration (Groww green styling)
├── data/
│   ├── hdfc-mid-cap-opportunities-fund-direct-growth_structured.json
│   ├── nippon-india-small-cap-fund-direct-growth_structured.json
│   └── quant-small-cap-fund-direct-plan-growth_structured.json
├── .env                     # Local environment file containing GROQ_API_KEY
├── .gitignore               # Clean git exclusion rules
├── app.py                   # Main Streamlit application
├── qa_pipeline.py           # LangChain Groq QA pipeline
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## 🚀 Local Setup & Hosting

Follow these simple steps to run the application on your local machine:

1. **Activate the Environment:**
   If you have a virtual environment in the project directory, activate it:
   ```bash
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   Ensure all packages are up-to-date:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**
   Create a `.env` file in the root folder and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Launch the Application:**
   Run the Streamlit server locally:
   ```bash
   streamlit run app.py
   ```
   The dashboard will automatically open in your default browser at `http://localhost:8501`.

---

## ☁️ Deployment to Streamlit Cloud

Because we consolidated the application and integrated the AI pipeline directly into Streamlit (removing the need for a separate FastAPI backend server), deploying it on **Streamlit Community Cloud** is incredibly straightforward:

### Step 1: Create a GitHub Repository
1. Log in to your GitHub account and create a new repository (e.g., `groww-faq-ai-bot`).
2. Do **NOT** add a README, LICENSE, or `.gitignore` (as they are already present in your local codebase).

### Step 2: Push your Local Code to GitHub
Open your terminal in the project directory and run:
```bash
# Link your local repository to your GitHub repo
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/groww-faq-ai-bot.git

# Rename main branch to main (if not already)
git branch -M main

# Push the code
git push -u origin main
```

### Step 3: Deploy on Streamlit Community Cloud
1. Visit [Streamlit Share](https://share.streamlit.io/) and log in with your GitHub account.
2. Click the **"New app"** button.
3. Select your repository (`groww-faq-ai-bot`), branch (`main`), and set the main file path to `app.py`.
4. Click **"Deploy!"**.

### Step 4: Configure the Secrets (Groq API Key)
Since the `.env` file containing your `GROQ_API_KEY` is excluded from git for security (via `.gitignore`), you must provide it to your Streamlit Cloud app:
1. In your Streamlit Cloud console, open your app's dashboard.
2. Click on **Settings** -> **Secrets**.
3. Add your Groq API key in the following format:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_groq_key_here"
   ```
4. Click **Save**. Your app will automatically restart and run with the live API key!

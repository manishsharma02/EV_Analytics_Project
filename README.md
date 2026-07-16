# ⚡ EV Analytics using Tableau & Flask
### Electric Vehicle Data Analysis — India & Global Market

> A centralized EV Analytics platform that combines Global and 
> India-specific Electric Vehicle data into one interactive platform 
> with Tableau dashboards embedded in a Flask web application.

**Status:** Completed | **Database:** SQLite | 
**Visualization:** Tableau Public | **Web:** Flask

---

## 📋 Table of Contents

1. [Introduction](#1-introduction)
2. [Ideation Phase](#2-ideation-phase)
3. [Requirement Analysis](#3-requirement-analysis)
4. [Project Design Phase](#4-project-design-phase)
5. [Project Planning Phase](#5-project-planning-phase)
6. [Project Development Phase](#6-project-development-phase)
7. [Performance Testing](#7-performance-testing)
8. [Project Documentation](#8-project-documentation)
9. [Repository Structure](#9-repository-structure)
10. [Getting Started Locally](#10-getting-started-locally)
11. [Tableau Public Links](#11-tableau-public-links)
12. [Conclusion](#12-conclusion)
13. [Summary](#13-summary)

---

## 1. Introduction

Electric Vehicles are the future of transportation, but people 
planning to buy an EV in India face a major challenge — EV data 
(specs, prices, charging stations, efficiency) is scattered across 
multiple websites with no single platform to compare everything 
visually.

**EV Analytics** solves this problem. It is a complete data analytics 
platform that:

- Collects real EV data from 4 publicly available datasets
- Cleans and stores 1,03,665 rows in a structured SQLite database
- Visualizes insights through 18 interactive Tableau charts
- Presents a guided story of EV trends in India (4 scenes)
- Makes everything accessible through a custom Flask website 
  (E-CarStart) without needing Tableau software

This README covers all 7 project phases documented in this 
repository's numbered folders and provides setup instructions for 
running the project locally.

---

## 2. Ideation Phase

*(Folder: 01_Dataset/)*

| Document | Summary |
|----------|---------|
| Problem Statement | Two customer problem statements were defined: PS-1 — an EV buyer in India who cannot find a single platform to compare brands, prices, and charging stations; PS-2 — a data analyst who wants to study global EV efficiency trends but finds raw datasets hard to interpret. Both statements highlight confusion and information overload as the core pain points. |
| Empathy Map | Frames the target EV buyer's experience across four lenses — Think & Feel, Hear, See, Say & Do — to keep the solution user-centric rather than data-centric. Pain: scattered information, no single trusted source. Gain: clear visual comparison, confident purchase decision. |
| Brainstorming | Team generated ideas including a single dashboard combining specs and charging stations, interactive India map, brand-wise filters, and a Flask web platform. Ideas were prioritized on an Importance vs Feasibility grid — single dashboard, filters, and web integration were rated High importance + High feasibility. |

Key takeaway: the project was validated around three pillars — 
centralized EV data, interactive visual comparison, and public 
web accessibility.

---

## 3. Requirement Analysis

*(Folder: 05_Documentation/)*

| Document | Summary |
|----------|---------|
| Customer Journey Map | Maps the EV buyer's journey across 5 stages: Awareness → Research → Comparison → Decision → Post-Purchase. Captures steps, interactions, goals, positive/negative moments, and areas of opportunity at each stage. |
| Data Flow Diagram | Defines the data flow: CSV Datasets → Python Cleaning → SQLite Database → Tableau Dashboards → Tableau Public → Flask Web App → End User. |
| Solution Requirements | Lists 4 Functional Requirements (Data Collection, Visualization, Dashboard & Filters, Web Integration) and 6 Non-Functional Requirements (Usability, Security, Reliability, Performance, Availability, Scalability). |
| Technology Stack | Documents the chosen stack: Python + Pandas (data processing), SQLite (database), Tableau Desktop + Tableau Public (visualization), Flask + HTML + CSS (web application), GitHub (version control). |

---

## 4. Project Design Phase

*(Folder: 05_Documentation/)*

| Document | Summary |
|----------|---------|
| Problem-Solution Fit | A Problem-Solution Fit Canvas covering customer segments (EV buyers, market analysts), root causes (scattered EV data, no visual platform), triggers (rising fuel prices, government EV incentives), and the proposed solution: a centralized EV Analytics platform with interactive filters and a public web interface. |
| Proposed Solution | The formal proposal: use Tableau to build interactive dashboards from a cleaned SQLite database, publish on Tableau Public, and embed into a Flask website. Covers novelty (combined India + Global data in one place), social impact (supporting EV adoption in India), and scalability (new datasets/regions can be added easily). |
| Solution Architecture | Defines a linear pipeline architecture: Raw CSV Files → data_cleaning.py (Python/Pandas) → ev_analytics.db (SQLite) → Tableau (Dashboards & Story) → Tableau Public (hosting) → E-CarStart Flask Website → End User. |

---

## 5. Project Planning Phase

*(Folder: 05_Documentation/)*

The project was planned across 3 sprints, each mapped to an epic:

1. **Sprint 1** — Epic 1: Data Collection & Preparation (dataset 
   gathering, database loading, data cleaning, calculated fields). 
   Total story points: 9.
2. **Sprint 2** — Epic 2: Data Visualization & Dashboard (brand 
   comparison charts, charging station map, Global & India 
   dashboards with 4 filters). Total story points: 12.
3. **Sprint 3** — Epic 3: Story, Web Integration & Testing 
   (4-scene Tableau story, Flask website, performance testing). 
   Total story points: 12.

Total Story Points: 33 | Velocity: 11 points per sprint

Each user story was estimated with story points (1–5 scale) and 
mapped to sprints following an Agile/Scrum backlog format.

---

## 6. Project Development Phase

*(Folder: 02_Database/, 03_Data_Preparation/, 
04_Tableau/, 06_Web_Integration/)*

| Component | Summary |
|-----------|---------|
| Data Collection | 4 CSV datasets collected covering global EV specs (478 rows), India charging stations (1,342 rows), India EV sales (5,000 rows), and global EV market (96,845 rows). Total: 1,03,665 rows. |
| data_cleaning.py | Python script using Pandas to remove null values, fix column name inconsistencies, remove duplicates, standardize categorical data, and create 2 calculated fields (Count, Count_powertrain). |
| create_database.py | Python script using sqlite3 to create ev_analytics.db with 4 tables (vehicle_specs, charging_stations, ev_sales, global_market) and load cleaned data. |
| Tableau Dashboards | 18 visualizations across India EV Analytics Dashboard (8 charts: map, bar charts, treemaps, bubble chart) and Global EV Market Overview Dashboard (5 charts). 4 interactive filters: BodyStyle, Brand, PowerTrain, Car Filter. 2 calculated fields: Count, Count_powertrain. |
| Tableau Story | 4-scene story titled "Story of Electric Cars in India": Different Brands & Models, Price Range of EVs, Charging Stations by Region & Type, Charging Stations Map of India. |
| app.py (Flask) | Flask web application named E-CarStart with 6 pages (Home, About, Dashboard, Story, Team, Contact) embedding both Tableau dashboards and the story via Tableau Public iframe links. Home page displays summary cards: 98 Global EV Brands, 9 India EV Brands, 477 EV Models. |

---

## 7. Performance Testing

*(Folder: 05_Documentation/)*

Performance testing was conducted to verify 4 key parameters:

| Parameter | Result |
|-----------|--------|
| Data Rendered to DB | 1,03,665 rows across 4 tables: vehicle_specs (478) + charging_stations (1,342) + ev_sales (5,000) + global_market (96,845) |
| Data Filters | 4 filters — BodyStyle, Brand, PowerTrain, Car Filter |
| Calculated Fields | 2 fields — Count, Count_powertrain |
| Total Visualizations | 18 graphs across 2 dashboards + 1 story |

Data verification was done using Python sqlite3 SELECT COUNT(*) 
queries in the VS Code terminal. All 4 filters were tested to 
confirm correct cross-chart updates. Both calculated fields 
confirmed accurate values in dashboard summary cards.

---

## 8. Project Documentation

*(Folder: 05_Documentation/)*

| Document | Summary |
|----------|---------|
| EV_Analytics_Final_Report.docx | Complete project report covering all phases: Ideation, Requirement Analysis, Project Design, Project Planning, Performance Testing, Results (with screenshots), Advantages & Disadvantages, Conclusion, and Future Scope. Includes DFD diagram, Solution Architecture diagram, and Burndown Chart. |
| Practical_Training_Report.docx | College training report following the institution's template format: Title Page, Acknowledgment, Candidate's Declaration, Certificate, Abstract, 5 Chapters (Introduction, Data Collection, Data Preparation & Visualization, Web Integration & Testing, Conclusions), and Appendix. |
| Video Script | 6-minute explanation video script covering all 10 sections of the project, presented by Radhika Agarwal. |
| Presentation | 13-slide PowerPoint presentation with EV-themed color scheme covering all project phases with actual dashboard screenshots. |

---

## 9. Repository Structure

EV_Analytics_Project/
├── .gitignore
├── requirements.txt              # Flask + Pandas
├── README.md
│
├── 01_Dataset/                   # Raw CSV datasets
│   ├── electric_vehicles_spec_2025.csv
│   ├── EV_Dataset(1).csv
│   ├── ev-charging-stations-india.csv
│   └── global_ev_market_charging_infrastructure.csv
│
├── 02_Database/                  # SQLite database + creation script
│   ├── create_database.py
│   └── ev_analytics.db
│
├── 03_Data_Preparation/          # Data cleaning script
│   ├── data_cleaning.py
│   └── Cleaned_Data/
│
├── 04_Tableau/                   # Tableau workbook files
│
├── 05_Documentation/             # All project documents
│   └── EV_Analytics_Final_Report.docx
│
├── 06_Web_Integration/           # Flask web application
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── 07_Vedio/                     # Project demo video
├── 08_Presentation/              # PPT slides
└── 09_Resource/                  # Reference materials
---

## 10. Getting Started Locally

**Prerequisites:** Python 3.13+, Git

```bash
# 1. Clone the repository
git clone https://github.com/manishsharma02/EV_Analytics_Project.git
cd EV_Analytics_Project

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install flask pandas

# 4. Run the web application
cd 06_Web_Integration
python app.py

# 5. Open browser
# Go to http://localhost:5000

Then open http://localhost:5000 to explore the E-CarStart website
with embedded Tableau dashboards, India charging station map,
and the EV story.
11. Tableau Public Links
🌍 Global EV Market Overview Dashboard
🇮🇳 India EV Analytics Dashboard
📖 Story of Electric Cars in India
12. Conclusion
EV Analytics demonstrates how raw, scattered electric vehicle data
can be transformed into a centralized, visually rich analytics
platform using industry-standard tools. Across all 7 documented
project phases — from empathy mapping through performance testing
— the team validated the problem, designed a clean data pipeline
architecture, developed 18 interactive Tableau visualizations, and
shipped a complete Flask web application.
The result is a working, publicly accessible EV Analytics platform
— not just a prototype — that helps EV buyers make informed
decisions and supports India's growing EV ecosystem.
13. Summary
Problem: EV buyers in India cannot find a single platform to
compare brands, prices, efficiency, and charging stations.
Solution: A centralized platform combining 4 EV datasets
(1,03,665 rows) in a SQLite database, visualized through 18
Tableau charts across 2 dashboards and 1 story, embedded in a
Flask website.
Delivery: 3 sprints, 10 user stories, 18 visualizations,
4 interactive filters, 2 calculated fields — all completed and
tested.
Validation: Performance tested for data capacity
(1,03,665 rows), filter functionality (4 filters), calculated
fields (2), and visualization count (18).
What's next: Real-time API integration, machine learning
predictions, mobile app version, dealer booking integration.

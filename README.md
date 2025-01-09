# **DSA210 Project: Car & Spotify Usage Analysis**
## **Demo Video (Highly suggested for understanding)**

[Click here to watch the demo video](videoexplainingproject.mp4)

As you can see I had to change the project but it stayed as youtube usage analysis since I am not able to change the github repo.
## **Motivation**  
I spend a lot of time driving to school and visiting my family on weekends. Since I spend so much time driving, I wanted to understand what I typically do during that time.  
My hypothesis was that I listen to music **at least 75%** of the time while driving.

### **Hypotheses:**
- **\( H_0 \) (Null Hypothesis):** The proportion of time I listen to music while driving is less than 75%.  
- **\( H_a \) (Alternative Hypothesis):** The proportion of time I listen to music while driving is at least 75%.

---

## **Data Source**  
I created my own data source using an online website and a database to track my activity:  
**Website:** [Car Button for Baris](https://carbuttonforbaris.netlify.app/)
also here is the repo [carbuttonchecker](https://github.com/barisMarathon/carbuttonchecker)

### **How the Data Was Collected:**  
- **First button**: Pressed when entering the car.  
- **Second button**: Pressed when starting Spotify.

To help remind me to press the buttons, I used **Apple Shortcuts**.

---

## **Data Analysis**

### **1. Preventing Data Duplication**  
- Used **SQL** to remove duplicate entries.  
- Any data entry within **±15 seconds** was considered a duplicate and removed.

### **2. Shaping the Data**  
- Converted SQL records to text and cleaned the data using a **Python script** to remove unnecessary symbols.

---

## **Visualization and Hypothesis Testing**

- **Initial Visualization**: Created plots to visually observe if I was close to my hypothesis (using `DSA210.py`).  
- **Activity Tracking**: Analyzed when and how much I performed these two activities (Spotify usage vs. being in the car).  

### **Hypothesis Test**:
- Defined a matching event as opening Spotify **within 15 minutes** of entering the car.
- Calculated the **z-score** and performed a statistical hypothesis test (using `hypothesis_test.py`).

---

## **Findings**  
I found that I was **correct**: I listen to music during most of my drives.  
Interestingly, despite thinking that I had been listening to the radio more over the past month, the analysis showed that **83%** of the time I was using Spotify.

---

## **Limitations and Future Work**  
### **Limitations**:
- The data does not capture when I listen to the radio.  

### **Future Work**:
- Expand the project by tracking the times I listen to the radio.
- Consider implementing an **AI system** that automatically detects what I am listening to and sends the data to the database, removing the need for manual button presses.

---

## **Usage Instructions**  

### **Files in the Repository:**
1. **`DSA210.py`**: Script for visualizing Spotify and car data.
2. **`hypothesis_test.py`**: Script for performing hypothesis testing using z-scores.
3. **`SQLtoTXT.py`**: Script for performing transitions from sql to txt.
4. **SQL Files**: Include SQL queries for cleaning and querying the database.

### **To Run the Analysis**:
1. Ensure Python and required libraries (`pandas`, `matplotlib`, `scipy`, etc.) are installed.
2. Load and clean the data using the SQL queries.
3. Use the Python scripts to visualize the data and run hypothesis tests.

---
Also I didn't hide the database password and username you can enter try yourself since it is a basic 5mb database from a random free site.

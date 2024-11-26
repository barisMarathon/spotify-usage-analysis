# My YouTube Viewing Data Analysis

## Description

Sabanci University CS210 Introduction to Data Science Course Fall 2023-2024 Term Project.  
This project is an analysis of my personalized <a href="https://www.youtube.com/" target="_blank">YouTube</a> viewing data.

For the final report, see [here](#).

## Table of Contents
**[Motivation](#motivation)**  

**[Tools](#tools)**  

**[Data Source](#data-source)**  
* [Personalized Data](#personalized-data)  
* [YouTube Data API](#youtube-data-api)  

**[Data Processing](#data-processing)**  

**[Data Visualizations](#data-visualizations)**  

**[Data Analysis](#data-analysis)**  
* [Viewing Habits](#viewing-habits)  
* [Content Preferences](#content-preferences)  
* [Time Distribution](#time-distribution)  

**[Findings](#findings)**  
* [Viewing Trends](#viewing-trends)  
* [Category Insights](#category-insights)  
* [Content Exploration](#content-exploration)  

**[Limitations](#limitations)**  
* [Data Collection Challenges](#data-collection-challenges)  
* [Analysis Constraints](#analysis-constraints)  

**[Future Work](#future-work)**  

---

## Motivation

YouTube has become one of the primary platforms I use for entertainment, learning, and exploration. Analyzing my personalized data offers a unique opportunity to better understand my viewing habits and preferences. By examining the content I consume, identifying trends in watch time, and exploring content categories, I hope to uncover meaningful insights into my online behavior.

---

### Tools

- **[Python](https://www.python.org/):** Used for data retrieval, processing, and analysis.  
- **[Jupyter Notebook](https://jupyter.org/):** For interactive coding and documentation.  
- **[Pandas](https://pandas.pydata.org/):** Data cleaning, structuring, and manipulation.  
- **[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** Data visualization and pattern identification.  
- **[Scikit-learn](https://scikit-learn.org/):** Machine learning models for clustering and prediction.  
- **[Google Colab](https://colab.research.google.com/):** For cloud-based computation.  

---

## Data Source

The project data is derived from two main sources:

### Personalized Data

- I retrieved my YouTube activity data using the account data download feature. This includes viewing history, liked videos, and playlists.  
- The data contains timestamps, video metadata, and interaction history, ensuring personalized insights.

### YouTube Data API

- Using the [YouTube Data API v3](https://developers.google.com/youtube/v3), I accessed supplementary data, such as:  
  - Video statistics (likes, views, comments).  
  - Channel details (categories, subscribers).  
  - Metadata for videos I interacted with.  
- All API interactions adhered to the quota limits and terms of service. Scripts are available in `youtube_api_scripts.py`.

---

## Data Processing

The collected data required preprocessing to ensure usability and relevance. Key steps included:  

- **Timestamp Conversion:** Standardizing all timestamps to local time for analysis.  
- **Metadata Enrichment:** Merging API-derived metadata with my viewing history.  
- **Cleaning:** Removing incomplete or redundant entries from the dataset.  
- **Categorization:** Assigning content categories (e.g., Education, Entertainment) based on video metadata.  

Detailed steps are documented in `data_processing.ipynb`.

---

## Data Visualizations

To explore the data, I created various visualizations using Matplotlib and Seaborn. Highlights include:  

- **Viewing Trends:** Line charts showing daily and weekly viewing habits.  
- **Content Breakdown:** Pie charts displaying time spent on different video categories.  
- **Engagement Patterns:** Heatmaps of viewing times to identify peak hours.

Interactive visualizations are hosted in `data_visualization.ipynb`. For static images, see the `figures` directory.

---

## Data Analysis

### Viewing Habits
Analyzed my daily and weekly activity to uncover patterns, such as peak viewing times and variations across weekdays and weekends.

### Content Preferences
Clustered videos into categories using metadata and tags. Analyzed time spent on each category to understand interests.

### Time Distribution
Examined the duration of videos watched to identify preferences for short-form vs. long-form content.

---

## Findings

### Viewing Trends
- Peak viewing times were in the evening on weekdays and mid-afternoon on weekends.  
- Viewing habits varied significantly between weekdays and weekends.

### Category Insights
- A majority of time was spent on **Education** and **Entertainment** categories.  
- Niche interests like **Music** and **Tech Reviews** accounted for a smaller share but had consistent engagement.

### Content Exploration
- Discovered trends in content discovery, with playlists being a significant driver for new video engagement.

---

## Limitations

### Data Collection Challenges
- API quota restrictions limited the number of videos for which metadata could be fetched.  
- Missing data for deleted videos or private playlists.

### Analysis Constraints
- Limited scope of machine learning models due to the dataset size and variety.  
- Results may not generalize to other platforms or time periods.

---

## Future Work

- **Broader Analysis:** Incorporate additional data (e.g., search history) for a more comprehensive view of usage patterns.  
- **Interactive Dashboard:** Create a web-based dashboard for live analysis and visualization of viewing habits.  
- **Longitudinal Study:** Extend the analysis to include future data, tracking changes in habits over time.  

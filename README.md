# My Spotify Listening Data Analysis

## Description
!!! THE PROJECT WAS INITIALLY ABOUT YOUTUBE BUT BECAUSE OF THE CHANGES MADE TO THE YOUTUBE API I HAD TO GO WITH SPOTIFY INSTEAD
!!! I COULDNT CHANGE THE PROJECT TITLE BECAUSE OF THE LINK I SUBMITTED ALREADY
Sabancı University CS210 Introduction to Data Science Course Fall 2024-2025 Term Project.  
This project is an analysis of my personalized [Spotify](https://www.spotify.com/) listening data.

For the final report, see [here](#).

## Table of Contents

- [Motivation](#motivation)
- [Tools](#tools)
- [Data Source](#data-source)
  - [Personalized Data](#personalized-data)
  - [Spotify Web API](#spotify-web-api)
- [Data Processing](#data-processing)
- [Data Visualizations](#data-visualizations)
- [Data Analysis](#data-analysis)
  - [Listening Habits](#listening-habits)
  - [Genre Preferences](#genre-preferences)
  - [Time Distribution](#time-distribution)
- [Findings](#findings)
  - [Listening Trends](#listening-trends)
  - [Genre Insights](#genre-insights)
  - [Artist Exploration](#artist-exploration)
- [Limitations](#limitations)
  - [Data Collection Challenges](#data-collection-challenges)
  - [Analysis Constraints](#analysis-constraints)
- [Future Work](#future-work)

---

## Motivation

Spotify is one of my primary platforms for music and podcast consumption. Analyzing my personalized data offers a unique opportunity to better understand my listening habits and preferences. By examining the content I consume, identifying trends in listening time, and exploring genre preferences, I hope to uncover meaningful insights into my audio consumption behavior.

---

## Tools

- **[Python](https://www.python.org/):** Used for data retrieval, processing, and analysis.
- **[Jupyter Notebook](https://jupyter.org/):** For interactive coding and documentation.
- **[Pandas](https://pandas.pydata.org/):** Data cleaning, structuring, and manipulation.
- **[Matplotlib](https://matplotlib.org/)** and **[Seaborn](https://seaborn.pydata.org/):** Data visualization and pattern identification.
- **[Spotipy](https://spotipy.readthedocs.io/):** A lightweight Python library for the Spotify Web API.
- **[Google Colab](https://colab.research.google.com/):** For cloud-based computation.

---

## Data Source

The project data is derived from two main sources:

### Personalized Data

- I retrieved my Spotify activity data using the account data download feature. This includes listening history, liked songs, and playlists.
- The data contains timestamps, track metadata, and interaction history, ensuring personalized insights.

### Spotify Web API

- Using the [Spotify Web API](https://developer.spotify.com/documentation/web-api/), I accessed supplementary data, such as:
  - Track statistics (popularity, audio features).
  - Artist details (genres, followers).
  - Metadata for tracks and artists I interacted with.
- All API interactions adhered to the rate limits and terms of service. Scripts are available in `spotify_api_scripts.py`.

---

## Data Processing

The collected data required preprocessing to ensure usability and relevance. Key steps included:

- **Timestamp Conversion:** Standardizing all timestamps to local time for analysis.
- **Metadata Enrichment:** Merging API-derived metadata with my listening history.
- **Cleaning:** Removing incomplete or redundant entries from the dataset.
- **Categorization:** Assigning genres to tracks based on artist metadata.

Detailed steps are documented in `data_processing.ipynb`.

---

## Data Visualizations

To explore the data, I created various visualizations using Matplotlib and Seaborn. Highlights include:

- **Listening Trends:** Line charts showing daily and weekly listening habits.
- **Genre Breakdown:** Pie charts displaying time spent on different music genres.
- **Engagement Patterns:** Heatmaps of listening times to identify peak hours.

Interactive visualizations are hosted in `data_visualization.ipynb`. For static images, see the `figures` directory.

---

## Data Analysis

### Listening Habits

Analyzed my daily and weekly activity to uncover patterns, such as peak listening times and variations across weekdays and weekends.

### Genre Preferences

Clustered tracks into genres using artist metadata. Analyzed time spent on each genre to understand musical interests.

### Time Distribution

Examined the duration of listening sessions to identify preferences for short vs. long listening periods.

---

## Findings

### Listening Trends

- Peak listening times were in the evening on weekdays and mid-afternoon on weekends.
- Listening habits varied significantly between weekdays and weekends.

### Genre Insights

- A majority of time was spent on **Pop** and **Rock** genres.
- Niche genres like **Jazz** and **Classical** accounted for a smaller share but had consistent engagement.

### Artist Exploration

- Discovered trends in artist discovery, with playlists and recommendations being significant drivers for new artist engagement.

---

## Limitations

### Data Collection Challenges

- API rate limits restricted the number of tracks for which metadata could be fetched.
- Missing data for tracks or artists not available on Spotify.

### Analysis Constraints

- Limited scope of machine learning models due to the dataset size and variety.
- Results may not generalize to other platforms or time periods.

---

## Future Work

- **Broader Analysis:** Incorporate additional data (e.g., podcast listening history) for a more comprehensive view of audio consumption patterns.
- **Interactive Dashboard:** Create a web-based dashboard for live analysis and visualization of listening habits.
- **Longitudinal Study:** Extend the analysis to include future data, tracking changes in habits over time.

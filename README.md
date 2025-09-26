# NFL Play-by-Play Data Downloader

A Streamlit application that allows users to easily download NFL play-by-play data in CSV format using the `nfl_data_py` library.

## Features

- Download play-by-play data for any NFL season from 1999 to present
- Filter data by team:
  - **None**: Download all plays for the season
  - **Team in Possession**: Only plays where the selected team has the ball
  - **Plays Involving Team**: All plays involving the selected team (offense or defense)
- Preview data before downloading
- Export filtered data as CSV

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run nfl_pbp_downloader.py
```

2. The app will open in your default web browser
3. Follow the on-screen instructions:
   - Select a season
   - Choose a filter type (optional)
   - If filtering, select a team
   - Click "Load Data" to fetch the data
   - Click "Download CSV" to save the data

## Notes

- Loading data for an entire season may take several minutes
- The app uses the `nfl_data_py` library which sources data from nflfastR
- Downloaded CSV files will be named according to your filter selections

## Requirements

- Python 3.7+
- streamlit
- nfl-data-py
- pandas
- numpy

## Team Abbreviations

- ARI: Arizona Cardinals
- ATL: Atlanta Falcons
- BAL: Baltimore Ravens
- BUF: Buffalo Bills
- CAR: Carolina Panthers
- CHI: Chicago Bears
- CIN: Cincinnati Bengals
- CLE: Cleveland Browns
- DAL: Dallas Cowboys
- DEN: Denver Broncos
- DET: Detroit Lions
- GB: Green Bay Packers
- HOU: Houston Texans
- IND: Indianapolis Colts
- JAX: Jacksonville Jaguars
- KC: Kansas City Chiefs
- LA: Los Angeles Rams
- LAC: Los Angeles Chargers
- LV: Las Vegas Raiders
- MIA: Miami Dolphins
- MIN: Minnesota Vikings
- NE: New England Patriots
- NO: New Orleans Saints
- NYG: New York Giants
- NYJ: New York Jets
- PHI: Philadelphia Eagles
- PIT: Pittsburgh Steelers
- SEA: Seattle Seahawks
- SF: San Francisco 49ers
- TB: Tampa Bay Buccaneers
- TEN: Tennessee Titans
- WAS: Washington Commanders

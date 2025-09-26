import streamlit as st
import nfl_data_py as nfl
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="NFL Play-by-Play Data Downloader",
    page_icon="🏈",
    layout="wide"
)

# Title
st.title("NFL Play-by-Play Data Downloader")

# Create two columns for layout
col1, col2 = st.columns([1, 1.5])

with col1:
    # Season selection
    current_year = datetime.now().year
    seasons = list(range(1999, current_year + 1))[::-1]  # Reverse to show newest first
    
    st.markdown("**Select Season:**")
    selected_season = st.selectbox(
        "Select Season",
        options=seasons,
        index=seasons.index(2022) if 2022 in seasons else 0,
        label_visibility="collapsed"
    )
    
    # Filter type selection
    st.markdown("**Filter Type:**")
    filter_type = st.selectbox(
        "Filter Type",
        options=["None", "Team in Possession", "Plays Involving Team"],
        label_visibility="collapsed"
    )
    
    # Team selection (only show if filter type is not "None")
    if filter_type != "None":
        st.markdown("**Select Team:**")
        # Get list of teams
        teams = [
            "ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE",
            "DAL", "DEN", "DET", "GB", "HOU", "IND", "JAX", "KC",
            "LA", "LAC", "LV", "MIA", "MIN", "NE", "NO", "NYG",
            "NYJ", "PHI", "PIT", "SEA", "SF", "TB", "TEN", "WAS"
        ]
        selected_team = st.selectbox(
            "Select Team",
            options=teams,
            label_visibility="collapsed"
        )
    
    # Load data button
    load_button = st.button("Load Data", type="primary", use_container_width=True)
    
    # Initialize session state for data
    if 'data' not in st.session_state:
        st.session_state.data = None
        st.session_state.filtered_data = None
    
    # Load data when button is clicked
    if load_button:
        with st.spinner(f"Loading {selected_season} play-by-play data..."):
            try:
                # Load play-by-play data
                data = nfl.import_pbp_data([selected_season])
                st.session_state.data = data
                
                # Apply filters if selected
                if filter_type == "None":
                    st.session_state.filtered_data = data
                elif filter_type == "Team in Possession":
                    st.session_state.filtered_data = data[data['posteam'] == selected_team]
                else:  # "Plays Involving Team"
                    st.session_state.filtered_data = data[
                        (data['posteam'] == selected_team) | 
                        (data['defteam'] == selected_team)
                    ]
                
                st.success(f"Data loaded successfully! {len(st.session_state.filtered_data):,} plays found.")
            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
    
    # Download button
    if st.session_state.filtered_data is not None:
        csv = st.session_state.filtered_data.to_csv(index=False)
        
        # Create filename
        if filter_type == "None":
            filename = f"nfl_pbp_{selected_season}.csv"
        elif filter_type == "Team in Possession":
            filename = f"nfl_pbp_{selected_season}_{selected_team}_possession.csv"
        else:
            filename = f"nfl_pbp_{selected_season}_{selected_team}_all_plays.csv"
        
        st.download_button(
            label="⬇ Download CSV",
            data=csv,
            file_name=filename,
            mime="text/csv",
            use_container_width=True
        )
    
    # Note
    st.markdown(
        """
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-top: 20px;'>
        <span style='color: red; font-weight: bold;'>Note:</span> 
        <span style='color: red;'>Season-long, unfiltered downloads may take several minutes to complete.</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    # Instructions
    st.markdown("## Instructions:")
    st.markdown(
        """
        1. Select a season from the dropdown menu.
        2. Choose a filter type (optional):
           - **'None'** for all plays
           - **'Team in Possession'** for plays where the selected team has the ball
           - **'Plays Involving Team'** for all plays involving the selected team
        3. If filtering by team, select the desired team from the dropdown.
        4. Click **'Load Data'** to retrieve the play-by-play information.
        5. Once data is loaded, click **'Download CSV'** to save the data to your computer.
        """
    )
    
    # Display data preview if available
    if st.session_state.filtered_data is not None:
        st.markdown("---")
        st.markdown("### Data Preview")
        st.markdown(f"**Total plays:** {len(st.session_state.filtered_data):,}")
        
        # Show first few rows
        st.dataframe(
            st.session_state.filtered_data.head(100),
            use_container_width=True,
            height=400
        )

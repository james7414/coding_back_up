""" Script used to help clean data extracted from fbref. """

import pandas as pd
from src.config.fbref_config import (
    FIXTURE_TABLE_COLUMNS,
)


def clean_fixtures_df(fixtures_df):
    """Function used to clean fixtures data extracted from FBref"""
    cleaned_fixtures_df = (
        fixtures_df
        # change column types
        .astype(
            {
                "home_score": float,
                "away_score": float,
                "Venue": "category",
                "Referee": "category",
            }
        )
        # rename
        .rename(
            columns={
                "Wk": "week",
                "Day": "dow",
                "Date": "date",
                "Time": "time",
                "Home": "home_team",
                "xG": "xG_home",
                "xG.1": "xG_away",
                "Away": "away_team",
                "Attendance": "attendance",
                "Referee": "referee",
                "Notes": "notes",
            }
        )
        # set kick off column
        .assign(kickoff=pd.to_datetime(fixtures_df["Date"] + " " + fixtures_df["Time"]))
        # filter for columns we want
        [FIXTURE_TABLE_COLUMNS]
    )
    return cleaned_fixtures_df


def clean_league_table_df(league_table_df):
    """Function used to clean league table data extracted from FBref"""
    cleaned_league_table_df = (
        league_table_df
        # change column types
        .astype(
            {
                "Squad": "category",
            }
        )
        # rename
        .rename(
            columns={
                "Rank": "Position",
                "Home_Pts/MP": "Home_Pts_Per_MP",
                "Away_Pts/MP": "Away_Pts_Per_MP",
            }
        )
        # Create new columns
        .assign(
            win_perc=lambda dfr: round(dfr.W / dfr.MP, 3),
            draw_perc=lambda dfr: round(dfr.D / dfr.MP, 3),
            loss_perc=lambda dfr: round(dfr.L / dfr.MP, 3),
            home_win_perc=lambda dfr: round(dfr.Home_W / dfr.Home_MP, 3),
            home_draw_perc=lambda dfr: round(dfr.Home_D / dfr.Home_MP, 3),
            home_loss_perc=lambda dfr: round(dfr.Home_L / dfr.Home_MP, 3),
            away_win_perc=lambda dfr: round(dfr.Away_W / dfr.Away_MP, 3),
            away_draw_perc=lambda dfr: round(dfr.Away_D / dfr.Away_MP, 3),
            away_loss_perc=lambda dfr: round(dfr.Away_L / dfr.Away_MP, 3),
            goals_per_game=lambda dfr: round(dfr.GF / dfr.MP, 3),
            goals_against_per_game=lambda dfr: round(dfr.GA / dfr.MP, 3),
            home_goals_per_game=lambda dfr: round(dfr.Home_GF / dfr.Home_MP, 3),
            home_goals_against_per_game=lambda dfr: round(dfr.Home_GA / dfr.Home_MP, 3),
            away_goals_per_game=lambda dfr: round(dfr.Away_GF / dfr.Away_MP, 3),
            away_goals_against_per_game=lambda dfr: round(dfr.Away_GA / dfr.Away_MP, 3),
        )
    )
    return cleaned_league_table_df

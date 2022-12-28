import streamlit as st
import pandas as pd
import plotly.express as px

def filter_by_team_member(df, team_member):
    # Create a boolean mask to select only the rows where the "filter_column" is team_member
    mask = df['First Name'] == team_member

    # Use the mask to select only the rows that meet the condition
    filtered_df = df[mask]

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(filtered_df, values='Hours', names='Project',title='Hours by Project for '+team_member, hole=0.4)
        fig.update_layout(height=400, width=400)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=-1,
            bgcolor='rgba(0,0,0,0)'
        ))
        st.plotly_chart(fig)

    with col2:
        fig = px.pie(filtered_df, values='Hours', names='Task',title='Hours by Task for '+team_member, hole=0.4)
        fig.update_layout(height=400, width=400)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=-1,
            bgcolor='rgba(0,0,0,0)'
        ))
        st.plotly_chart(fig)

    return


# Read the Excel file into a pandas DataFrame
myfile = st.file_uploader("Enter XLSX file")

if myfile != None:
    df = pd.read_excel(myfile)

    # Show the data as a table
    #st.write(df)
    # Create a pie chart with Plotly
    fig = px.pie(df, values='Hours', names='Client',title='Hours by Client', hole=0.4)
    st.plotly_chart(fig)

    fig = px.pie(df, values='Hours', names='Project',title='Hours by Project', hole=0.4)
    st.plotly_chart(fig)

    #loop through the people

    team_members = df['First Name'].unique().tolist()

    for team_member in team_members:
        filter_by_team_member(df,team_member)

    #now select project and show who has worked on it
    projects = df['Project'].unique().tolist()
    this_project = st.selectbox("Choose project",options=projects)
    mask = df["Project"] == this_project
    filtered_df = df[mask]
    fig = px.pie(filtered_df, values='Hours', names='First Name', title='Hours by Team Member for ' + this_project,
                     hole=0.4)
    st.plotly_chart(fig)


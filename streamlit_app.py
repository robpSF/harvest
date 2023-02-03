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

    if "Amount" in df.columns: #expenses report
        # Create a pie chart with Plotly
        fig = px.pie(df, values='Amount', names='Client',title='Expenses by Client', hole=0.4)
        fig.update_traces(textinfo='value',texttemplate='£%{value:,.2f}')
        fig.update_layout(margin=dict(t=30, b=30, l=30, r=30))
        st.plotly_chart(fig)

        fig = px.pie(df, values='Amount', names='Project',title='Expenses by Project', hole=0.4)
        fig.update_traces(textinfo='value', texttemplate='£%{value:,.2f}')
        fig.update_layout(margin=dict(t=30, b=30, l=30, r=30))
        st.plotly_chart(fig)

        fig = px.pie(df, values='Amount', names='Category',title='Expenses by Category', hole=0.4)
        fig.update_traces(textinfo='value', texttemplate='£%{value:,.2f}')
        fig.update_layout(margin=dict(t=30, b=30, l=30, r=30))
        st.plotly_chart(fig)


        fig = px.sunburst(df, path=['Project', 'Category'], values='Amount',labels=['Project', 'Category'])
        fig.update_traces(textinfo='label+value',texttemplate='%{label}:\n £%{value:,.2f}')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)

        fig = px.sunburst(df, path=['Category','First name'], values='Amount',labels=['Category','First name'])
        fig.update_traces(textinfo='label+value',texttemplate='%{label}:\n £%{value:,.2f}')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)

        fig = px.bar(df, x="Amount", y="Notes", orientation='h')
        st.plotly_chart(fig)

    else: #time report
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

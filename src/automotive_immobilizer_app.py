import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client




st.set_page_config(
    # Shows the page title
    page_title='Immobilizer Assistant',
    # Shows the page icon on the browser tab.
    page_icon=':closed_lock_with_key:',
    # Set the position of the results after selecting make/year/model
    layout='centered',
    initial_sidebar_state='expanded'
)

st.write("<div align='center'><h2><i>Immobilizer Assistant</i></h2></div>", unsafe_allow_html=True)

# Shows the header using HTML.
st.write("<div align='left'><h2 style='font-size: 20px;'><i>Please, select Make, Year and Model desired:</i></h2></div>", unsafe_allow_html=True)



# Get Supabase URL from environment variable
url: str = os.environ.get("NEXT_PUBLIC_SUPABASE_URL")
# Get Supabase anonymous key from environment variable 
key: str = os.environ.get("NEXT_PUBLIC_SUPABASE_ANON_KEY")

# Initialize Supabase client with URL and anonymous key
Supabase: Client = create_client(url, key)

def query_table_from_supabaseto_df(table_name):
    # Query all records from the table in Supabase and store the response 
    response_table = (Supabase.table(table_name).select("*").execute())

    # Store the queried data from Supabase response into a variab
    year_make_model_data = response_table.data

    # Convert the data to dataframe format
    df = pd.DataFrame(year_make_model_data)

    # Drop unnecessary columns came from the Supabase table
    df_dropped_columns = df.drop(columns=['id', 'created_at', 'updated_at'])

    # Return a clear df after query
    return df_dropped_columns

# Call the function to get a cleared df after query from Supabase
df_dropped_columns = query_table_from_supabaseto_df("year_make_model_table")

# Get a list w/ unique years from the main df
makes_list = df_dropped_columns['make'].unique()
# Sort the years list
sorted_makes = makes_list.sort()
# Show the sorted year list at the sidebar
selected_make = st.sidebar.selectbox('Make: ', (makes_list))

# Change the name of make to getthe database from Supabase
selected_table = f'{selected_make.lower()}_table'

# Call the function to get a cleared df after query from Supabase
make_selected = query_table_from_supabaseto_df(selected_table)

# Get a unique list with the years avaiable on the df_make selected  
years = make_selected['year'].unique()
# Sort the year list
sorted_years = sorted(years)
# Show the sorted years list at the sidebar
selected_year = st.sidebar.selectbox('Year: ', (sorted_years))

# Filter the df_make based on the year selected
df_filtered_after_year_selected = make_selected[make_selected['year'] == selected_year]

# Get a unique list with models available based on the year selected
models = df_filtered_after_year_selected['model'].unique()
# Sort the make list
sorted_models = sorted(models)
# Show the sorted makes list at the sidebar
selected_model = st.sidebar.selectbox('Model: ', (sorted_models))

# Filter the df_make based on the year selected to obtain the final dataframe
final_df = df_filtered_after_year_selected[df_filtered_after_year_selected['model'] == selected_model]

# Get the first row index (index 0) and store it as a Pandas Series object
data_final_df = final_df.iloc[0]

# Convert it to dict
dict_final_df = dict(data_final_df)

# Loop to show the data from the dict
for column, data in dict_final_df.items():
    st.write(f'''**:red[{column}:]** {data}''')




# streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\src\automotive_immobilizer_app.py'
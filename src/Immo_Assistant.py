import streamlit as st
import pandas as pd
import requests

# Get the url containing the main dataframe from the remote repository
url_df = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/data/year_make_model_df.xlsx'
# Requests the HTTP from the GitHub URL
df_response = requests.get(url_df)
# Stores the url content w/ the dataframe
df_content = df_response.content

# Load the DataFrame and save it in the variable df.
df = pd.read_excel(df_content)

# Converting all values in column Model to string, as some of models are numbers, for instance BMWs 318, 328, 525
df = df.astype({'Model':'string'})

# Store the urls in a variable
url_acura = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_acura_updated.xlsx'
url_audi = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_audi_updated.xlsx'
url_bmw = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_bmw_updated.xlsx'
url_buick = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_buick.xlsx'
url_cadillac = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_cadillac.xlsx'
url_chevrolet = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_chevy_filtered.xlsx'
url_chrysler = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_chrysler_updated.xlsx'
url_dodge = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_dodge_updated.xlsx'
url_fiat = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_fiat_updated.xlsx'
url_ford = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_ford_new.xlsx'
url_gmc = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_gmc.xlsx'
url_honda = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_honda_updated.xlsx'
url_hummer = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_hummer.xlsx'
url_infiniti = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_infiniti_up_to_dated.xlsx'
url_jaguar = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_jaguar_up_to_dated.xlsx'
url_jeep = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_jeep_updated.xlsx'
url_land_rover = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_land_rover_updated.xlsx'
url_lexus = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_lexus_updated.xlsx'
url_lincoln = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_lincoln_updated.xlsx'
url_mazda = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_mazda_updated.xlsx'
url_mercury = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_mercury_updated.xlsx'
url_mini = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_mini_updated.xlsx'
url_mitsubishi = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_mitsubishi_upddated.xlsx'
url_nissan = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_nissan_updated.xlsx'
url_oldsmobile = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_oldsmobile.xlsx'
url_plymouth = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_plymouth_updated.xlsx'
url_pontiac = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_pontiac.xlsx'
url_rolls_royce = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_rolls_royce_updated.xlsx'
url_saturn = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_saturn.xlsx'
url_scion = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_scion_updated.xlsx'
url_subaru = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_subaru_updated.xlsx'
url_toyota = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_toyota_updated.xlsx'
url_vw = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_vw_updated.xlsx' 


# Create a dictionary with the dataframes from each make
dataframes_urls = pd.DataFrame({'Makes': ['Acura', 'Audi', 'BMW','Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Fiat', 'Ford', 'GMC',
                                           'Honda', 'Hummer', 'infiniti', 'Jaguar', 'Jeep', 'Land Rover', 'Lexus', 'Lincoln', 'Mazda', 'Mercury',
                                           'Mini', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 'Rolls-Royce', 'Saturn', 'Scion', 
                                           'Subaru', 'Toyota', 'Volkswagen'],
                                'URLs': [url_acura, url_audi, url_bmw, url_buick, url_cadillac, url_chevrolet, url_chrysler, url_dodge, url_fiat, 
                                url_ford, url_gmc, url_honda, url_hummer, url_infiniti, url_jaguar, url_jeep, url_land_rover, url_lexus,
                                url_lincoln, url_mazda, url_mercury, url_mini, url_mitsubishi, url_nissan, url_oldsmobile, url_plymouth, 
                                url_pontiac, url_rolls_royce, url_saturn, url_scion, url_subaru, url_toyota, url_vw]})

# STREAMLIT CODE

# Sort and show the years in a sidebar
years = df['Year'].unique()
sorted_years = sorted(years)
selected_year = st.sidebar.selectbox('Year: ', (sorted_years))

# Same procedure with the makes
makes = df['Make'].unique()
sorted_makes = sorted(makes)
selected_make = st.sidebar.selectbox('Make: ', (sorted_makes))

# Function to convert the url link to .xlsx file
def convert_url_to_xlsx(url_make):
    # Store the raw content from the url link into a variable
    get_url = requests.get(url_make)
    # Convert the url link to bytes
    get_content = get_url.content
    # Return the bytes content into .xlsx file
    return pd.read_excel(get_content)

filtered_make = dataframes_urls[dataframes_urls['Makes'] == selected_make]

for index in filtered_make.index:
    index_selected = index

selected_url = filtered_make.at[index_selected, 'URLs']
df_selected = convert_url_to_xlsx(selected_url)
models = df_selected['Model'].unique()
sorted_models = sorted(models)
selected_model = st.sidebar.selectbox('Model: ', (sorted_models))
final_df = df_selected[(df_selected['Year'] == selected_year) & (df_selected['Model'] == selected_model)]
# st.write(final_df)

if not final_df.empty:
    final_df_dropped_column = final_df.drop(columns=['Unnamed: 0'])
    row_final_df = final_df_dropped_column.iloc[0]
    for column in final_df_dropped_column.columns:
        st.write (f'''**:red[{column}:]** {row_final_df[column]}''')
else:
    st.write("Year/Make/Model not avaiable in the data base")


# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\src\Immo_Assistant.py'
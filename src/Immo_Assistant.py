import streamlit as st
import pandas as pd
import requests
import openpyxl


# PROJECT NEXT STEPS:
# ADICIONAR UM COMENTARIO AQUI O MOTIVO PELO QUAL ESSA BIBLIOTECA FOI ADICIONADA, BEM COMO A PASTA REQUIREMENTS.TXT ADICIONADA TBM E AS BIBLIOTECAS.
# CORRIGIR O ERRO DA MONTADORA INFINITI.
# CORRIGIR DE concat([df_ford_new, df_lincoln_new]) PARA concat([df_lincoln_new, df_lincoln_new])


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

# Store the Github urls into the variables below
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


# Create a dataframe with all URLs from GitHub
dataframes_urls = pd.DataFrame({'Makes': ['Acura', 'Audi', 'BMW','Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Fiat', 'Ford', 'GMC',
                                           'Honda', 'Hummer', 'infiniti', 'Jaguar', 'Jeep', 'Land Rover', 'Lexus', 'Lincoln', 'Mazda', 'Mercury',
                                           'Mini', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 'Rolls-Royce', 'Saturn', 'Scion', 
                                           'Subaru', 'Toyota', 'Volkswagen'],
                                'URLs': [url_acura, url_audi, url_bmw, url_buick, url_cadillac, url_chevrolet, url_chrysler, url_dodge, url_fiat, 
                                url_ford, url_gmc, url_honda, url_hummer, url_infiniti, url_jaguar, url_jeep, url_land_rover, url_lexus,
                                url_lincoln, url_mazda, url_mercury, url_mini, url_mitsubishi, url_nissan, url_oldsmobile, url_plymouth, 
                                url_pontiac, url_rolls_royce, url_saturn, url_scion, url_subaru, url_toyota, url_vw]})

#--------------------------------------------------------------------------------------------------------#
#                                            STREAMLIT CODE                                              #
#--------------------------------------------------------------------------------------------------------#

# This application uses 2 types dataframes based on what the user selects. The main one where all makes are located. 
# It will be used to show the years and makes available at first.
# The 2nd dataframe is the one created for each make and stored the URLs into the dataframe named 'dataframes_urls'.
# Therefore, when mentioning the dataframe created for each make below, let's call it make/dataframe and the main the data from the dataframe named df

# Get a list w/ unique years from the main df
years = df['Year'].unique()
# Sort the years list
sorted_years = sorted(years)
# Show the sorted year list at the sidebar
selected_year = st.sidebar.selectbox('Year: ', (sorted_years))

# Get a unique make list from the main df
makes = df['Make'].unique()
# Sort the make list
sorted_makes = sorted(makes)
# Show the sorted makes list at the sidebar
selected_make = st.sidebar.selectbox('Make: ', (sorted_makes))

# Function to convert the url link to .xlsx file w/ the make/dataframe 
def convert_url_to_xlsx(url_make):
    # Store the raw content from the url link into a variable
    get_url = requests.get(url_make)
    # Convert the url link to bytes
    get_content = get_url.content
    # Return the bytes content into .xlsx file
    return pd.read_excel(get_content)

# Use the make selected by the user to select the url link w/ .xlsx file containing the dataframe
filtered_make = dataframes_urls[dataframes_urls['Makes'] == selected_make]

index_selected = 0
# Loop to get the index from the dataframe where the url link is located 
for index in filtered_make.index:
    # Store the link in a variable
    index_selected = index

# Filter the url link based on the index and the column it is located
selected_url = filtered_make.at[index_selected, 'URLs']

# Call the function to convert the url link from the GitHub w/ the dataframe from the spefic make selected by the user, to .xlsx file
df_selected = convert_url_to_xlsx(selected_url)

# Get a list w/ unique models from the dataframe selected
models = df_selected['Model'].unique()
# Sort the models
sorted_models = sorted(models)
# Show the models at the sidebar
selected_model = st.sidebar.selectbox('Model: ', (sorted_models))
# Filter the dataframe based on the year and model selected
final_df = df_selected[(df_selected['Year'] == selected_year) & (df_selected['Model'] == selected_model)]

# Condition to check the status of the final df after selecting year/make/model
if not final_df.empty:
    # For an unknown reason the index from the main df appears, this drops it
    final_df_dropped_column = final_df.drop(columns=['Unnamed: 0'])
    # Get the data/values from the final df based on the index
    row_final_df = final_df_dropped_column.iloc[0]
    # Loop to get the column names from the final fd
    for column in final_df_dropped_column.columns:
        # Print the columns and their elements on the application
        st.write (f'''**:red[{column}:]** {row_final_df[column]}''')
else:
    # Print the following message when the final df is empty
    st.write("Year/Make/Model not avaiable in the data base")


# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\src\Immo_Assistant.py'
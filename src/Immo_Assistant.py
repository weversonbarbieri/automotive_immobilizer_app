import streamlit as st
import pandas as pd
import requests
import openpyxl


#---------------------------------------- openpyxl -------------------------------------------#
# When deploying the application on Streamlit, the error 'ImportError: Missing optional dependency 'openpyxl'' occurred, 
# indicating that pandas suggests installing this library to handle Excel files.


#----------------------------------- requirements.txt -------------------------------------------#
# The 'ModuleNotFoundError' error occurred, indicating that Streamlit requires the creation of a file named requirements.txt, where the .py file is located, 
# listing all the libraries used in the project within this file.

st.set_page_config(
    # Shows the page title
    page_title='Immobilizer Assistant',
    # Shows the page icon on the browser tab.
    page_icon=':closed_lock_with_key:',
    # Set the position of the results after selecting make/year/model
    layout='centered',
    initial_sidebar_state='expanded'
)

# Shows the header using HTML.
st.write("<div align='left'><h2 style='font-size: 20px;'><i>Please, select Make, Year and Model desired:</i></h2></div>", unsafe_allow_html=True)


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

# Store the Github urls into the variables containing the dataframes and the PDF files.

#------------------------------------------------------------------------------------------------------------------------#
#                                                  Dataframes                                                            #
#------------------------------------------------------------------------------------------------------------------------#

url_acura = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_acura_updated.xlsx'
url_audi = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_audi_updated.xlsx'
url_bmw = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_bmw_updated.xlsx'
url_buick = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_buick.xlsx'
url_cadillac = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_cadillac.xlsx'
url_chevrolet = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_chevy_filtered.xlsx'
url_chrysler = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_chrysler_updated.xlsx'
url_dodge = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_dodge_updated.xlsx'
url_fiat = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_fiat_updated.xlsx'
url_ford = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/dataframe_each_make_xlsx_file/df_ford_removed_duplicated.xlsx'
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


#------------------------------------------------------------------------------------------------------------------------#
#                                                  PDF url from GitHub                                                   #
#------------------------------------------------------------------------------------------------------------------------#

ford_parameter_reset_bcfg_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/FORD_PARAMETER_RESET_B_C_F_G%20(15).pdf'
ford_parameter_reset_c_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/FORD_PARAMETER_RESET_C%20(6).pdf'
ford_pats_a_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/FORD_PATS_TYPE_A%20(1).pdf'
ford_pats_d_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/FORD_PATS_TYPE_D.pdf'
ford_pats_e_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/FORD_PATS_TYPE_E%20(3).pdf'
mazda_ma_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-A%20(3).pdf'
mazda_mb_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-B%20(1).pdf'
mazda_mc_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-C%20(1).pdf'
mazda_md_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-D.pdf'
mazda_me_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-E.pdf'
mazda_mf_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-F.pdf'
mazda_mg_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-G.pdf'
mazda_mh_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/Mazda_procedure_M-H.pdf'
gm_push_to_start_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/GM-PUSH_TO_START_INS.pdf'
gm_passlock_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/PASSLOCK.pdf'
gm_pk2_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/PK2.pdf'
gm_pk3_url = 'https://github.com/weversonbarbieri/immobilizer_assistant.app/raw/main/docs/PK3.pdf'

# Variables to store the label the downloaded file will have. In order to the download the file in PDF format, 
# the file label MUST have .pdf at the end. The procedure name is based on the Year/Make/Model selected.
ford_parameter_reset_bcfg_file_name = "ford_parameter_reset_bcfg.pdf"
ford_parameter_reset_c_file_name = "ford_parameter_reset_c.pdf"
ford_pats_a_file_name = "ford_pats_a.pdf"
ford_pats_d_file_name = "ford_pats_d.pdf"
ford_pats_e_file_name = "ford_pats_e.pdf"
mazda_ma_file_name = "mazda_ma.pdf"
mazda_mb_file_name = "mazda_mb.pdf"
mazda_mc_file_name = "mazda_mc.pdf"
mazda_md_file_name = "mazda_md.pdf"
mazda_me_file_name = "mazda_me.pdf"
mazda_mf_file_name = "mazda_mf.pdf"
mazda_mg_file_name = "mazda_mg.pdf"
mazda_mh_file_name = "mazda_mh.pdf"
gm_push_to_start_file_name = "gm_push_to_start.pdf"
gm_passlock_file_name = "gm_passlock.pdf"
gm_pk2_file_name = "gm_pk2.pdf"
gm_pk3_file_name = "gm_pk3.pdf"

# Variables to store the message included under the download button based on the name of the key relearn procedure.
ford_parameter_reset_bcfg_message = "Click on the button to download the PARAMETER RESET Instructions:"
ford_parameter_reset_c_message = "Click on the button to download the PARAMETER RESET Instructions:"
ford_pats_a_message = "Click on the button to download the PATS A Instructions:"
ford_pats_d_message = "Click on the button to download the PATS D Instructions:"
ford_pats_e_message = "Click on the button to download the PATS E Instructions:"
mazda_ma_message = "Click on the button to download the MAZDA M-A Instructions:"
mazda_mb_message = "Click on the button to download the MAZDA M-B Instructions:"
mazda_mc_message = "Click on the button to download the MAZDA M-C Instructions:"
mazda_md_message = "Click on the button to download the MAZDA M-D Instructions:"
mazda_me_message = "Click on the button to download the MAZDA M-E Instructions:"
mazda_mf_message = "Click on the button to download the MAZDA M-F Instructions:"
mazda_mg_message = "Click on the button to download the MAZDA M-G Instructions:"
mazda_mh_message = "Click on the button to download the MAZDA M-H Instructions:"
gm_push_to_start_message = "Click on the button to download the PUSH-TO-START Instructions:"
gm_passlock_message = "Click on the button to download the PASSLOCK Instructions:"
gm_pk2_message = "Click on the button to download the PASSKEY 2 Instructions:"
gm_pk3_message = "Click on the button to download the PASSKEY 3 Instructions:"

# Variables to store the button's label based on the name of the key relearn procedure.
ford_parameter_reset_bcfg_button_label = "Parameter Reset B, C, F, G Procedure"
ford_parameter_reset_c_button_label = "Parameter Reset C Procedure"
ford_pats_a_button_label = "PATS A Procedure"
ford_pats_d_button_label = "PATS D Procedure"
ford_pats_e_button_label = "PATS E Procedure"
mazda_ma_button_label = "Mazda M-A Procedure"
mazda_mb_button_label = "Mazda M-B Procedure"
mazda_mc_button_label = "Mazda M-C Procedure"
mazda_md_button_label = "Mazda M-D Procedure"
mazda_me_button_label = "Mazda M-E Procedure"
mazda_mf_button_label = "Mazda M-F Procedure"
mazda_mg_button_label = "Mazda M-G Procedure"
mazda_mh_button_label = "Mazda M-H Procedure"
gm_push_to_button_label = "Push-to-Start Procedure"
gm_passlock_button_label = "PASSLOCK Procedure"
gm_pk2_button_label = "PASSKEY 2 Procedure"
gm_pk3_button_label = "PASSKEY 3 Procedure"


# Create a dataframe with all URLs from GitHub
dataframes_urls = pd.DataFrame({'Makes': ['Acura', 'Audi', 'BMW','Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Fiat', 'Ford', 'GMC',
                                           'Honda', 'Hummer', 'Infiniti', 'Jaguar', 'Jeep', 'Land Rover', 'Lexus', 'Lincoln', 'Mazda', 'Mercury',
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
makes_list = df['Make'].unique()
# Sort the years list
sorted_makes = makes_list.sort()
# Show the sorted year list at the sidebar
selected_make = st.sidebar.selectbox('Make: ', (makes_list))

# Use the make selected by the user to select the url link w/ .xlsx file from the df containing the dataframes to each make
df_selected = dataframes_urls[dataframes_urls['Makes'] == selected_make]

# Loop to get the index from the dataframe where the url link is located 
for index in df_selected.index:
    # Store the index in a variable
    index_selected_df_url = index

# Filter the row with the url link based on the index and the column it is located
selected_url = df_selected.at[index_selected_df_url, 'URLs']

# Function to convert the url link to .xlsx file w/ the make/dataframe
def convert_url_to_xlsx(url_make):
    # Store the raw content from the url link into a variable
    get_url = requests.get(url_make)
    # Convert the url link to bytes
    get_content = get_url.content
    # Return the bytes content into .xlsx file
    return pd.read_excel(get_content)

# Call the function to convert the url link from the GitHub w/ the dataframe from the spefic make selected by the user, to .xlsx file
df_selected = convert_url_to_xlsx(selected_url)

# Get a unique list with the years avaiable on the df_make selected  
years = df_selected['Year'].unique()
# Sort the year list
sorted_years = sorted(years)
# Show the sorted years list at the sidebar
selected_year = st.sidebar.selectbox('Year: ', (sorted_years))

# Filter the df_make based on the year selected
df_filtered_after_year_selected = df_selected[df_selected['Year'] == selected_year]

# Get a unique list with models available based on the year selected
models = df_filtered_after_year_selected['Model']
# Sort the make list
sorted_models = sorted(models)
# Show the sorted makes list at the sidebar
selected_model = st.sidebar.selectbox('Model: ', (sorted_models))

# Filter the df_make based on the year selected to obtain the final dataframe
final_df = df_filtered_after_year_selected[df_filtered_after_year_selected['Model'] == selected_model]

# For an unknown reason the index from the main df appears, this drops it
final_df_dropped_column = final_df.drop(columns=['Unnamed: 0'])

# Loop to get the index from the final df based on the model selected
for index in final_df_dropped_column.index:
    # Store the index in a variable
    index_final_df_model_selected = index

# Get the data/values from the final df based on the index
row_final_df = final_df_dropped_column.iloc[0]

# Loop to get the column names from the final df
for column in final_df_dropped_column.columns:
    # Print the columns and their elements on the application
    st.write (f'''**:red[{column}:]** {row_final_df[column]}''')

# Def function to to convert the a raw url link from GitHub to an available PDF file for download
def convert_raw_url_to_download_file(make_procedure_url, make_procedure_message, make_procedure_button_label, make_procedure_file_name):
    # Requests the HTTP from the URL saved on GitHub
    response_make_procedure = requests.get(make_procedure_url)
    # Get the content from the url link
    content_make_procedure = response_make_procedure.content
    # Shows a message to the user
    st.write(make_procedure_message)
    # Set up the button to download the key relearn procedure
    st.download_button(
        # Button label
        label=make_procedure_button_label,
        # The data the file contains
        data=content_make_procedure,
        # File name after downloading
        file_name=make_procedure_file_name,
        mime='application/pdf'
    )

# Condition to check the column name where the key relearn procedure is located
if 'Security' in final_df_dropped_column.columns:
    # Loop through each row in the dataframe to check the key relearn name in the 'Security' column using part of the key relearn string 
    for index, row in final_df_dropped_column.iterrows():
        # Conditions to identify the Mazda key relearn procedures only through the last 2 characteres in the 'Security' column
        # If 'M-A' is found in 'Security', create the download button for Mazda M-A       
        if '-A' in row['Security']:  
            convert_raw_url_to_download_file(mazda_ma_url, mazda_ma_message, mazda_ma_button_label, mazda_ma_file_name)
        # If 'M-B' is found in 'Security', create the download button for Mazda M-B
        elif '-B' in row['Security']:
            convert_raw_url_to_download_file(mazda_mb_url, mazda_mb_message, mazda_mb_button_label, mazda_mb_file_name)
        # If 'M-C' is found in 'Security', create the download button for Mazda M-C
        elif '-C' in row['Security']:
            convert_raw_url_to_download_file(mazda_mc_url, mazda_mc_message, mazda_mc_button_label, mazda_mc_file_name)
        # If 'M-D' is found in 'Security', create the download button for Mazda M-D
        elif '-D' in row['Security']:
            convert_raw_url_to_download_file(mazda_md_url, mazda_md_message, mazda_md_button_label, mazda_md_file_name)
        # If 'M-E' is found in 'Security', create the download button for Mazda M-E
        elif '-E' in row['Security']:
            convert_raw_url_to_download_file(mazda_me_url, mazda_me_message, mazda_me_button_label, mazda_me_file_name)
        # If 'M-F' is found in 'Security', create the download button for Mazda M-F
        elif '-F' in row['Security']:
            convert_raw_url_to_download_file(mazda_mf_url, mazda_mf_message, mazda_mf_button_label, mazda_mf_file_name)
        # If 'M-G' is found in 'Security', create the download button for Mazda M-G
        elif '-G' in row['Security']:
            convert_raw_url_to_download_file(mazda_mg_url, mazda_mg_message, mazda_mg_button_label, mazda_mg_file_name)
        # If 'M-H' is found in 'Security', create the download button for Mazda M-H
        elif '-H' in row['Security']:
            convert_raw_url_to_download_file(mazda_mh_url, mazda_mh_message, mazda_mh_button_label, mazda_mh_file_name)
        # Some Mazda models are equipped with PATS security system from Ford. Therefore, the next conditions check if the 'Security' column contains PATS type
        # name and whether or not the parameter reset is required.
        # If 'Type B' is found in 'Security' and 'Parameter Reset Not Required' in 'ParameterReset', create the download button for Ford PATS Type B
        elif 'Type B' in row['Security'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)
        # If 'Type E' is found in 'Security' and 'Parameter Reset Not Required' in 'ParameterReset', create the download button for Ford PATS Type E
        elif 'Type E' in row['Security'] and 'Parameter Not Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_pats_e_url, ford_pats_e_message, ford_pats_e_button_label, ford_pats_e_file_name)
        # If 'Type G' is found in 'Security' and 'Parameter Reset Not Required' in 'ParameterReset', create the download button for Ford PATS Type G
        elif 'Type G' in row['Security'] and 'Parameter Not Reset Required' in row['ParameterReset'] :
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)      
        # Conditions to identify the CHEVROLET KEY RELEARN PROCEDURE only through the last 2 characteres in the 'Security' column
        # If 'PL' is found in 'Security', create the download button for Chevrolet Passlock
        elif 'PL' in row['Security']:
            convert_raw_url_to_download_file(gm_passlock_url, gm_passlock_message, gm_passlock_button_label, gm_passlock_file_name)
        # If 'PK1' is found in 'Security', create the download button for Chevrolet Passkey 2
        elif 'PK1' in row['Security']:
            convert_raw_url_to_download_file(gm_pk2_url, gm_pk2_message, gm_pk2_button_label, gm_pk2_file_name)
        # If 'PK2' is found in 'Security', create the download button for Chevrolet Passkey 2
        elif 'PK2' in row['Security']:
            convert_raw_url_to_download_file(gm_pk2_url, gm_pk2_message, gm_pk2_button_label, gm_pk2_file_name)
        # If 'PK' is found in 'Security', create the download button for Chevrolet Passkey 3
        elif 'PK3' in row['Security']:
            convert_raw_url_to_download_file(gm_pk3_url, gm_pk3_message, gm_pk3_button_label, gm_pk3_file_name)
# When the dataframe has the column 'PATS Type'. This condition applies to Ford, Lincoln and Mercury because only these 3 makes contains 
# the column 'PATS Type' in their dataframes  
else:
    # Loop through each row in the dataframe to check the key relearn name in the 'PATS Type' column using part of the key relearn string
    for index, row in final_df_dropped_column.iterrows():
        # If 'Type A' is found in 'PATS Type' and 'Parameter Reset Not Required' in 'ParameterReset', create the download button for Ford PATS Type A
        if 'Type A' in row['PATS Type'] and 'Parameter Reset Not Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_pats_a_url, ford_pats_a_message, ford_pats_a_button_label, ford_pats_a_file_name)
        # If 'Type A' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset BCFG
        elif 'Type A' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)
        # If 'Type B' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset BCFG
        elif 'Type B' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)
        # If 'Type C' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset C
        elif 'pe C' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_c_url, ford_parameter_reset_c_message, ford_parameter_reset_c_button_label, ford_parameter_reset_c_file_name)
        # If 'Type C' is found in 'PATS Type' and 'Parameter Not Reset Required' in 'ParameterReset', create the download button for Ford PATS Type A
        elif 'pe C' in row['PATS Type'] and 'Parameter Reset Not Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_pats_a_url, ford_pats_a_message, ford_pats_a_button_label, ford_pats_a_file_name)
        # If 'Type E' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset BCFG
        elif 'Type E' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)
        # If 'Type E' is found in 'PATS Type' and 'Parameter Not Reset Required' in 'ParameterReset', create the download button for Ford PATS Type E
        elif 'Type E' in row['PATS Type'] and 'Parameter Reset Not Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_pats_e_url, ford_pats_e_message, ford_pats_e_button_label, ford_pats_e_file_name)
        # If 'Type F' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset BCFG
        elif 'Type F' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)
        # If 'Type G' is found in 'PATS Type' and 'Parameter Reset Required' in 'ParameterReset', create the download button for Ford Parameter Reset BCFG
        elif 'Type G' in row['PATS Type'] and 'Parameter Reset Required' in row['ParameterReset']:
            convert_raw_url_to_download_file(ford_parameter_reset_bcfg_url, ford_parameter_reset_bcfg_message, ford_parameter_reset_bcfg_button_label, ford_parameter_reset_bcfg_file_name)



# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\src\Immo_Assistant.py'
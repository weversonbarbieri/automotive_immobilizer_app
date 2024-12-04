import streamlit as st
import pandas as pd

# Load the DataFrame and save it in the variable df.
df = pd.read_excel('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\data\year_make_model_df.xlsx')

# Converting all values in column Model to string, as some of models are numbers, for instance BMWs 318, 328, 525
df = df.astype({'Model':'string'})

# Load the dataframes of makes: Ford, Mercury, Lincoln, Mazda, Chevrolet, Pontiac, Cadillac, Buick, Oldsmobile, GMC, Saturn, Hummer
df_ford_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_ford_new.pkl')
df_lincoln_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_lincoln_updated.pkl')
df_mercury_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_mercury_updated.pkl')
df_mazda_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_mazda_updated.pkl')
df_chevrolet_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_chevy_filtered.pkl') 
df_pontiac_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_pontiac.pkl')
df_cadillac_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_cadillac.pkl')
df_buick_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_buick.pkl')
df_oldsmobile_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_oldsmobile.pkl')
df_gmc_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_gmc.pkl')
df_saturn_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_saturn.pkl')
df_hummer_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_hummer.pkl')
df_land_rover_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\\Python\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_land_rover_updated.pkl')
df_mini_st = pd.read_pickle('C:\\Language_Projects\\Language_Projects\Python\\Flagship_1\\Immo_Assistant.app\\dataframe_each_make_pkl_file\\df_mini_updated.pkl')
df_acura_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_acura_updated.pkl')
df_audi_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_audi_updated.pkl')
df_bmw_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_bmw_updated.pkl')
df_chrysler_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_chrysler_updated.pkl')
df_dodge_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_fiat_updated.pkl')
df_fiat_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_honda_updated.pkl')
df_honda_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_honda_updated.pkl')
df_infiniti_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_infiniti_up_to_dated.pkl')
df_jaguar_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_jaguar_up_to_dated.pkl')
df_jeep_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_jeep_updated.pkl')
df_lexus_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_lexus_updated.pkl')
df_mitsubishi_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_mitsubishi_upddated.pkl')
df_nissan_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_nissan_updated.pkl')
df_plymouth_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_plymouth_updated.pkl')
df_rolls_royce_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_rolls_royce_updated.pkl')
df_scion_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_scion_updated.pkl')
df_subaru_dt = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_subaru_updated.pkl')
df_toyota_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_toyota_updated.pkl')
df_vw_st = pd.read_pickle('C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\dataframe_each_make_pkl_file\df_vw_updated.pkl')

# Create a dictionary with the dataframes from each make
dataframes_each_make = {
                        'Ford': df_ford_st,
                        'Lincoln': df_lincoln_st,
                        'Mercury': df_mercury_st,
                        'Mazda': df_mazda_st,
                        'Chevrolet': df_chevrolet_st,
                        'Pontiac': df_pontiac_st,
                        'Cadillac': df_cadillac_st,
                        'Buick': df_buick_st,
                        'Oldsmobile': df_oldsmobile_st,
                        'GMC': df_gmc_st,
                        'Saturn': df_saturn_st,
                        'Hummer': df_hummer_st,
                        'Land Rover': df_land_rover_st,
                        'Mini': df_mini_st,
                        'Acura': df_acura_st,
                        'Audi': df_audi_st,
                        'BMW': df_bmw_st,
                        'Chrysler': df_chrysler_st,
                        'Dodge': df_dodge_st,
                        'Fiat': df_fiat_st,
                        'Honda': df_honda_st,
                        'Infiniti': df_infiniti_st,
                        'Jaguar': df_jaguar_st,
                        'Jeep': df_jeep_st,
                        'Land Rover': df_land_rover_st,
                        'Lexus': df_lexus_st,
                        'Mitsubishi': df_mitsubishi_st,
                        'Nissan': df_nissan_st,
                        'Plymouth': df_plymouth_st,
                        'Rolls-Royce': df_rolls_royce_st,
                        'Scion': df_scion_st,
                        'Subaru': df_subaru_dt,
                        'Toyota': df_toyota_st,
                        'Volkswagen': df_vw_st
}

# STREAMLIT CODE

# Sort and show the years in a sidebar
years = df['Year'].unique()
sorted_years = sorted(years)
selected_year = st.sidebar.selectbox('Year: ', (sorted_years))

# Same procedure with the makes
makes = df['Make'].unique()
sorted_makes = sorted(makes)
selected_make = st.sidebar.selectbox('Make: ', (sorted_makes))

filtered_model = dataframes_each_make.get(selected_make)
models = filtered_model['Model'].unique()
sorted_models = sorted(models)
selected_model = st.sidebar.selectbox('Model: ', (sorted_models))
final_df = filtered_model[(filtered_model['Year'] == selected_year) & (filtered_model['Model'] == selected_model)]
# st.write(final_df)


if not final_df.empty:
    row_final_df = final_df.iloc[0]
    for column in final_df.columns:
        st.write (f'''**:red[{column}:]** {row_final_df[column]}''')
else:
    st.write("Year/Make/Model not avaiable in the data base")


# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\src\Immo_Assistant.py'
import streamlit as st
import pandas as pd

# Load the DataFrame and save it in the variable df.
df = pd.read_excel('year_make_model_df.xlsx')

# Converting all values in column Model to string, as some of models are numbers, for instance BMWs 318, 328, 525
df = df.astype({'Model':'string'})

# Load the dataframes of makes: Ford, Mercury, Lincoln, Mazda, Chevrolet, Pontiac, Cadillac, Buick, Oldsmobile, GMC, Saturn, Hummer
df_ford_st = pd.read_pickle('df_ford_new.pkl')
df_lincoln_st = pd.read_pickle('df_lincoln_updated.pkl')
df_mercury_st = pd.read_pickle('df_mercury_updated.pkl')
df_mazda_st = pd.read_pickle('df_mazda_updated.pkl')
df_chevrolet_st = pd.read_pickle('df_chevy_filtered.pkl') 
df_pontiac_st = pd.read_pickle('df_pontiac.pkl')
df_cadillac_st = pd.read_pickle('df_cadillac.pkl')
df_buick_st = pd.read_pickle('df_buick.pkl')
df_oldsmobile_st = pd.read_pickle('df_oldsmobile.pkl')
df_gmc_st = pd.read_pickle('df_gmc.pkl')
df_saturn_st = pd.read_pickle('df_saturn.pkl')
df_hummer_st = pd.read_pickle('df_hummer.pkl')

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
                        'Hummer': df_hummer_st
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


# python -m streamlit run 'C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assistant.app\Immo_Assistant.py'
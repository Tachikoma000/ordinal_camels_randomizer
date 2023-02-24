import random
import streamlit as st
import pandas as pd

# Read the CSV files and extract the lists of OG wallets and Inscriptions IDs
og_wallets = list(pd.read_csv('og_wallets.csv')['Address'].astype(str))
inscriptions = list(pd.read_csv('inscriptions.csv')['Inscription #'].astype(str))

# Set the random seed for reproducibility
random.seed(42)

# Define the function to select 20 random OG wallets for Inscription IDs
def select_random_wallets_for_inscriptions():
    # Shuffle the OG wallets and Inscriptions IDs
    shuffled_wallets = random.sample(og_wallets, len(og_wallets))
    shuffled_inscriptions = random.sample(inscriptions, len(inscriptions))

    # Zip the shuffled OG wallets and Inscriptions IDs together
    shuffled_pairs = zip(shuffled_wallets, shuffled_inscriptions)

    # Select 20 random pairs of OG wallets and Inscriptions IDs
    selected_pairs = random.sample(list(shuffled_pairs), 20)

    # Return the selected pairs
    return selected_pairs

# Define the Streamlit app
def app():
    # Set the page title and description
    st.set_page_config(page_title="Ordinal Camel Allocator", page_icon=":money_with_wings:", layout="wide")
    st.title("Welcome to the Ordinal Camel Allocator")
    st.write("This app allocates an Ordinal Camel to an OG. Your Camel awaits you!")
        
    # Define a button to select 20 random OG wallets for Inscription IDs
    if st.button("Select 20 Random OG Wallets for Inscription IDs"):
        # Select 20 random OG wallets for Inscription IDs
        selected_pairs = select_random_wallets_for_inscriptions()
        
        # Create a dataframe of the selected OG wallets and Inscriptions IDs
        df = pd.DataFrame(selected_pairs, columns=["OG Wallet", "Inscription #"])
        
        # Display the dataframe
        st.subheader("Randomly Paired OG Wallets and Inscription IDs")
        st.write(df)

# Run the Streamlit app
if __name__ == '__main__':
    app()

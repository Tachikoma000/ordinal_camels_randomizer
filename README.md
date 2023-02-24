# ordinal_camels_randomizer
Simple pairing system to match OGs with an ordinal camel

This app generates a table of random pairs consisting of btc wallet addresses and inscription IDs. The app reads in two CSV files: one containing a list of wallet addresses ("og_wallets.csv") and another containing a list of inscription IDs ("inscriptions.csv").

Installation
To run this app, you will need to install Streamlit and pandas. You can do this by running the following command in your terminal:

`pip install streamlit pandas`

Usage
To use the app, simply run the following command in your terminal:

`streamlit run app.py`

Once the app is running, click the "Generate Pairs" button to generate a table of random pairs consisting of wallet addresses and inscription IDs. Each pair is selected randomly from the respective CSV file. The table will display 20 pairs by default, but you can modify this by changing the argument passed to the generate_pairs function.

Note: The CSV files included with this code are not real addresses or inscriptions and should be used only to understand how the code works. For real use, you should fork the code and replace the fake CSV files with real ones.

Files
app.py: The main Streamlit app.
og_wallets.csv: A CSV file containing a list of wallet addresses.
inscriptions.csv: A CSV file containing a list of inscription IDs.



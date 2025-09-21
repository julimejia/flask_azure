from flask import Flask, jsonify
import pandas as pd 

app =  Flask('my_azure_app')


@app.route('/api/v1/report', methods=['GET'] )
def get_report():
 df_final_data = pd.read_csv('./data/final_data.csv')
 json_data = df_final_data.to_json(orient='records')
 return json_data
from crypt import methods
import os
import pickle
import pandas as pd
from flask import Flask, request, Response
from pcrcovidtester import PCRCovidTesterNIR

# loading model
model = pickle.load( open( 'model/Logistic_Model.pkl','rb' ) )

# initialize API
app = Flask( __name__ )

@app.route( '/predict', methods=['POST'] )
def healthinsurance_predict():
    test_json = request.get_json()
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique exemple
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple exemples
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
        
        # Instantiate PCRCovidTesterNIR Class
        pipeline = PCRCovidTesterNIR()
        
        # data cleaning
        df = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df = pipeline.feature_engineering( df )
        
        # data preparation
        df = pipeline.data_preparation( df )
        
        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df )
        
        return df_response
        
    else:
        return Response( '{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( '0.0.0.0', port=port )
import pickle
import pandas as pd
import numpy as np

class PCRCovidTesterNIR( object ):
  def __init__( self ):
    self.home_path = ''
    self.scaler_879 = pickle.load( open( self.home_path + 'scaler_879.pkl','rb' ) )
    self.scaler_875 = pickle.load( open( self.home_path + 'scaler_875.pkl','rb' ) )
    self.scaler_851 = pickle.load( open( self.home_path + 'scaler_851.pkl','rb' ) )
    self.scaler_878 = pickle.load( open( self.home_path + 'scaler_878.pkl','rb' ) )
    self.scaler_877 = pickle.load( open( self.home_path + 'scaler_877.pkl','rb' ) )
    self.scaler_816 = pickle.load( open( self.home_path + 'scaler_816.pkl','rb' ) )
    self.scaler_880 = pickle.load( open( self.home_path + 'scaler_880.pkl','rb' ) )
    self.scaler_873 = pickle.load( open( self.home_path + 'scaler_873.pkl','rb' ) )
    self.scaler_675 = pickle.load( open( self.home_path + 'scaler_675.pkl','rb' ) )
    self.scaler_662 = pickle.load( open( self.home_path + 'scaler_662.pkl','rb' ) )
    self.scaler_876 = pickle.load( open( self.home_path + 'scaler_876.pkl','rb' ) )
    self.scaler_874 = pickle.load( open( self.home_path + 'scaler_874.pkl','rb' ) )
    self.scaler_676 = pickle.load( open( self.home_path + 'scaler_676.pkl','rb' ) )
    self.scaler_661 = pickle.load( open( self.home_path + 'scaler_661.pkl','rb' ) )
    self.scaler_781 = pickle.load( open( self.home_path + 'scaler_781.pkl','rb' ) )
    self.scaler_674 = pickle.load( open( self.home_path + 'scaler_674.pkl','rb' ) )
    self.scaler_881 = pickle.load( open( self.home_path + 'scaler_881.pkl','rb' ) )
    self.scaler_835 = pickle.load( open( self.home_path + 'scaler_835.pkl','rb' ) )
    self.scaler_832 = pickle.load( open( self.home_path + 'scaler_832.pkl','rb' ) )
    self.scaler_764 = pickle.load( open( self.home_path + 'scaler_764.pkl','rb' ) )
    self.scaler_677 = pickle.load( open( self.home_path + 'scaler_677.pkl','rb' ) )
    
    
  def data_cleaning( self, df ):
    df = df
    return df

  def feature_engineering( self, df ):
    # Replacing "," to "."
    for i in range ( df.shape[1] ):
      df[i] = df[i].apply( lambda x: x.replace( ',', '.' ) )

    # Converting Target Variable to 0 and 1
    # Control = 0, Covid = 1
    df[0] = df[0].apply( lambda x: 0 if x == 'Control' else 1 )

    # Transform float (exclude = df[0])
    for i in range ( df.shape[1] - 1 ):
      df[i+1] = df[i+1].astype( 'float64' )

    return df

  def data_preparation( self, df ):
    # 879
    df[879] = self.scaler_879.transform( df[[879]].values )

    # 875
    df[875] = self.scaler_875.transform( df[[875]].values )

    # 851
    df[851] = self.scaler_851.transform( df[[851]].values )

    # 878
    df[878] = self.scaler_878.transform( df[[878]].values )

    # 877
    df[877] = self.scaler_877.transform( df[[877]].values )

    # 816
    df[816] = self.scaler_816.transform( df[[816]].values )

    # 880
    df[880] = self.scaler_880.transform( df[[880]].values )

    # 873
    df[873] = self.scaler_879.transform( df[[873]].values )

    # 675
    df[675] = self.scaler_675.transform( df[[675]].values )

    # 662
    df[662] = self.scaler_662.transform( df[[662]].values )

    # 876
    df[876] = self.scaler_876.transform( df[[876]].values )

    # 874
    df[874] = self.scaler_874.transform( df[[874]].values )

    # 676
    df[676] = self.scaler_676.transform( df[[676]].values )

    # 661
    df[661] = self.scaler_661.transform( df[[661]].values )

    # 781
    df[781] = self.scaler_781.transform( df[[781]].values )

    # 674
    df[674] = self.scaler_674.transform( df[[674]].values )

    # 881
    df[881] = self.scaler_881.transform( df[[881]].values )

    # 835
    df[835] = self.scaler_835.transform( df[[835]].values )

    # 832
    df[832] = self.scaler_832.transform( df[[832]].values )

    # 764
    df[764] = self.scaler_764.transform( df[[764]].values )

    # 677
    df[677] = self.scaler_677.transform( df[[677]].values )
    
    return df[879, 875, 851, 878, 877, 816, 880, 873, 675, 662, 876, 874, 676, 661, 781, 674, 881, 835, 832, 764, 677]
    
  def get_prediction( self, model, original_data, test_data ):
    # model prediction
    pred = model.predict( test_data )

    # join prediction into original_data
    original_data['target_predict'] = pred.tolist()

    # define threshold if necessary
    # self.threshold = lambda x: 0 if x < 0.33 else original_data['target_predict']
    # original_data.loc[:, 'target_predict'] = original_data['target_predict'].map( self.threshold )
    
    # sort_values
    original_data = original_data.sort_values( 'target_predict', ascending = False )

    return original_data.to_json( orient='records', data_format='iso')
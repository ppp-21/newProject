import pandas as pd
import numpy as np
import pickle
import json
import config

class Houseprd:
    def __init__(self):
        print("init functin")
    
    def load_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)
        with open(config.JSON_FILE_PATH,'r') as f:
            self.column_names=json.load(f)['Columns']
    
    def get_location_names(self):
        self.load_data()
        
        locations = self.column_names[3:]
        loc=[]
        for i in locations:
            l1=i.split("_")
            loc.append(l1[1])
        print("locations :",loc)

        return loc

    def get_house_price(self,location,total_sqft,bath,BHK):
        self.load_data()
        test_array = np.zeros(self.model.n_features_in_,int)
        
        index = self.column_names.index(location)
        #location = 'location_'+ 'Anandapura'
        
        
        test_array[0] = BHK
        test_array[1] = total_sqft
        test_array[2] = bath
        test_array[index] = 1

        price = np.around(self.model.predict([test_array])[0],2)
        print(f'Predicted House Price is: {price} Lakhs')
    
        return price


if __name__ == "__main__":
    hp = Houseprd()
    hp.get_location_names()
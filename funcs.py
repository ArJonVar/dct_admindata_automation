#region imports
import smartsheet
from smartsheet.exceptions import ApiError
from smartsheet_grid import grid
import requests
import json
import time
from globals import smartsheet_token
from logger import ghetto_logger
import datetime
#endregion

class NewClass():
    '''Explain Class'''
    def __init__(self, config):
        self.config = config
        self.smartsheet_token=config.get('smartsheet_token')
        self.sheet_id=config.get("sheet_id")
        grid.token=smartsheet_token
        self.smart = smartsheet.Smartsheet(access_token=self.smartsheet_token)
        self.smart.errors_as_exceptions(True)
        self.log=ghetto_logger("funcs.py")
        self.now = datetime.datetime.now()
    
    def export_sheet(self, file_path):
        '''grabs sheet w/id, and exports it to path'''
        sheet = grid(self.sheet_id)
        sheet.fetch_content()
        sheet.df.to_excel(file_path, index=False)
    
    def format_datename(self):
        '''formats the date name coby wanted'''

    def run(self):
        '''runs main script as intended'''
        self.log.log('ran script')
        self.export_sheet(r'Z:\Shared\Digital Construction Team\03_DCT Admin\Historical Data\Projects_&_Planning_Data\_' + f'{self.now.strftime("%Y.%m.%d.%H.%S")}_dct-p&p.xlsx')

if __name__ == "__main__":
    config = {
        'smartsheet_token':smartsheet_token,
        'sheet_id':2789557075765124
    }
    nc = NewClass(config)
    nc.run()
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:58:38 2020

@author: vijay

See https://github.com/philipperemy/FX-1-Minute-Data
"""

from histdata import download_hist_data as dl
from histdata.api import Platform as P, TimeFrame as TF


dl = dl(year='2019', pair='eurusd', platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
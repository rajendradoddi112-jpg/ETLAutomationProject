import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal

def test_duplicates():
    target_csv=pd.read_csv("c:/DataFiles/employee_src.txt")
    duplicate_count=target_csv.duplicated().sum()
    assert duplicate_count==0 , "Duplicates found -please verify target"
    print(duplicate_count)


def test_datacompleteness():
    target_csv=pd.read_csv("c:/DataFiles/employee_src.txt")
    assert not target_csv.empty ,"Target is no data-Please verify"
    print(target_csv)

def test_nullcheck():
    target_csv=pd.read_csv("c:/DataFiles/employee_src.txt")
    isemployeenonull=target_csv["employee_id"].isnull().any()
    assert isemployeenonull==True , "Nulls are present in employeeid"
    print(isemployeenonull)

def test_hike(source_data,target_data):
    # source_csv=pd.read_csv("c:/DataFiles/employee_src.txt")
    hike=source_data["salary"]*0.10
    source_df=hike.to_frame()
    source_df.rename(columns={"salary":"hike"},inplace=True)
    #target_csv=pd.read_csv("c:/DataFiles/employee_tgt.txt")
    hike_tgt=target_data["hike"]
    target_df=hike_tgt.to_frame()
    assert_frame_equal(source_df,target_df), "hike are not matching from source to target"
    print(source_df)
    print(target_df)
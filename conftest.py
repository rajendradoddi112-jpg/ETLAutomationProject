from datetime import datetime
import os
import pandas as pd
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir="reports"
    os.makedirs(report_dir,exist_ok=True)
    now=datetime.now().strftime("%D-%M-%Y %H-%M-%S")
    config.option.htmlpath=f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="module")
def source_data():
    source_data=pd.read_csv("c:/DataFiles/employee_src.txt")
    return source_data

@pytest.fixture(scope="module")
def target_data():
    target_data=pd.read_csv("c:/DataFiles/employee_tgt.txt")
    return target_data

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("\nStarted")
    yield
    print("\nEnd")
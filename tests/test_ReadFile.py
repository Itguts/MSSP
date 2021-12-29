import pandas as pd
import pytest

df_Actual = pd.read_csv('data/TestResult_Actual.csv')
df_Expected = pd.read_csv('BlobFile/TestResult_Expected.csv')


def test_TotalRowCount():
	assert ((df_Actual.loc[df_Actual.TestName=='TotalCount', 'ActualValue'] == df_Expected.loc[df_Expected.TestName=='TotalCount', 'ExpectedValue']).values[0])
 
 
def test_MemberCount():
	assert ((df_Actual.loc[df_Actual.TestName=='MemberCount', 'ActualValue'] == df_Expected.loc[df_Expected.TestName=='MemberCount', 'ExpectedValue']).values[0])
 
def test_TotalClaimlines():
    	assert ((df_Actual.loc[df_Actual.TestName=='TotalClaimlines', 'ActualValue'] == df_Expected.loc[df_Expected.TestName=='TotalClaimlines', 'ExpectedValue']).values[0])
 
 
def test_TotalPaidAmount():
	assert ((df_Actual.loc[df_Actual.TestName=='TotalPaidAmount', 'ActualValue'] == df_Expected.loc[df_Expected.TestName=='TotalPaidAmount', 'ExpectedValue']).values[0])
 
 
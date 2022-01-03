-- Databricks notebook source
--Write cliams ETL
--Select 1

-- COMMAND ----------

--Deleteting testnames
delete from default.testresult where TestName in ('TotalClaimlines','TotalPaidAmount')

-- COMMAND ----------

--Insert test result into default.testresult table
Insert into default.testresult values('TotalClaimlines', 3456)

-- COMMAND ----------

--Insert test result into default.testresult table
Insert into default.testresult values('TotalPaidAmount', 12345)

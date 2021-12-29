-- Databricks notebook source
--Write etl

-- COMMAND ----------

--Deleteting testnames
delete from default.testresult where TestName in ('TotalCount','MemberCount')



-- COMMAND ----------

--Insert test result into default.testresult table
Insert into default.testresult values('TotalCount', 100)

-- COMMAND ----------

--Insert test result into default.testresult table
Insert into default.testresult values('MemberCount', 200)

-- COMMAND ----------



-- Databricks notebook source
-- MAGIC %md
-- MAGIC # General Social Survey
-- MAGIC ### Essential variables exploration
-- MAGIC 
-- MAGIC This notebook look at the [General Social Survey](https://gss.norc.org/) (GSS), exploring essential variables in the over the 50+ years of survey data. The primary data file for this exploration (gss7221_r
-- MAGIC j2.dta) can be found in the [GSS Strata archive](https://gss.norc.org/documents/stata/GSS_stata.zip). If you want to work with this data for your own analysis, it is also essential to review the survey [codebooks](https://gss.norc.org/Get-Documentation).
-- MAGIC 
-- MAGIC Special thanks to [Allen Downey](https://github.com/AllenDowney) for all the work they have published on crafting jupyter notebooks with GSS data.
-- MAGIC 
-- MAGIC This notebook is part of the [GeneralSocialSurvey](https://github.com/CulleyHarrelson/GeneralSocialSurvey) github repository.

-- COMMAND ----------


-- Returns label for wrkstat variable
CREATE OR REPLACE FUNCTION work_status(wrkstat INT) RETURNS STRING RETURN
  CASE wrkstat
  WHEN 1 THEN 'Working full time'
  WHEN 2 THEN 'Working part time'
  WHEN 3 THEN 'Temp Unemployed'
  WHEN 4 THEN 'Unemployed'
  WHEN 5 THEN 'Retired'
  WHEN 6 THEN 'In school'
  WHEN 7 THEN 'Keeping house'
  WHEN 8 THEN 'Other'
  ELSE NULL
END;

-- Returns label for childs variable
CREATE OR REPLACE FUNCTION number_of_children(childs INT) RETURNS STRING RETURN
  CASE childs
  WHEN 0 THEN 'None'
  WHEN 1 THEN 'One'
  WHEN 2 THEN 'Two'
  WHEN 3 THEN 'Three'
  WHEN 4 THEN 'Four'
  WHEN 5 THEN 'Five'
  WHEN 6 THEN 'Six'
  WHEN 7 THEN 'Seven'
  WHEN 8 THEN 'Eight or more'
  ELSE NULL
END;


-- Returns label for sex variable
CREATE OR REPLACE FUNCTION sex_label(sex INT) RETURNS STRING RETURN
  CASE sex
  WHEN 2 THEN 'Female'
  WHEN 1 THEN 'Male'
  ELSE NULL
END;

          

-- COMMAND ----------


SELECT
  work_status(wrkstat) as work_status,
  age,
  count(wrkstat)
FROM
  gss.raw_survey_latest
GROUP BY
  work_status(wrkstat),
  age
HAVING count(wrkstat) > 0

-- COMMAND ----------


SELECT
  number_of_children(childs) AS number_of_children,
  count(childs)
FROM
  gss.raw_survey_latest
GROUP BY
  number_of_children(childs)

-- COMMAND ----------


SELECT
  educ
FROM
  gss.raw_survey_latest
  

-- COMMAND ----------


SELECT
  sex_label(sex) AS sex,
  count(sex)
FROM
  gss.raw_survey_latest
GROUP BY sex_label(sex)

start_date = '20200905'
end_date = str(int(start_date)+6)
start_date_2 = str(int(start_date)+2)
start_date_4 = str(int(start_date)+4)
start_date_6 = str(int(start_date)+6)
start_date_7 = str(int(start_date)+7)
start_date_8 = str(int(start_date)+8)
start_date_9 = str(int(start_date)+9)
start_date_13 = str(int(start_date)+13)
sql_string = f'''# 流失用户（准确）

CREATE TABLE tmp.churn_1009
WITH (
  format='PARQUET'
) AS

WITH sample AS (SELECT DISTINCT month||day AS day, gaid, country
FROM ads.newuser
WHERE appid = 223 AND month||day BETWEEN \'{start_date}\' AND \'{start_date}\'
AND gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') AND country != 'CN'),

two_hour AS (SELECT DISTINCT t1.gaid
FROM basic_stats.firebase_events AS t1
INNER JOIN sample AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{end_date}\' AND t1.ec = 'user_engagement' 
GROUP BY t1.gaid
HAVING SUM(try_cast(t1.info AS bigint))>5400000),
           
more_then_7day AS (SELECT DISTINCT gaid
FROM basic_stats.firebase_events 
WHERE appid = 223 AND month||day BETWEEN \'{start_date_7}\' AND \'{start_date_13}\' AND ec IN ('level_start', 'earn_virtual_currency' ,'session_start')),

churn AS (SELECT t1.gaid
FROM two_hour AS t1
LEFT JOIN more_then_7day AS t2
ON t1.gaid = t2.gaid
WHERE t2.gaid IS NULL),


churn_updated AS (SELECT DISTINCT t1.gaid
FROM basic_stats.firebase_events AS t1
INNER JOIN churn AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date}\' 
AND t1.ec = 'level_up' AND t1.ext like 'L0002%') 

SELECT DISTINCT t1.gaid, MIN(t1.event_ts) AS start_ts
FROM basic_stats.firebase_events AS t1
RIGHT JOIN churn_updated AS t2   
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date}\'AND t1.ec = 'session_start' 
GROUP BY t1.gaid


# 留存用户（准确）
CREATE TABLE tmp.retained_1009
WITH (
  format='PARQUET'
) AS
WITH sample AS (SELECT DISTINCT month||day AS day, gaid, country
FROM ads.newuser
WHERE appid = 223 AND month||day BETWEEN \'{start_date}\' AND \'{start_date}\'
AND gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') AND country != 'CN'),

long_term_temp AS (SELECT DISTINCT gaid,num FROM (SELECT DISTINCT t1.gaid, 
CASE WHEN t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date_2}\' THEN 1 
WHEN  t1.month||t1.day BETWEEN \'{start_date_2}\' AND \'{start_date_4}\'  THEN 2 
WHEN  t1.month||t1.day BETWEEN \'{start_date_4}\' AND \'{start_date_6}\'  THEN 3
WHEN  t1.month||t1.day BETWEEN \'{start_date_6}\' AND \'{start_date_8}\'  THEN 4
WHEN  t1.month||t1.day BETWEEN \'{start_date_8}\' AND \'{start_date_9}\'  THEN 5 END AS num
FROM basic_stats.firebase_events AS t1
INNER JOIN sample AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date_9}\' AND t1.ec = 'user_engagement'  AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
UNION ALL
SELECT DISTINCT t1.gaid, 
CASE 
WHEN  t1.month||t1.day =\' {start_date_2}\' THEN 2 
WHEN  t1.month||t1.day = \'{start_date_4}\'THEN 3
WHEN  t1.month||t1.day = \'{start_date_6}\' THEN 4
WHEN  t1.month||t1.day = \'{start_date_8}\'  THEN 5 END AS num
FROM basic_stats.firebase_events AS t1
INNER JOIN sample AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date_9}\' AND t1.ec = 'user_engagement' AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') )),


long_term_user AS (SELECT gaid, SUM(num) AS total
FROM long_term_temp
GROUP BY gaid
HAVING SUM(num) = 15),

long_term_updated AS (SELECT DISTINCT t1.gaid
FROM basic_stats.firebase_events AS t1
INNER JOIN long_term_user AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date}\' 
AND t1.ec = 'level_up' AND t1.ext like 'L0002%') 

SELECT DISTINCT t1.gaid, MIN(t1.event_ts) AS start_ts
FROM basic_stats.firebase_events AS t1
RIGHT JOIN long_term_updated AS t2   
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN \'{start_date}\' AND \'{start_date}\' AND t1.ec = 'session_start' 
GROUP BY t1.gaid
'''.format()


print(sql_string)


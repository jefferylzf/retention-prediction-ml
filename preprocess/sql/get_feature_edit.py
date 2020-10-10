sql_string = '''WITH level1 AS 
(SELECT t1.gaid, COUNT(*) AS level_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'level_up' AND t1.ext like 'L%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t1.gaid),

level2 AS 
(SELECT t1.gaid, COUNT(*) AS level_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'level_up' AND t1.ext like 'L%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

level3 AS 
(SELECT t1.gaid, COUNT(*) AS level_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'level_up' AND t1.ext like 'L%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),


ads1 AS (SELECT t1.gaid, COUNT(*) AS ads_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'm_ad_impression' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

ads2 AS (SELECT t1.gaid, COUNT(*) AS ads_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'm_ad_impression' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

ads3 AS (SELECT t1.gaid, COUNT(*) AS ads_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'm_ad_impression' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



pvp1 AS (SELECT t2.gaid, COUNT(*) AS pvp_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),

pvp2 AS (SELECT t2.gaid, COUNT(*) AS pvp_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),

pvp3 AS (SELECT t2.gaid, COUNT(*) AS pvp_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),



pvp_won1 AS (SELECT t2.gaid, COUNT(split_part(ext,'@',1)='1') AS pvp_won_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),

pvp_won2 AS (SELECT t2.gaid, COUNT(split_part(ext,'@',1)='1') AS pvp_won_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),

pvp_won3 AS (SELECT t2.gaid, COUNT(split_part(ext,'@',1)='1') AS pvp_won_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'arena_finish' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t2.gaid),



gem1 AS (SELECT t1.gaid, sum(t1.amount) AS gem_spend1
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts/1000 + 86400 AND t1.ec = 'gem_spend'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

gem2 AS (SELECT t1.gaid, sum(t1.amount) AS gem_spend2
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts/1000 + 86400 AND t1.event_ts <= t2.start_ts/1000 + 172800  AND t1.ec = 'gem_spend'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),


gem3 AS (SELECT t1.gaid, sum(t1.amount) AS gem_spend3
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts/1000 + 172800 AND t1.event_ts <= t2.start_ts/1000 + 259200  AND t1.ec = 'gem_spend'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



coin1 AS (SELECT t1.gaid, sum(t1.amount) AS coin_spend1
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts/1000 + 86400 AND t1.ec = 'coin_spend' AND 
 t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t1.gaid),

coin2 AS (SELECT t1.gaid, sum(t1.amount) AS coin_spend2
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts/1000 + 86400 AND t1.event_ts <= t2.start_ts/1000 + 172800  AND t1.ec = 'coin_spend' AND 
 t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t1.gaid),

coin3 AS (SELECT t1.gaid, sum(t1.amount) AS coin_spend3
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts/1000 + 172800 AND t1.event_ts <= t2.start_ts/1000 + 259200  AND t1.ec = 'coin_spend' AND 
 t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t1.gaid),



gem_earning1 AS (SELECT t1.gaid, sum(t1.amount) AS gem_earn1
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts/1000 + 86400 AND t1.ec = 'gem_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

gem_earning2 AS (SELECT t1.gaid, sum(t1.amount) AS gem_earn2
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts/1000 + 86400 AND t1.event_ts <= t2.start_ts/1000 + 172800  AND t1.ec = 'gem_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

gem_earning3 AS (SELECT t1.gaid, sum(t1.amount) AS gem_earn3
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts/1000 + 172800 AND t1.event_ts <= t2.start_ts/1000 + 259200  AND t1.ec = 'gem_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



ads_reward1 AS (SELECT t1.gaid, COUNT(*) AS ads_reward_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000
AND t1.ec = 'ad_reward'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY  t1.gaid),

ads_reward2 AS (SELECT t1.gaid, COUNT(*) AS ads_reward_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000 
AND t1.ec = 'ad_reward'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY  t1.gaid),

ads_reward3 AS (SELECT t1.gaid, COUNT(*) AS ads_reward_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000 
AND t1.ec = 'ad_reward'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY  t1.gaid),



hero1 AS (SELECT t2.gaid, COUNT(*) AS org_hero_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'hero_acq' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') AND SPLIT_PART(ext,'@',2) in ('10601','10801','10901','11301','11401','11501','11701','11801','11901','12601','12701','12801','12901','13001','13101','13201','13301','13401','13501')
GROUP BY t2.gaid),

hero2 AS (SELECT t2.gaid, COUNT(*) AS org_hero_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'hero_acq' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') AND SPLIT_PART(ext,'@',2) in ('10601','10801','10901','11301','11401','11501','11701','11801','11901','12601','12701','12801','12901','13001','13101','13201','13301','13401','13501')
GROUP BY t2.gaid),

hero3 AS (SELECT t2.gaid, COUNT(*) AS org_hero_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'hero_acq' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') AND SPLIT_PART(ext,'@',2) in ('10601','10801','10901','11301','11401','11501','11701','11801','11901','12601','12701','12801','12901','13001','13101','13201','13301','13401','13501')
GROUP BY t2.gaid),



level_e_try1 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_try_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'level_start' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

level_e_try2 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_try_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'level_start' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

level_e_try3 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_try_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'level_start' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



level_e1 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'level_up' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

level_e2 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'level_up' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

level_e3 AS 
(SELECT t1.gaid, COUNT(*) AS level_e_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'level_up' AND t1.ext like 'E%' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



idle1 AS (SELECT t1.gaid, count(*) AS idle_cnt1
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts/1000 + 86400 AND t1.ec = 'coin_earn' AND reason = 'idle'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

idle2 AS (SELECT t1.gaid, count(*) AS idle_cnt2
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts/1000 + 86400 AND t1.event_ts <= t2.start_ts/1000 + 172800  AND t1.ec = 'coin_earn' AND reason = 'idle'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

idle3 AS (SELECT t1.gaid, count(*) AS idle_cnt3
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts/1000 + 172800 AND t1.event_ts <= t2.start_ts/1000 + 259200  AND t1.ec = 'coin_earn' AND reason = 'idle'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



purchase1 AS (SELECT t2.gaid, COUNT(*) AS purchase_times1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'purchase_ok' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),

purchase2 AS (SELECT t2.gaid, COUNT(*) AS purchase_times2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'purchase_ok' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),

purchase3 AS (SELECT t2.gaid, COUNT(*) AS purchase_times3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'purchase_ok' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),



login1 AS (SELECT t2.gaid, COUNT(*) AS login_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'login' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),

login2 AS (SELECT t2.gaid, COUNT(*) AS login_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'login' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),

login3 AS (SELECT t2.gaid, COUNT(*) AS login_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'login' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000') 
GROUP BY t2.gaid),


headhunt1 AS 
(SELECT t1.gaid, COUNT(*)/2 AS level_h_cnt1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'level_start' AND (t1.ext like 'C%' OR t1.ext like 'S%') 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

headhunt2 AS 
(SELECT t1.gaid, COUNT(*)/2 AS level_h_cnt2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'level_start' AND (t1.ext like 'C%' OR t1.ext like 'S%') 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

headhunt3 AS 
(SELECT t1.gaid, COUNT(*)/2 AS level_h_cnt3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'level_start' AND (t1.ext like 'C%' OR t1.ext like 'S%') 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



logs1 AS 
(SELECT t1.gaid, COUNT(*) AS log_num1
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

logs2 AS 
(SELECT t1.gaid, COUNT(*) AS log_num2
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

logs3 AS 
(SELECT t1.gaid, COUNT(*) AS log_num3
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),



d1 AS (SELECT t1.gaid,SUM(try_cast(t1.info AS bigint)) AS d1_duration
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts + 86400000 AND t1.ec = 'user_engagement' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

d2 AS (SELECT t1.gaid,SUM(try_cast(t1.info AS bigint)) AS d2_duration
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts + 86400000 AND t1.event_ts <= t2.start_ts + 172800000  AND t1.ec = 'user_engagement' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

d3 AS (SELECT t1.gaid,SUM(try_cast(t1.info AS bigint)) AS d3_duration
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts + 172800000 AND t1.event_ts <= t2.start_ts + 259200000  AND t1.ec = 'user_engagement' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

will_pay AS (SELECT DISTINCT t1.gaid,count(*) AS willpay
FROM basic_stats.firebase_events AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200812' AND ec = 'will_pay' 
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

daily_task1 AS (SELECT t1.gaid, COUNT(*) AS daily_task_cnt1
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200810' AND '20200811' AND t1.event_ts <= t2.start_ts/1000 + 86400 AND t1.reason = 'daily_task_finish' AND ec = 'coin_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

daily_task2 AS (SELECT t1.gaid, COUNT(*) AS daily_task_cnt2
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200811' AND '20200812' AND t1.event_ts > t2.start_ts/1000 + 86400 AND t1.event_ts <= t2.start_ts/1000 + 172800  AND t1.reason = 'daily_task_finish' AND ec = 'coin_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid),

daily_task3 AS (SELECT t1.gaid, COUNT(*) AS daily_task_cnt3
FROM basic_stats.items_change AS t1
INNER JOIN retained_0810 AS t2
ON t1.gaid = t2.gaid 
WHERE t1.appid = 223 AND t1.month||t1.day BETWEEN '20200812' AND '20200813' AND t1.event_ts > t2.start_ts/1000 + 172800 AND t1.event_ts <= t2.start_ts/1000 + 259200  AND t1.reason = 'daily_task_finish' AND ec = 'coin_earn'
AND t1.gaid NOT IN ('','null','00000000-0000-0000-0000-000000000000')
GROUP BY t1.gaid)


SELECT t1.gaid, t1.level_cnt1, t2.ads_cnt1,t3.pvp_cnt1, t4.pvp_won_cnt1, t5.gem_spend1, t6.coin_spend1, t7.gem_earn1, t8.ads_reward_cnt1, t9.org_hero_cnt1, t10.level_e_try_cnt1, t11.level_e_cnt1, t12.idle_cnt1, t13.purchase_times1, t14.login_cnt1, t15.level_h_cnt1, t16.log_num1, d1.d1_duration, d2.d2_duration, d3.d3_duration, t17.willpay, t18.daily_task_cnt1,


t21.level_cnt2, t22.ads_cnt2,t23.pvp_cnt2, t24.pvp_won_cnt2, t25.gem_spend2, t26.coin_spend2, t27.gem_earn2, t28.ads_reward_cnt2, t29.org_hero_cnt2, t210.level_e_try_cnt2, t211.level_e_cnt2, t212.idle_cnt2, t213.purchase_times2, t214.login_cnt2, t215.level_h_cnt2, t216.log_num2, t218.daily_task_cnt2,

t31.level_cnt3, t32.ads_cnt3,t33.pvp_cnt3, t34.pvp_won_cnt3, t35.gem_spend3, t36.coin_spend3, t37.gem_earn3, t38.ads_reward_cnt3, t39.org_hero_cnt3, t310.level_e_try_cnt3, t311.level_e_cnt3, t312.idle_cnt3, t313.purchase_times3, t314.login_cnt3, t315.level_h_cnt3, t316.log_num3, t318.daily_task_cnt3


FROM level1 AS t1
LEFT JOIN ads1 AS t2
ON t1.gaid = t2.gaid 
LEFT JOIN pvp1 AS t3
ON t1.gaid = t3.gaid 
LEFT JOIN pvp_won1 AS t4
ON t1.gaid = t4.gaid 
LEFT JOIN gem1 AS t5
ON t1.gaid = t5.gaid 
LEFT JOIN coin1 AS t6
ON t1.gaid = t6.gaid 
LEFT JOIN gem_earning1 AS t7
ON t1.gaid = t7.gaid 
LEFT JOIN ads_reward1 AS t8
ON t1.gaid = t8.gaid 
LEFT JOIN hero1 AS t9
ON t1.gaid = t9.gaid 
LEFT JOIN level_e_try1 AS t10
ON t1.gaid = t10.gaid 
LEFT JOIN level_e1 AS t11
ON t1.gaid = t11.gaid 
LEFT JOIN idle1 AS t12
ON t1.gaid = t12.gaid 
LEFT JOIN purchase1 AS t13
ON t1.gaid = t13.gaid 
LEFT JOIN login1 AS t14
ON t1.gaid = t14.gaid 
LEFT JOIN headhunt1 AS t15
ON t1.gaid = t15.gaid 
LEFT JOIN logs1 AS t16
ON t1.gaid = t16.gaid
LEFT JOIN daily_task1 AS t18
ON t1.gaid = t18.gaid

LEFT JOIN  level2 AS t21
ON t1.gaid = t21.gaid
LEFT JOIN ads2 AS t22
ON t1.gaid = t22.gaid 
LEFT JOIN pvp2 AS t23
ON t1.gaid = t23.gaid 
LEFT JOIN pvp_won2 AS t24
ON t1.gaid = t24.gaid 
LEFT JOIN gem2 AS t25
ON t1.gaid = t25.gaid 
LEFT JOIN coin2 AS t26
ON t1.gaid = t26.gaid 
LEFT JOIN gem_earning2 AS t27
ON t1.gaid = t27.gaid 
LEFT JOIN ads_reward2 AS t28
ON t1.gaid = t28.gaid 
LEFT JOIN hero2 AS t29
ON t1.gaid = t29.gaid 
LEFT JOIN level_e_try2 AS t210
ON t1.gaid = t210.gaid 
LEFT JOIN level_e2 AS t211
ON t1.gaid = t211.gaid 
LEFT JOIN idle2 AS t212
ON t1.gaid = t212.gaid 
LEFT JOIN purchase2 AS t213
ON t1.gaid = t213.gaid 
LEFT JOIN login2 AS t214
ON t1.gaid = t214.gaid 
LEFT JOIN headhunt2 AS t215
ON t1.gaid = t215.gaid 
LEFT JOIN logs2 AS t216
ON t1.gaid = t216.gaid
LEFT JOIN daily_task2 AS t218
ON t1.gaid = t218.gaid

LEFT JOIN  level3 AS t31
ON t1.gaid = t31.gaid
LEFT JOIN ads3 AS t32
ON t1.gaid = t32.gaid 
LEFT JOIN pvp3 AS t33
ON t1.gaid = t33.gaid 
LEFT JOIN pvp_won3 AS t34
ON t1.gaid = t34.gaid 
LEFT JOIN gem3 AS t35
ON t1.gaid = t35.gaid 
LEFT JOIN coin3 AS t36
ON t1.gaid = t36.gaid 
LEFT JOIN gem_earning3 AS t37
ON t1.gaid = t37.gaid 
LEFT JOIN ads_reward3 AS t38
ON t1.gaid = t38.gaid 
LEFT JOIN hero3 AS t39
ON t1.gaid = t39.gaid 
LEFT JOIN level_e_try3 AS t310
ON t1.gaid = t310.gaid 
LEFT JOIN level_e3 AS t311
ON t1.gaid = t311.gaid 
LEFT JOIN idle3 AS t312
ON t1.gaid = t312.gaid 
LEFT JOIN purchase3 AS t313
ON t1.gaid = t313.gaid 
LEFT JOIN login3 AS t314
ON t1.gaid = t314.gaid 
LEFT JOIN headhunt3 AS t315
ON t1.gaid = t315.gaid 
LEFT JOIN logs3 AS t316
ON t1.gaid = t316.gaid
LEFT JOIN daily_task3 AS t318
ON t1.gaid = t318.gaid

LEFT JOIN d1
ON t1.gaid = d1.gaid
LEFT JOIN d2 
ON t1.gaid = d2.gaid
LEFT JOIN d3
ON t1.gaid = d3.gaid
LEFT JOIN will_pay AS t17
ON t1.gaid = t17.gaid
'''
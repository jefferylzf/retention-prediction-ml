import numpy as np
import pandas as pd
import profunc as pf

date = '0928'

# retain param
retain_param = {'input-data-name':('retain_{}.csv').format(date),
         'output-data-name':('retained_label_{}.csv').format(date),
         'bool_churn': 0
         }

# churn param
churn_param = {'input-data-name':('churn_{}_clear.csv').format(date),
         'output-data-name':('churned_label_{}_merged.csv').format(date),
         'bool_churn': 1
         }

# feature param
source_list = ['na_source', 'ot_source', 'gg_source', 'fb_source', 'fbE_source', 'fbV_source']

# Retain user data load and process
retain_df = pd.read_csv(("../raw-data/{0}/{1}").format(date, retain_param['input-data-name']), header = 0)
country_cnt_dict = retain_df['country'].value_counts()

# new features
# mode unlock state
#day 1
retain_df['pvp-unlock'] = 0
retain_df['hunt-unlock'] = 0
retain_df['exp-unlock'] = 0

# source one-hot feature
retain_df['na_source'] = 0
retain_df['ot_source'] = 0
retain_df['gg_source'] = 0
retain_df['fb_source'] = 0
retain_df['fbE_source'] = 0
retain_df['fbV_source'] = 0

# continent one-hot feature
retain_df['AS'] = 0
retain_df['EU'] = 0
retain_df['AF'] = 0
retain_df['NA'] = 0
retain_df['SA'] = 0
retain_df['OC'] = 0

# developed country feature
retain_df['Dev'] = 0

# country proportion
retain_df['ctry_per'] = 0.0

# label assignment
retain_df['label'] = retain_param['bool_churn']

# feature label assignment
for idx in range(len(retain_df)):
    print(idx)
    # unlock feature assignment
    d1_lv = retain_df.loc[idx, 'level_cnt1']
    d2_lv = d1_lv + retain_df.loc[idx, 'level_cnt2']
    d3_lv = d2_lv + retain_df.loc[idx, 'level_cnt3']

    check_flag = True

    # d1 check
    if d1_lv >= 70:
        retain_df.loc[idx, 'hunt-unlock'] = 3
        retain_df.loc[idx, 'pvp-unlock'] = 3
        retain_df.loc[idx, 'exp-unlock'] = 3
    elif d1_lv >= 30:
        retain_df.loc[idx, 'hunt-unlock'] = 3
        retain_df.loc[idx, 'pvp-unlock'] = 3
    else:
        retain_df.loc[idx, 'hunt-unlock'] = 3

    # d2 check
    if d2_lv >= 70:
        if retain_df.loc[idx, 'hunt-unlock'] < 3:
            retain_df.loc[idx, 'hunt-unlock'] = 2
        if retain_df.loc[idx, 'pvp-unlock'] < 3:
            retain_df.loc[idx, 'pvp-unlock'] = 2
        if retain_df.loc[idx, 'exp-unlock'] < 3:
            retain_df.loc[idx, 'exp-unlock'] = 2
    elif d2_lv >= 30:
        if retain_df.loc[idx, 'hunt-unlock'] < 3:
            retain_df.loc[idx, 'hunt-unlock'] = 2
        if retain_df.loc[idx, 'pvp-unlock'] < 3:
            retain_df.loc[idx, 'pvp-unlock'] = 2
    else:
        if retain_df.loc[idx, 'hunt-unlock'] < 3:
            retain_df.loc[idx, 'hunt-unlock'] = 2

    # d3 check
    if d3_lv >= 70:
        if retain_df.loc[idx, 'hunt-unlock'] < 2:
            retain_df.loc[idx, 'hunt-unlock'] = 1
        if retain_df.loc[idx, 'pvp-unlock'] < 2:
            retain_df.loc[idx, 'pvp-unlock'] = 1
        if retain_df.loc[idx, 'exp-unlock'] < 2:
            retain_df.loc[idx, 'exp-unlock'] = 1
    elif d3_lv >= 30:
        if retain_df.loc[idx, 'hunt-unlock'] < 2:
            retain_df.loc[idx, 'hunt-unlock'] = 1
        if retain_df.loc[idx, 'pvp-unlock'] < 2:
            retain_df.loc[idx, 'pvp-unlock'] = 1
    else:
        if retain_df.loc[idx, 'hunt-unlock'] < 2:
            retain_df.loc[idx, 'hunt-unlock'] = 1

    # if lv >= 70:
    #     retain_df.loc[idx, 'pvp-unlock'] = 3
    #     retain_df.loc[idx, 'hunt-unlock'] = 3
    #     retain_df.loc[idx, 'exp-unlock'] = 3
    # if lv >= 30:
    #     retain_df.loc[idx, 'hunt-unlock'] = 1
    #     retain_df.loc[idx, 'pvp-unlock'] = 1
    # if lv >= 15:
    #     retain_df.loc[idx, 'hunt-unlock'] = 1

    # country count feature assignment
    country_cnt = 0.0
    if not pd.isnull(retain_df.loc[idx, 'country']):
        country_cnt = country_cnt_dict[retain_df.loc[idx, 'country']]
    retain_df.loc[idx, 'ctry_per'] = country_cnt/len(retain_df)

    # source feature assignment
    source_idx = pf.get_channel(retain_df.loc[idx, 'refer'])
    retain_df.loc[idx, source_list[source_idx]] = 1

    # country-related feature assignment
    bool_dev = pf.get_development(retain_df.loc[idx, 'country'])
    retain_df.loc[idx, 'Dev'] = bool_dev

    continent = pf.get_continent(retain_df.loc[idx, 'country'])
    if continent != 'other':
        retain_df.loc[idx, continent] = 1


# churn user data load and process
churn_df = pd.read_csv(("../raw-data/{0}/{1}").format(date, churn_param['input-data-name']), header = 0)
country_cnt_dict = churn_df['country'].value_counts()

# new features
churn_df['pvp-unlock'] = 0
churn_df['hunt-unlock'] = 0
churn_df['exp-unlock'] = 0

# source: one-hot features
churn_df['na_source'] = 0
churn_df['ot_source'] = 0
churn_df['gg_source'] = 0
churn_df['fb_source'] = 0
churn_df['fbE_source'] = 0
churn_df['fbV_source'] = 0

# continent one-hot feature
churn_df['AS'] = 0
churn_df['EU'] = 0
churn_df['AF'] = 0
churn_df['NA'] = 0
churn_df['SA'] = 0
churn_df['OC'] = 0

# developed country feature
churn_df['Dev'] = 0

# country proportion
churn_df['ctry_per'] = 0.0

# label assignment
churn_df['label'] = churn_param['bool_churn']

for idx in range(len(churn_df)):
    # unlock feature assignment
    print(idx)
    d1_lv = churn_df.loc[idx, 'level_cnt1']
    d2_lv = d1_lv + churn_df.loc[idx, 'level_cnt2']
    d3_lv = d2_lv + churn_df.loc[idx, 'level_cnt3']

    check_flag = True

    # d1 check
    if check_flag:
        if d1_lv >= 70:
            churn_df.loc[idx, 'hunt-unlock'] = 3
            churn_df.loc[idx, 'pvp-unlock'] = 3
            churn_df.loc[idx, 'exp-unlock'] = 3
            check_flag = 0
        elif d1_lv >= 30:
            churn_df.loc[idx, 'hunt-unlock'] = 3
            churn_df.loc[idx, 'pvp-unlock'] = 3
        else:
            churn_df.loc[idx, 'hunt-unlock'] = 3

    # d2 check
    if check_flag:
        if d2_lv >= 70:
            if churn_df.loc[idx, 'hunt-unlock'] < 3:
                churn_df.loc[idx, 'hunt-unlock'] = 2
            if churn_df.loc[idx, 'pvp-unlock'] < 3:
                churn_df.loc[idx, 'pvp-unlock'] = 2
            if churn_df.loc[idx, 'exp-unlock'] < 3:
                churn_df.loc[idx, 'exp-unlock'] = 2
            check_flag = 0
        elif d2_lv >= 30:
            if churn_df.loc[idx, 'hunt-unlock'] < 3:
                churn_df.loc[idx, 'hunt-unlock'] = 2
            if churn_df.loc[idx, 'pvp-unlock'] < 3:
                churn_df.loc[idx, 'pvp-unlock'] = 2
        else:
            if churn_df.loc[idx, 'hunt-unlock'] < 3:
                churn_df.loc[idx, 'hunt-unlock'] = 2

    # d3 check
    if check_flag:
        if d3_lv >= 70:
            if churn_df.loc[idx, 'hunt-unlock'] < 2:
                churn_df.loc[idx, 'hunt-unlock'] = 1
            if churn_df.loc[idx, 'pvp-unlock'] < 2:
                churn_df.loc[idx, 'pvp-unlock'] = 1
            if churn_df.loc[idx, 'exp-unlock'] < 2:
                churn_df.loc[idx, 'exp-unlock'] = 1
        elif d3_lv >= 30:
            if churn_df.loc[idx, 'hunt-unlock'] < 2:
                churn_df.loc[idx, 'hunt-unlock'] = 1
            if churn_df.loc[idx, 'pvp-unlock'] < 2:
                churn_df.loc[idx, 'pvp-unlock'] = 1
        else:
            if churn_df.loc[idx, 'hunt-unlock'] < 2:
                churn_df.loc[idx, 'hunt-unlock'] = 1

    # source feature assignment
    source_idx = pf.get_channel(churn_df.loc[idx, 'refer'])
    churn_df.loc[idx, source_list[source_idx]] = 1

    # country count feature assignment
    country_cnt = 0.0
    if not pd.isnull(churn_df.loc[idx, 'country']):
        country_cnt = country_cnt_dict[churn_df.loc[idx, 'country']]
    churn_df.loc[idx, 'ctry_per'] = country_cnt/len(churn_df)

    # developed feature assignment
    bool_dev = pf.get_development(churn_df.loc[idx, 'country'])
    churn_df.loc[idx, 'Dev'] = bool_dev

    # continent feature assignment
    continent = pf.get_continent(churn_df.loc[idx, 'country'])
    if continent != 'other':
        churn_df.loc[idx, continent] = 1

res = pd.concat([churn_df,retain_df], axis=0, ignore_index=True)
res.replace(np.nan, 0, inplace=True)
res.drop(res.columns[0],axis=1,inplace=True)
res.to_csv(('../train-data/withNewFeatures/merged_global_{}_clear.csv').format(date))


print('finally')
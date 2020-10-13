def get_channel(string):
    if string[:2] == 'na':
        return 0
    if string[:2] == 'aw':
        return 2
    if string[:2] == 'fb':
        pos = string.find('[')
        if pos != -1:
            user_val = string[pos+1]
            if user_val == 'E':
                return 4
            return 5
        return 3
    return 1


def get_continent(string):
    '''
    get the continent of user
    :param string:
    :return:
    '''
    idx_list = []
    asia_list = {'AF', 'AZ', 'BH', 'BD', 'AM', 'BT', 'IO', 'BN', 'MM', 'KH', 'LK', 'CN', 'TW', 'CX', 'CC', 'CY', 'GE',
                 'PS',
                 'HK', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'KZ', 'JO', 'KP', 'KR', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY',
                 'MV',
                 'MN', 'OM', 'NP', 'PK', 'PH', 'TL', 'QA', 'RU', 'SA', 'SG', 'VN', 'SY', 'TJ', 'TH', 'AE', 'TR', 'TM',
                 'UZ',
                 'YE', 'XE', 'XD', 'XS'}
    idx_list.append(asia_list)

    africa_list = {'DZ', 'AO', 'BW', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'YT', 'CG', 'CD', 'BJ', 'GQ', 'ET', 'ER', 'DJ', 'GA',
     'GM', 'GH', 'GN', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG',
     'GW', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'ZW', 'SS', 'EH', 'SD', 'SZ', 'TG', 'TN', 'UG',
     'EG', 'TZ', 'BF', 'ZM'}
    idx_list.append(africa_list)

    europe_list = {'AL', 'AD', 'AZ', 'AT', 'AM', 'BE', 'BA', 'BG', 'BY', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FO', 'FI', 'AX', 'FR',
          'GE', 'DE', 'GI', 'GR', 'VA', 'HU', 'IS', 'IE', 'IT', 'KZ', 'LV', 'LI', 'LT', 'LU', 'MT', 'MC', 'MD', 'ME',
          'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SJ', 'SE', 'CH', 'TR', 'UA', 'MK', 'GB',
          'GG', 'JE', 'IM'}
    idx_list.append(europe_list)

    namerica_list = {'AG', 'BS', 'BB', 'BM', 'BZ', 'VG', 'CA', 'KY', 'CR', 'CU', 'DM', 'DO', 'SV', 'GL', 'GD', 'GP', 'GT', 'HT',
          'HN', 'JM', 'MQ', 'MX', 'MS', 'AN', 'CW', 'AW', 'SX', 'BQ', 'NI', 'UM', 'PA', 'PR', 'BL', 'KN', 'AI', 'LC',
          'MF', 'PM', 'VC', 'TT', 'TC', 'US', 'VI'}
    idx_list.append(namerica_list)

    ocean_list = {'AS', 'AU', 'SB', 'CK', 'FJ', 'PF', 'KI', 'GU', 'NR', 'NC', 'VU', 'NZ', 'NU', 'NF', 'MP', 'UM', 'FM', 'MH',
          'PW', 'PG', 'PN', 'TK', 'TO', 'TV', 'WF', 'WS', 'XX'}
    idx_list.append(ocean_list)

    samerica_list = {'AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE'}
    idx_list.append(samerica_list)

    continent_list = ['AS', 'AF', 'EU', 'NA', 'OC', 'SA']

    for idx, l in enumerate(idx_list):
        if string in l:
            return continent_list[idx]
    return 'other'

def get_development(string):
    '''
    classify the development/developing type of country
    :param string:
    :return:
    '''
    dev_list = {'AL','AD','AZ','AT','AM','BE','BA','AU','CA','BG','BY','HR','NZ','CY',
                'CZ','DK','EE','FO','FI','AX','FR','JP','GE','IL','DE','GI','GR','VA',
                'KR','HU','IS','IE','IT','KZ','LV','LI','LT','LU','MT','MC','MD','ME',
                'NL','NO','SG','PL','PT','RO','US','SM','RS','SK','SI','ES','SJ','SE',
                'CH','TR','UA','MK','GB','GG','JE','IM'}
    if string in dev_list:
        return 1
    return 0



# for i in range(0, 145):
#     j = sc.iloc[i, 0]
#     k = sc.iloc[i, 1]
#     data['count'].replace(sc.iloc[i, 0], sc.iloc[i, 1], inplace=True)
# data.to_csv('retain_new_features_0902.csv')
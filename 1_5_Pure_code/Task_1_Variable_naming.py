"""
Задание на именование переменных.
Контекст: функция, которая проводит расчеты доходов в датафрейме Pandas
Изменения наименования переменных:

df - dataframe // Основной DataFrame с данными.
prev_rules - previous_rules // Список предыдущих правил.
rule_obj - rule // Объект правила.
base_revenue_col - base_revenue_column // Название колонки с доходами за 2024 год.
filters - conditions_filters // Список фильтров для условий правил.
total - total_base_revenue // Общая сумма базовых доходов.
year_index - yearly_index // Годовой индекс.
rules - current_rules // Список текущих правил.
rule_indexation - rule_indexes // Словарь индексов правил.
revenue_base - base_revenue_name // Название колонки с базовыми доходами.
revenue - yearly_revenue // Колонка доходов за текущий год.
revenue_prev - previous_year_revenue // Колонка доходов за предыдущий год.
revenue_noindex - revenue_without_indexation // Колонка доходов без учёта индексации.
epl - current_year_epl // Грузооборот за текущий год.
epl_prev - previous_year_epl // Грузооборот за предыдущий год.
rule_index - rule_counter // Счётчик правил.
rule_coef - rule_coefficient // Коэффициент правила.

"""



# было
def calculate_base_revenues(df, YEARS, INDEXES, EPL_CHANGE):

    prev_rules = tr_prev.load_rules(active_only=True)
    base_revenue_col = 'Доходы 2024, тыс.руб'
    for rule_obj in prev_rules:
        filters = []
        for condition in rule_obj["conditions"]:
            parameter = condition["parameter"]
            include = condition["include"]
            values = condition["values"].split(';') if condition["values"] else []
            if values == ['Все']:
                values = df[parameter].unique()
            if include == 'включает':
                filters.append(df[parameter].isin(values))
            else:
                filters.append(~df[parameter].isin(values))

        if rule_obj['variant'] == 'млрд': # миллиарды
            total = df.loc[np.logical_and.reduce(filters), base_revenue_col].sum()
            df.loc[np.logical_and.reduce(filters), 'part'] = df.loc[np.logical_and.reduce(filters), base_revenue_col] / total
            df.loc[np.logical_and.reduce(filters), base_revenue_col] = df.loc[np.logical_and.reduce(filters), base_revenue_col] + (float(rule_obj['index_2024']) * 1000000 * df.loc[np.logical_and.reduce(filters), 'part'])
        else:  # индексы
            if rule_obj['variant'] == '*':
                df.loc[np.logical_and.reduce(filters), base_revenue_col] = df.loc[np.logical_and.reduce(filters), base_revenue_col] * float(rule_obj['index_2024'])


    year_index = 1
    rules = tr.load_rules(active_only=True)
    rule_indexation = {}
    for rule_obj in rules:
        rule_indexation[rule_obj["id"]] = []

    revenue_base = CON.PR_P
    epl_base = f'2024 ЦЭКР груззоборот, тыс ткм'
    df['epl_tarif_base'] = df[revenue_base] / df[epl_base]
    df['rules_total'] = 0
    for i, year in enumerate(YEARS):
        year_index *= INDEXES[i]
        revenue = f'Доходы {year}, тыс.руб'
        revenue_prev = f'Доходы {year-1}, тыс.руб'
        revenue_base = f'Доходы {year}_0, тыс.руб'
        revenue_noindex = f'Доходы {year}_без учета индексации, тыс.руб'

        epl = f'{year} ЦЭКР груззоборот, тыс ткм'
        epl_prev = f'{year-1} ЦЭКР груззоборот, тыс ткм'

        if EPL_CHANGE == [True]:
        # учитываем рост грузооборота
            df.loc[df['epl_tarif_base'].notna(), revenue_noindex] = df[revenue_prev]  * (df[epl] / df[epl_prev])
            df.loc[df['epl_tarif_base'].isna(), revenue_noindex] = df[revenue_prev]
        else:
            df[revenue_noindex] = df[revenue_prev]

        # базовая индексация
        df[revenue_base] = df[revenue_noindex] * (INDEXES[i]-1) * df['base_diff']

        df[revenue] = df[revenue_noindex] + df[revenue_base]
        rule_index = 0
        df[f'rules%_{year}'] = 1.0
        for rule_obj in rules:
            rule_index += 1
            df[f'rules%_{year}_{rule_index}'] = 1.0
            revenue_rule = f'Доходы {year}_{rule_index}, тыс.руб'
            revenue_rule_prev = f'Доходы {int(year)-1}_{rule_index}, тыс.руб'
            filters = []
            for condition in rule_obj["conditions"]:
                parameter = condition["parameter"]
                include = condition["include"]
                values = condition["values"].split(';') if condition["values"] else []
                if values == ['Все']:
                    values = df[parameter].unique()
                if include == 'включает':
                    filters.append(df[parameter].isin(values))
                else:
                    filters.append(~df[parameter].isin(values))

            df[revenue_rule] = 0.0
            rule_coef = float(rule_obj['index_'+str(year)]) - 1
            df.loc[np.logical_and.reduce(filters), revenue_rule] = df[revenue_noindex] * rule_coef * df['rules_diff'] * int(rule_obj['base_percent'])/100
            df.loc[np.logical_and.reduce(filters), f'rules%_{year}'] *=  float(rule_obj['index_'+str(year)]) * df['rules_diff']
            df.loc[np.logical_and.reduce(filters), f'rules%_{year}_{rule_index}'] =  float(rule_obj['index_'+str(year)])

            df[revenue] += df[revenue_rule]

    return df

# стало
def calculate_base_revenues(dataframe, years, indexes, epl_change):
    previous_rules = tr_prev.load_rules(active_only=True)
    base_revenue_column = 'Доходы 2024, тыс.руб'
    for rule in previous_rules:
        conditions_filters = []
        for condition in rule["conditions"]:
            parameter = condition["parameter"]
            include = condition["include"]
            values = condition["values"].split(';') if condition["values"] else []
            if values == ['Все']:
                values = dataframe[parameter].unique()
            if include == 'включает':
                conditions_filters.append(dataframe[parameter].isin(values))
            else:
                conditions_filters.append(~dataframe[parameter].isin(values))

        if rule['variant'] == 'млрд':  # миллиарды
            total_base_revenue = dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column].sum()
            dataframe.loc[np.logical_and.reduce(conditions_filters), 'part'] = dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column] / total_base_revenue
            dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column] = dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column] + (float(rule['index_2024']) * 1000000 * dataframe.loc[np.logical_and.reduce(conditions_filters), 'part'])
        else:  # индексы
            if rule['variant'] == '*':
                dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column] = dataframe.loc[np.logical_and.reduce(conditions_filters), base_revenue_column] * float(rule['index_2024'])

    yearly_index = 1
    current_rules = tr.load_rules(active_only=True)
    rule_indexes = {}
    for rule in current_rules:
        rule_indexes[rule["id"]] = []

    pcb_size_column = CON.PR_P
    epl_tariff_base = f'2024 ЦЭКР груззоборот, тыс ткм'
    dataframe['epl_tarif_base'] = dataframe[pcb_size_column] / dataframe[epl_tariff_base]
    dataframe['rules_total'] = 0
    for i, year in enumerate(years):
        yearly_index *= indexes[i]
        yearly_revenue = f'Доходы {year}, тыс.руб'
        previous_year_revenue = f'Доходы {year-1}, тыс.руб'
        base_revenue_name = f'Доходы {year}_0, тыс.руб'
        revenue_without_indexation = f'Доходы {year}_без учета индексации, тыс.руб'

        current_year_epl = f'{year} ЦЭКР груззоборот, тыс ткм'
        previous_year_epl = f'{year-1} ЦЭКР груззоборот, тыс ткм'

        if epl_change == [True]:
            # учитываем рост грузооборота
            dataframe.loc[dataframe['epl_tarif_base'].notna(), revenue_without_indexation] = dataframe[previous_year_revenue] * (dataframe[current_year_epl] / dataframe[previous_year_epl])
            dataframe.loc[dataframe['epl_tarif_base'].isna(), revenue_without_indexation] = dataframe[previous_year_revenue]
        else:
            dataframe[revenue_without_indexation] = dataframe[previous_year_revenue]

        # базовая индексация
        dataframe[base_revenue_name] = dataframe[revenue_without_indexation] * (indexes[i] - 1) * dataframe['base_diff']

        dataframe[yearly_revenue] = dataframe[revenue_without_indexation] + dataframe[base_revenue_name]
        rule_counter = 0
        dataframe[f'rules%_{year}'] = 1.0
        for rule in current_rules:
            rule_counter += 1
            dataframe[f'rules%_{year}_{rule_counter}'] = 1.0
            rule_based_revenue = f'Доходы {year}_{rule_counter}, тыс.руб'
            previous_rule_based_revenue = f'Доходы {int(year) - 1}_{rule_counter}, тыс.руб'
            conditions_filters = []
            for condition in rule["conditions"]:
                parameter = condition["parameter"]
                include = condition["include"]
                values = condition["values"].split(';') if condition["values"] else []
                if values == ['Все']:
                    values = dataframe[parameter].unique()
                if include == 'включает':
                    conditions_filters.append(dataframe[parameter].isin(values))
                else:
                    conditions_filters.append(~dataframe[parameter].isin(values))

            dataframe[rule_based_revenue] = 0.0
            rule_coefficient = float(rule['index_' + str(year)]) - 1
            dataframe.loc[np.logical_and.reduce(conditions_filters), rule_based_revenue] = dataframe[revenue_without_indexation] * rule_coefficient * dataframe['rules_diff'] * int(rule['base_percent']) / 100
            dataframe.loc[np.logical_and.reduce(conditions_filters), f'rules%_{year}'] *= float(rule['index_' + str(year)]) * dataframe['rules_diff']
            dataframe.loc[np.logical_and.reduce(conditions_filters), f'rules%_{year}_{rule_counter}'] = float(rule['index_' + str(year)])

            dataframe[yearly_revenue] += dataframe[rule_based_revenue]

    return dataframe
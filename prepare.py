from sklearn.model_selection import train_test_split



def prep_iris(df):
    df = df.drop(columns=['species_id','measurement_id','Unnamed: 0'])
    df.rename(columns={'species_name':'species'},inplace = True)
    dummies = pd.get_dummies(df[['species']])
    df = pd.concat([df, dummies], axis=1)
    return df

def prep_titanic(df):
    df = df.drop(columns=['passenger_id','deck','Unnamed: 0','embarked','class','age'])
    df = df.dropna()
    dummies = df.select_dtypes(include='object').columns
    dummies = pd.get_dummies(df[dummies])
    df = pd.concat([df, dummies], axis=1)
    return df

def prep_telco(df):
    df = df.drop(columns=['Unnamed: 0','payment_type_id', 'internet_service_type_id', 'contract_type_id','customer_id'])
    df['total_charges'] = (df.total_charges + '0').astype('float')
    dummies = df.select_dtypes(include='object').columns
    dummies = pd.get_dummies(df[dummies])
    df = pd.concat([df, dummies], axis=1)
    return df

def split_data(df, target = ''):
    train, val_test = train_test_split(df,test_size=.2,random_state=21,stratify=df[target])
    validate, test = train_test_split(val_test,test_size=.3,random_state=21,stratify=val_test[target])
    return train, validate, test
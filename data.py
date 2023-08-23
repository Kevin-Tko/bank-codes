import pandas as pd

def bank_name(user_input):
  df = pd.read_csv('bics.csv')
  bank = df[df['Bank'].str.contains(user_input)].iloc[0, 0]
  return bank

def bank_bic(user_input):
  df = pd.read_csv('bics.csv')
  swift = df[df['Bank'].str.contains(user_input)].iloc[0, 2]
  return swift

def bank_city(user_input):
  df = pd.read_csv('bics.csv')
  city = df[df['Bank'].str.contains(user_input)].iloc[0, 1]
  return city

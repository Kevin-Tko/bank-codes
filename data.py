import pandas as pd

def bank_name(user_input):
  df = pd.read_csv('HQ BICS.csv')
  bank = df[df['Bank'].str.contains(user_input)].iloc[0, 0]
  return bank

def bank_bic(user_input):
  df = pd.read_csv('HQ BICS.csv')
  swift = df[df['Bank'].str.contains(user_input)].iloc[0, 2]
  return swift

def international_bank_name(user_input_iban):
  df_int = pd.read_csv('iban.csv')
  bank = df_int[df_int['BANKS'].str.contains(user_input_iban)].iloc[0, 0]
  return bank
  
def internationa_bank_bic(user_input_iban):
  df_int = pd.read_csv('iban.csv')
  swift = df_int[df_int['BANKS'].str.contains(user_input_iban)].iloc[0, 2]
  return swift

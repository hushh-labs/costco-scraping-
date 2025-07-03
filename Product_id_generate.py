import pandas as pd
import random
import string
from config import CSV_FILE

def generate_random_id(length=8):
    return 'prod_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def main():
    df = pd.read_csv(CSV_FILE)
    df['product_id'] = df['product_id'].apply(
        lambda x: generate_random_id() if pd.isna(x) or str(x).strip() == '' else x
    )
    df.to_csv(CSV_FILE, index=False)
    print("✅ Random product_ids added where missing!")

if __name__ == "__main__":
    main()

# ✅ main.py (ONLY place to configure CSV file)

import subprocess
import os
import sys  # 👈 Important for virtualenv fix

# 👇 CHANGE ONLY HERE
CSV_FILE = "costco-products.csv"
OUTPUT_DIR = "images"
BASE_URL = "https://gsqmwxqgqrgzhlhmbscg.supabase.co/storage/v1/object/public/costco-products-scrapped"

# Save shared config to a file so all scripts can import it
with open("config.py", "w") as f:
    f.write(f'CSV_FILE = "{CSV_FILE}"\n')
    f.write(f'OUTPUT_DIR = "{OUTPUT_DIR}"\n')
    f.write(f'BASE_URL = "{BASE_URL}"\n')


def run_script(script_name):
    print(f"\n🚀 Running {script_name}...")
    try:
        subprocess.run([sys.executable, script_name], check=True)  # 👈 Use correct Python path
        print(f"✅ {script_name} completed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ {script_name} failed with error: {e}")
        exit(1)


def main():
    print("\n📦 Starting Costco Scraper Pipeline...")

    if not os.path.exists(CSV_FILE):
        print(f"❌ Error: {CSV_FILE} not found!")
        exit(1)

    run_script("Product_id_generate.py")
    run_script("Image_download.py")
    run_script("fill_costco_data.py")

    print("\n🎉 All tasks completed successfully!")


if __name__ == "__main__":
    main()

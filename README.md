# 🛒 Costco Product Scraper

Scrapes Costco product info & images like a beast and saves everything in a single CSV. Fully automated pipeline. All you gotta do is drop a CSV with product URLs. That's it.

---

## 🧾 Folder Structure

```

Costco Scraping/
├── main.py                  # Main pipeline to run all steps
├── Product\_id\_generate.py  # Fills in random product IDs
├── Image\_download.py       # Downloads product images from bfasset
├── fill\_costco\_data.py     # Scrapes brand, title, price, description etc.
├── config.py               # Auto-generated config file with shared vars
├── costco-products.csv     # Your input/output CSV (must have product\_url column)
├── images/                 # Folder where all images will be saved
├── requirements.txt        # All required libraries
└── README.md               # You're reading it

````

---

## 🔧 Setup Instructions

### 1. 📂 Move into Folder

Make sure all the `.py` files and your CSV file are in **one folder**.

---

### 2. 🧠 Prepare the CSV

Create a CSV file called:  
**`costco-products.csv`**

It **must** have at least this column:

| product_url |
|-------------|
| https://www.costco.com/... |
| https://www.costco.com/... |

You can leave the rest empty — the script fills them in.

---

### 3. 📁 Create the `images` Folder

Create it manually:

```bash
mkdir images
````

Or right-click → New Folder → name it `images`.

---

### 4. 💻 Install Dependencies (Recommended: in a virtual environment)

```bash
python -m venv venv
venv\Scripts\activate        # For Windows
# source venv/bin/activate  # For Mac/Linux

pip install -r requirements.txt
playwright install
```

---

## 🚀 Run the Pipeline

```bash
python main.py
```

The script will:

1. ✅ Auto-generate product IDs if missing
2. 📸 Download bfasset product images
3. 📋 Scrape product info (title, brand, price, description)
4. 🧾 Save all data back into `costco-products.csv`

---

## 🪣 Supabase Setup (Manual Step)

> Images will be **downloaded locally into the `images/` folder**, but for the final links to work (in `image_url`), you need to:

1. Create a **Supabase bucket** (e.g. `costco-products-scrapped`)
2. Upload everything from the `images/` folder to that bucket manually
3. Make sure the bucket is **public**
4. Update the **`BASE_URL`** in `main.py` to point to your Supabase public bucket URL:

   ```python
   BASE_URL = "https://<your-project-ref>.supabase.co/storage/v1/object/public/<your-bucket-name>"
   ```

That’s how image URLs in the CSV will become valid online links.

---

## ⚠️ Notes

* `costco-products.csv` should not be empty and must have valid URLs.
* The browser window will pop up — don’t close it unless debugging.
* If you see timeout or `HTTP/2` errors, check your internet or increase timeout in `Image_download.py`.
* No rate-limiting bypass logic is added yet — you can add rotating proxies or delays if needed.

---

## 🧪 Sample Output CSV

| product\_id  | product\_url | image\_url                                                     | brand | price | description         | ... |
| ------------ | ------------ | -------------------------------------------------------------- | ----- | ----- | ------------------- | --- |
| prod\_abc123 | https\://... | [https://supabase.co/.../1.png](https://supabase.co/.../1.png) | Nike  | \$89  | Sleek running shoes | ... |

---

## 🧙‍♂️ Dev Tip

You only need to update `main.py`'s config:

```python
CSV_FILE = "costco-products.csv"
OUTPUT_DIR = "images"
BASE_URL = "https://your-supabase-link"
```

Everything else is auto-managed. Go build that scraper empire 🚀

```

---

Let me know if you want a version that **auto-uploads images to Supabase too** with API keys and everything. That’d be 🔥 next level.
```

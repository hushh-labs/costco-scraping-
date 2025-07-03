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
```

---

## 🚀 Run the Pipeline

```bash
python main.py
```

The script will:

1. Auto-generate product IDs if missing
2. Download bfasset product images
3. Scrape product info (title, brand, price, description)
4. Save all data back into `costco-products.csv`

---

## ⚠️ Notes

* `costco-products.csv` should not be empty and must have valid URLs.
* Images will be saved in the `images/` folder and uploaded to Supabase if configured.
* The browser will pop up — don’t close it manually unless you're debugging.
* If you see timeout or HTTP/2 errors, check your internet or increase the timeout in the Playwright script.

---

## 🧪 Sample Output CSV

| product\_id  | product\_url | image\_url                                               | brand | price | description         | ... |
| ------------ | ------------ | -------------------------------------------------------- | ----- | ----- | ------------------- | --- |
| prod\_abc123 | https\://... | [https://supabase/.../1.png](https://supabase/.../1.png) | Nike  | \$89  | Sleek running shoes | ... |

---




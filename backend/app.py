import csv

# ====== CSV PARSING ======
# removes all the parenthesis and unwanted symbols for neg pnl
def parseAmount(s):
    s = s.strip()
    neg = "(" in s and ")" in s
    s = s.replace("$", "").replace("(", "").replace(")", "").replace(",", "")
    val = float(s)
    return -val if neg else val

with open('./test_data.csv', 'r',) as performance:
    dt = csv.DictReader(performance)

# Normalizes the headers for clarity
    up_dt = []
    for r in dt:
        print(r)
        row = {'Symbol': r['symbol'],
           'Contrace Amount': r['_priceFormat'],
           'Price Format Type': r['_priceFormatType'],
           'Tick Size': r['_tickSize'],
           'pnl': parseAmount(r['pnl']),
           'Bought Time': r['boughtTimestamp'],
           'Sold Time': r['soldTimestamp'],
           'Duration': r['duration']}
    up_dt.append(row)
print(up_dt)


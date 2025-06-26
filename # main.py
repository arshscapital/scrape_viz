# main.py
import pandas as pd, requests, bs4, argparse

def scrape(limit=5, out_csv="gdp.csv"):
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    df = pd.read_html(str(table))[0].head(limit)
    df.to_csv(out_csv, index=False)
    print(f"Saved {out_csv}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--out", default="gdp.csv")
    args = p.parse_args()
    scrape(args.limit, args.out)

import pandas as pd

file = "instagram_accounts.xlsx"


def extract_handles(file):
    accounts = pd.read_excel(file)

    def get_hanlde(url):
        handle_arr = url.split("https://www.instagram.com/")[1].split("/")
        if len(handle_arr[0]) > 2:
            handle = handle_arr[0]
        else:
            handle = handle_arr[1]
        return handle

    accounts["handle"] = accounts["business_url"].apply(get_hanlde)
    new_accounts = accounts[["handle", "business_url"]]
    new_accounts = new_accounts.drop_duplicates(subset="handle", keep="first")
    new_accounts.to_excel(file, index=False)
    print("Done ✅")

extract_handles(file)
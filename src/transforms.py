import pandas as pd

def clean_users(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["email"] = out["email"].str.lower().str.strip()
    out.loc[out["age"] < 0, "age"] = pd.NA
    out = out.drop_duplicates(subset=["user_id"], keep="first").reset_index(drop=True)
    return out[["user_id", "email", "age"]]

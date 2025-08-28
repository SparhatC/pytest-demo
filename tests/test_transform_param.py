import pandas as pd
import pytest
from src.transforms import clean_users

@pytest.mark.parametrize("age_in, age_out", [(0, 0), (25, 25), (-1, None)])
def test_age_rule(age_in, age_out):
    df = pd.DataFrame({"user_id":[1,2], "email":["a@x.com","b@x.com"], "age":[30, age_in]})
    res = clean_users(df)
    val = res.loc[res["user_id"] == 2, "age"].iloc[0]
    assert (pd.isna(val) and age_out is None) or (val == age_out)

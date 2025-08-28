import pandas as pd
from hypothesis import given, strategies as st
from src.transforms import clean_users

@given(st.lists(st.tuples(
    st.integers(min_value=1, max_value=10),
    st.emails(),
    st.integers(min_value=-10, max_value=120)
), min_size=1, max_size=50))
def test_user_id_uniqueness(data):
    df_in = pd.DataFrame(data, columns=["user_id","email","age"])
    df_out = clean_users(df_in)
    assert df_out["user_id"].is_unique

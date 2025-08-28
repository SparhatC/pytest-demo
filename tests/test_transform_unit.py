from src.transforms import clean_users

def test_clean_users_basic(users_raw):
    df = clean_users(users_raw)
    assert len(df) == 2
    assert set(df["email"]) == {"alice@example.com", "bob@example.com"}
    assert df.loc[df["user_id"] == 2, "age"].isna().all()

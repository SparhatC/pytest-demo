import pytest
import pandas as pd

@pytest.fixture
def users_raw():
    return pd.DataFrame({
        "user_id": [1, 1, 2],
        "email": ["Alice@Example.COM ", "Alice@Example.COM ", "Bob@Example.com"],
        "age": [30, 30, -5]
    })



def test_sample_name(sample_data):
    assert sample_data["name"] == "Alice"

def test_sample_age(sample_data):
    assert sample_data['age'] == 30

def test_sample_salary(sample_data):
    assert sample_data['Salary'] == 500
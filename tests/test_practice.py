import pytest


def test_sample_name(sample_data):
    assert sample_data["name"] == "Alice"

def test_sample_age(sample_data):
    assert sample_data['age'] == 30

def test_sample_salary(sample_data):
    assert sample_data['Salary'] == 500


def test_validate_testdata(resource):
    assert resource["data"] == 123

#parameterizing data here.
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123"),
                             ("user1", "pass1"),
                             ("test", "test123")
                          ])
def test_login(username, password):
    print(f"Testing with {username}, {password}")
    assert  username != ""

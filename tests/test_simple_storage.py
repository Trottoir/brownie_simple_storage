from brownie import accounts, SimpleStorage


def test_deploy():
    # Arrange
    account = accounts[0]
    # Acting
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assserting
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Acting
    expected = 15
    simple_storage.store(expected, {"from": account}).wait(1)
    # Assserting
    assert expected == simple_storage.retrieve()

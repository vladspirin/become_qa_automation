def test_search_for_existing_repo(git_hub_api_app):
    existing_repo_name = 'become_qa_automation'
    repos = git_hub_api_app.search_repos(existing_repo_name)  # list/array returned

    print("Checking total count is not 0")

    assert repos['total_count'] != 0  # some elements exists in array/list


def test_search_for_nonexistent_repo(git_hub_api_app):
    nonexistent_repo_name = 'lnasdklfnkjanskdjfnkjabsdjhfuyagsuygfuyagsduyfgauysdf'
    repos = git_hub_api_app.search_repos(nonexistent_repo_name)  # list/array returned

    print("Checking total count is 0")

    assert repos['total_count'] == 0  # some elements exists in array/list


def test_search_for_nonexistent_hash(git_hub_api_app):
    nonexistent_commit_hash = 'lnasdklfnkjanskdjfnkjabsdjhfuyagsuygfuyagsduyfgauysdf'
    repos = git_hub_api_app.search_commits(nonexistent_commit_hash)  # list/array returned

    print("Checking total count is 0")

    assert 1 == 0  # some elements exists in array/list
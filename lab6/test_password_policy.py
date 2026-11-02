from password_policy import check_password, strength, suggest_fix


# check_password: length boundaries and common-password detection
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_password_below_minimum_length():
    assert "too short" in check_password("Ab1!")


def test_password_at_minimum_length_is_not_too_short():
    assert "too short" not in check_password("Abcdef1!")


def test_password_above_maximum_length():
    password = "Aa1!" + ("b" * 61)  # 65 characters
    assert "too long" in check_password(password)


def test_password_at_maximum_length_is_not_too_long():
    password = "Aa1!" + ("b" * 60)  # 64 characters
    assert "too long" not in check_password(password)


def test_common_password_is_detected_case_insensitively():
    assert "common" in check_password("PASSWORD")


# check_password: each character-category condition
def test_missing_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_missing_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_missing_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_missing_special_character():
    assert "no special" in check_password("Abcdefg1")


# strength: all return categories and both sides of decision branches
def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


def test_long_valid_password_is_strong():
    assert strength("Abcdefghijk1!X") == "strong"


def test_password_with_one_or_two_issues_is_weak():
    assert strength("Abcdefgh") == "weak"


def test_password_with_more_than_two_issues_is_very_weak():
    assert strength("abcdefg") == "very weak"


# suggest_fix: every decision path
def test_suggest_fix_with_no_issues():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_for_too_short():
    assert suggest_fix(["too short", "no uppercase"]) == "add more characters"


def test_suggest_fix_for_common_password():
    assert suggest_fix(["common", "no uppercase"]) == "avoid common passwords"


def test_suggest_fix_for_missing_character_category():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_for_too_long():
    assert suggest_fix(["too long"]) == "shorten it"

import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ---------- Starter examples ----------
def test_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_can_enter():
    assert can_enter(10, True, False, "M") is True


# ---------- membership_cost ----------
def test_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_too_young_raises():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_senior_discount():
    # 1500 - 1500//4 = 1125
    assert membership_cost("monthly", 65, False, False) == 1125


def test_student_discount():
    # 4000 - 4000//10 = 3600
    assert membership_cost("quarterly", 20, True, False) == 3600


def test_trainer_on_yearly_gets_500_off():
    assert membership_cost("yearly", 30, False, True) == 13500


# ---------- can_enter ----------
def test_inactive_plan_cannot_enter():
    assert can_enter(10, False, False, "M") is False


def test_too_early_cannot_enter():
    assert can_enter(4, True, False, "M") is False


def test_women_only_slot_female_allowed():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male_denied():
    assert can_enter(10, True, True, "M") is False


# ---------- bmi_category ----------
def test_invalid_height_raises():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_bmi_underweight():
    assert bmi_category(50, 1.8) == "underweight"


def test_bmi_normal():
    assert bmi_category(65, 1.75) == "normal"


def test_bmi_overweight():
    assert bmi_category(80, 1.75) == "overweight"


def test_bmi_obese():
    assert bmi_category(100, 1.7) == "obese"

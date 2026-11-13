import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ---------- Starter examples ----------
def test_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_can_enter():
    assert can_enter(10, True, False, "M") is True


# ---------- membership_cost: validation branches ----------
def test_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_too_young_raises():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_age_14_is_allowed_boundary():
    assert membership_cost("monthly", 14, False, False) == 1500


# ---------- membership_cost: discount branches (if / elif / neither) ----------
def test_senior_discount():
    assert membership_cost("monthly", 65, False, False) == 1125


def test_age_60_boundary_gets_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_age_59_student_gets_student_discount_not_senior():
    assert membership_cost("monthly", 59, True, False) == 1350


def test_student_discount():
    assert membership_cost("quarterly", 20, True, False) == 3600


def test_senior_student_gets_only_senior_discount():
    # age >= 60 branch wins; the elif (student) is skipped
    assert membership_cost("monthly", 65, True, False) == 1125


def test_no_discount_for_adult_non_student():
    assert membership_cost("yearly", 30, False, False) == 12000


# ---------- membership_cost: trainer branches ----------
def test_trainer_on_monthly():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_trainer_on_quarterly():
    assert membership_cost("quarterly", 30, False, True) == 6000


def test_trainer_on_yearly_gets_500_off():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_yearly_without_trainer_no_trainer_discount():
    assert membership_cost("yearly", 30, False, False) == 12000


# ---------- can_enter: every branch ----------
def test_inactive_plan_cannot_enter():
    assert can_enter(10, False, False, "M") is False


def test_too_early_cannot_enter():
    assert can_enter(4, True, False, "M") is False


def test_too_late_cannot_enter():
    assert can_enter(23, True, False, "M") is False


def test_hour_5_boundary_allowed():
    assert can_enter(5, True, False, "M") is True


def test_hour_22_boundary_allowed():
    assert can_enter(22, True, False, "M") is True


def test_women_only_slot_female_allowed():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male_denied():
    assert can_enter(10, True, True, "M") is False


def test_normal_slot_female_allowed():
    assert can_enter(10, True, False, "F") is True


# ---------- bmi_category: every branch ----------
def test_zero_height_raises():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_negative_height_raises():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, -1.7)


def test_bmi_underweight():
    assert bmi_category(50, 1.8) == "underweight"


def test_bmi_normal():
    assert bmi_category(65, 1.75) == "normal"


def test_bmi_overweight():
    assert bmi_category(80, 1.75) == "overweight"


def test_bmi_obese():
    assert bmi_category(100, 1.7) == "obese"

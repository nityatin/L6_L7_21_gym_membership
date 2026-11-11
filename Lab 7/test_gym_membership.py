from hypothesis import given, strategies as st
from gym_membership import parse_plan, calculate_bmi, average_workout


# ---------- 1. "Must never crash" fuzz tests (random text and None) ----------

@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except Exception as e:
        assert False, f"parse_plan crashed with: {e!r}"


@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):
    try:
        calculate_bmi(s)
    except Exception as e:
        assert False, f"calculate_bmi crashed with: {e!r}"


@given(st.text() | st.none())
def test_average_workout_no_crash(s):
    try:
        average_workout(s)
    except Exception as e:
        assert False, f"average_workout crashed with: {e!r}"


# ---------- 2. Correctness properties on VALID inputs ----------

@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
       st.integers(min_value=1, max_value=120))
def test_parse_plan_valid(plan, months):
    assert parse_plan(f"{plan}-{months}") == (plan.upper(), months)


@given(st.floats(min_value=1, max_value=500),
       st.floats(min_value=0.5, max_value=3))
def test_calculate_bmi_valid(weight, height):
    result = calculate_bmi(f"{weight},{height}")
    assert result is not None and result > 0


@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=1))
def test_average_workout_valid(values):
    result = average_workout(" ".join(map(str, values)))
    assert min(values) <= result <= max(values)

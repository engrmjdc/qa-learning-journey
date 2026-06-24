age_1 = 25

if age_1 >= 18:
    print("Adult")

age_2 = 15

if age_2 >= 18:
    print("Adult")
else:
    print("Minor")

actual_result = "Login Successful"
expected_result = "Login Successful"

if actual_result == expected_result:
    print("PASS")
else:
    print("FAIL")   

score = 85

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
else:
    print("Needs Improvement")

salary = 35000

if salary >= 80000:
    print("Salary Goal Reached")
elif salary >= 50000:
    print("Getting Closer")
else:
    print("Keep Upskilling")

test_cases_executed = 100
test_cases_passed = 95

pass_rate = (test_cases_passed / test_cases_executed) * 100

if pass_rate >= 95:
    print("Release Ready")
else:
    print("Needs More Testing")
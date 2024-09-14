# Challenge 013
# Make a script that reads the wage of an employee and shows their new salary, with 15% of salary increase.

print("If you were getting a salary increase of 15%, which would the final result be? Let's see, tell me your current wage value: ", end='')
wage = float(input(''))
sal_increase = wage * (15/100)
final_sal = wage + sal_increase

print(f"Your salary is U$ {wage:.2f} and it will be U$ {final_sal:.2f} after you raise. Congratulations.")
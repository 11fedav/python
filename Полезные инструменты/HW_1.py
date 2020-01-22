import sys

production, zp_hour, premium = map(float, sys.argv[1:])

print("Зарплата составила: ", format(production * zp_hour + premium))


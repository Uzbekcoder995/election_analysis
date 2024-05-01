print('Hello World!')

counties = ['Arapahoe', 'Denver', 'Jeferson']

if counties['1'] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(f' {county} county has {voters} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county_dict in voting_data:
    print(county_dict['registered_voters'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, votes in counties_dict.items():
    print(f'{county} county has {votes:,} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353}, 
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
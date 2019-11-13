from faker import Faker
import random
from collections import Counter, defaultdict

fake = Faker()

users = [{'id': i, 'name': fake.name(), 'friends': []} for i in range(100)]

ids = [user['id'] for user in users]
friendships = [(random.choice(ids), random.choice(ids)) for i in range(random.randint(10, 1000))]

for i, j in friendships:
    users[i]['friends'].append(users[j]['id'])
    users[j]['friends'].append(users[i]['id'])


def number_of_friends(user):
    return len(user['friends'])


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]


frienships = sorted(num_friends_by_id, key=lambda user: user[1], reverse=True)


def friends_of_a_friend_ids_bad(user):
    return [pk for i in user['friends'] for pk in users[i]['friends']]


def not_friends(user, other_user):
    return all(friend != other_user for friend in user['friends'])


def friends_of_a_friend_ids(user):
    return Counter(pk for i in user['friends'] for pk in users[i]['friends'] if user['id'] != pk and not_friends(user, pk))


interests = [(random.choice(ids), fake.job()) for i in range(140)]


def data_interests(target_interest):
    return [user_id for user_id, interest in interests if interest == target_interest]


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(
        inderested_user_id for interest in interests_by_user_id[user['id']]
        for inderested_user_id in user_ids_by_interest[interest]
        if inderested_user_id != user['id']
    )
# print(most_common_interests_with(users[0]))
# for user in users:
#     print(user)


salaries_and_tenures = [(random.randint(10000, 99999), round(random.uniform(0.1, 10.0), 1)) for i in range(10)]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

avg_salary_by_tenure = {tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less then 2"
    elif tenure < 5:
        return "less then 5"
    else:
        return "more then 5"


salary_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_bucket[bucket].append(salary)

avg_salary_bucket = {tenure_bucket: sum(salaries) / len(salaries) for tenure_bucket, salaries in salary_bucket.items()}


print(avg_salary_bucket)

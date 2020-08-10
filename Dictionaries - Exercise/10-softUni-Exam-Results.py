line = input()

user_lang = {}
user_points = {}
lang_submissions = {}

while line != "exam finished":
    info = line.split("-")
    username = info[0]
    if info[1] == "banned":
        del user_lang[username]

    else:
        language = info[1]
        points = info[2]
        comb = username + "_" + language

        if username not in user_lang:
            user_lang[username] = []

        if username in user_lang and language not in user_lang[username]:
            user_lang[username].append(language)

        if comb not in user_points:
            user_points[comb] = []

        if comb in user_points:
            user_points[comb].append(points)

        if language not in lang_submissions:
            lang_submissions[language] = 0

        if comb in user_points:
            lang_submissions[language] += 1

    line = input()

lang_submissions = dict(sorted(lang_submissions.items(), key=lambda x: x[1], reverse=True))

print(f"Results:")
for k, v in user_lang.items():
    for lang in v:
        new_key = k + "_" + lang
        print(f"{k} | {max(user_points[new_key])}")

print(f"Submissions:")
for k, v in lang_submissions.items():
    print(f"{k} - {v}")

# print(user_lang)
# print(user_points)
# print(lang_submissions)

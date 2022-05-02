# 신고 결과 받기

# def solution(id_list, report, k):
#     return answer

id_list = ['muzi', 'apeach', 'frodo', 'neo']
report = ['muzi frodo','muzi frodo' , 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi']
result = []
report_dict = dict()

for user in id_list:
    report_dict[user] = []

for i in range(len(report)):
    reporter, reported = map(str, report[i].split(' '))
    print(reporter, reported)
    if reported not in report_dict[f'{reporter}']:
        report_dict[reporter].append(reported)

for user in report_dict.items():
    pass
print(report_dict)


# print(solution(id_list, report, 2))

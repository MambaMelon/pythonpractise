data2file = {'2014-11-18': '1', '2014-11-19': '2', '2014-11-20': '3', '2014-11-21': '4',
             '2014-11-22': '5', '2014-11-23': '6', '2014-11-24': '7', '2014-11-25': '8',
             '2014-11-26': '9', '2014-11-27': '10', '2014-11-28': '11', '2014-11-29': '12',
             '2014-11-30': '13', '2014-12-01': '14', '2014-12-02': '15', '2014-12-03': '16',
             '2014-12-04': '17', '2014-12-05': '18', '2014-12-06': '19', '2014-12-07': '20',
             '2014-12-08': '21', '2014-12-09': '22', '2014-12-10': '23', '2014-12-11': '24',
             '2014-12-12': '25', '2014-12-13': '26', '2014-12-14': '27', '2014-12-15': '28',
             '2014-12-16': '29', '2014-12-17': '30', '2014-12-18': '31'}
file_name2file = {}
for (k, v) in data2file.items():
    # file = open('../data/%s.csv' % v, 'w')
    file = open(r'F:\dd\20181108_offline\%s.csv' % v, 'w')
    file_name2file[v] = file

# dataset = open('../data/tianchi_fresh_comp_train_user.csv')
dataset = open(r'F:\dd\20181108_offline\tianchi_fresh_comp_train_user.csv')
dataset.readline()
for line in dataset:
    print(line)
    arr = line.replace('\n', '').split(',')
    file = data2file[arr[-1].split(' ')[0]]
    file_name2file[file].write("%s,%s,%s,%s,%s\n"
                               % (arr[0], arr[1], arr[2], arr[3], arr[4]))

dataset.close()
for (k, v) in file_name2file.items():
    v.close()

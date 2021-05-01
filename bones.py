


coord_test = [778520, 9581875, 1195]

test_count = 0
def test(x):
    global test_count
    test_count += 1
    if x[0] == coord_test[0] and x[1] == coord_test[1] and x[2] == coord_test[2]:
        print(test_count, x)

def test2(x):
    global test_count
    test_count += 1
    if x == coord_test:
        print('found at index {}'.format(test_count), x)

coords_list = [

[778520,9581925,1195],
[778520,9581915,1195],
[778520,9581905,1195],
[778520,9581895,1195],
[778520,9581885,1195],
[778520,9581875,1195],
[778520,9581865,1195]

]

for coords in coords_list:
    test2(coords)




# https://www.leetfree.com/problems/meeting-rooms-ii.html
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

array = [[0, 30],[5, 10],[15, 20]]

def meeting(array):
    dict = {}
    rooms = []
    time, max, min = 0, 0, array[0][0]
    count = len(rooms)
    for a in array:
        dict[a[0]] = a[1]
        if a[0] < min:
            min = a[0]
        if a[1] > max:
            max = a[1]
    while time < max+1:
        if time in dict:
            rooms.append(dict[time])
        if time in rooms:
            for i, item in enumerate(rooms):
                if item == time:
                    rooms.pop(i)
        # print(time, count, rooms)
        if len(rooms) > count:
            count = len(rooms)
        time += 1
    return count

print(meeting(array))

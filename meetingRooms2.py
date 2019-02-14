# https://www.leetfree.com/problems/meeting-rooms-ii.html
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

array = [[0, 30], [15, 20], [2, 40], [5, 10], [5, 10], [0, 10], [35, 35], [0,60],[5, 8],[45, 60], [8, 10], [3, 10]]

# array = [[0, 30], [15, 20], [2, 40], [0, 10], [35, 35], [0,60],[5, 8],[45, 60]]

def meeting(array):

    #dictionary of start keys and an array of end times as the dictionary's values
    dict = {}
    #an array of end times with duplicates. the "unpacked" array of values from the dictionary above
    rooms = []
    #time, max (latest) ending meeting time, min (earliest) starting meeting time
    max, min = 0, array[0][0]
    #the max count of rooms ever used at once
    count = len(rooms)

    #iterate through the array and build the dictionary
    #find the earliest start time and lastest ending time
    for a in array:
        if a[0] not in dict:
            dict[a[0]] = [a[1]]
        else:
            dict[a[0]].append(a[1])
        if a[0] < min:
            min = a[0]
        if a[1] > max:
            max = a[1]

    #time begins when the first meeting does
    time = min

    #while time is less than or equal to the last, ending meeting time
    while time <= max:
    #if the time is a starting time in the dictionary (a key)
        if time in dict:
    #append / unpack all of the ending times for that start time
            for entry in dict[time]:
                rooms.append(entry)
    #if the time is in the rooms array of ending times, the meeting is over!
        if time in rooms:
    #iterate through the array of ending times
    #and append all of the indices of the items that equal the ending time
    #(multiple meetings can end at the same time)
            removeIndices = []
            for i, item in enumerate(rooms):
                if rooms[i] == time:
                    removeIndices.append(i)
    #remove all of these times from the rooms array
    #taking into account the differences of their index as we operate on the array
    #the indices shift as we remove items from the array!
            diff = 0
            for index in removeIndices:
                rooms.pop(index-diff)
                diff+=1
    #find the max count of rooms at a given time.
        if len(rooms) > count:
            count = len(rooms)
    #increment the timestep
        time += 1

    #return the max count of rooms that were used at once. huzzah!
    return count

print(meeting(array))

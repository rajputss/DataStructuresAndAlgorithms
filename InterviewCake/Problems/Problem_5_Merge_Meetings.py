#!/usr/bin/python


def merge_ranges(meetings):
    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    # get current meeting start and end tuple from sorted meeting
    for current_meeting_start, current_meeting_end in sorted_meetings [1:]:
        # assign values from merged meetings to last merged meeting start and end
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        # to assign to merged meetings
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))
    return merged_meetings


a = [(0,1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_ranges(a))
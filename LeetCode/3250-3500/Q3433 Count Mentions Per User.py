from collections import deque
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        n = numberOfUsers
        is_online = [True] * n
        res = [0] * n
        q_offline = deque()
        for event_type, timestamp, message in events:
            while q_offline and q_offline[0][1] <= int(timestamp):
                is_online[q_offline[0][0]] = True
                q_offline.popleft()
            if event_type == 'MESSAGE':
                if message == 'ALL':
                    for i in range(n):
                        res[i] += 1
                elif message == 'HERE':
                    for i in range(n):
                        if is_online[i]:
                            res[i] += 1
                else:
                    user_ids = [int(x) for x in message.replace('id', '').split()]
                    for user_id in user_ids:
                        res[user_id] += 1
            else:
                user_id = int(message)
                is_online[user_id] = False
                q_offline.append([user_id, int(timestamp) + 60])
        return res


s = Solution()
# print(s.countMentions(numberOfUsers=2,
#                       events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]))
# print(s.countMentions(numberOfUsers=2,
#                       events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]))
# print(s.countMentions(numberOfUsers=2, events=[["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]))
print(s.countMentions(numberOfUsers=3,
                      events=[["MESSAGE", "1", "id0 id1"], ["MESSAGE", "5", "id2"], ["MESSAGE", "6", "ALL"],
                              ["OFFLINE", "5", "2"]]))

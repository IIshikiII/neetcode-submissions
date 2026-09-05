class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tmp = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        times = []
        for i in range(len(position)):
            time_to_target = (target - tmp[i][0]) / tmp[i][1]
            if i > 0:
                if time_to_target < times[-1]:
                    time_to_target = times[-1]
            times.append(time_to_target)

        return len(set(times))
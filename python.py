def canJump(nums) :
        ArrayLen = len(nums)
        def singleJump(position, maxJump):
            if position == ArrayLen-1:
                return True
            if position > ArrayLen or maxJump == 0:
                return False
            for i in range(1, maxJump+1):
                print("Position:", position+i,"ArrayLen", ArrayLen-1 , "Max Jump:", nums[position+i])
                if position + i <= ArrayLen-1 and nums[position+i] >= nums[position]:
                    return singleJump(position+i, nums[position+i])
            return False
        return singleJump(0, nums[0])

print(canJump([2,0,0]))
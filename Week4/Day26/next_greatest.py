def next_greater(nums1,nums2):
    result=[]
    for num in nums1:
        found=False
        greater=-1
        for i in range(len(nums2)):
            if nums2[i]==num:
                found=True
            elif found and nums2[i]>num:
                greater=nums2[i]
                break
        result=result+[greater]
    return result
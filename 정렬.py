
#insertion sort
def insertion_sort(arr):
	for end in range(1, len(arr)):
		to_insert = arr[end]
		i = end
		while i>0 and arr[i-1]> to_insert:
			arr[i]=arr[i-1]
			i-=1
		arr[i] = to_insert


#selection sort
def selection_sort(arr):
	for i in range(len(arr)-1):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j

		arr[i], arr[min_idx] = arr[min_idx], arr[i]

#bubble sort
def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap



#merge sort
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


A = [13,43,4,66,7,2]

# insertion_sort(A)
# selection_sort(A)
# bubble_sort(A)
merge_sort(A)
print(A)
def remove_list_element(l:list) -> None:
    for i in l:
        print(i)
        l.remove(i)
    print(l)


remove_list_element([1, 2, 3, 4, 5])

# result: 
# 1
# 3
# 5
# [2, 4]

# for문으로 반복 중인 list를 변형시키면 안된다. 
# for문은 index는 0부터 순차적으로 올라가며 iterable 객체의 index 위치에 저장된 값을 가져온다. 
# list를 변형시키면 element의 index가 계속 바뀌기 때문에 전체 list의 값을 탐색할 수 없다. 
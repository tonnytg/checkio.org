def bigger_price(limit: int, data: list) -> list:
    data2 = []
    b_price = 0
    for i in range(len(data)):
        v_bruto = data[i]
        print(v_bruto)
        if b_price < data[i]["price"]:
            b_price = data[i]["price"]
            data2.insert(0,data[i])

    print(b_price)
    print(data2)





if __name__ == '__main__':
    #from pprint import pprint
    #     # print('Example:')
    bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])
    #
    # # These "asserts" using for self-checking and not for auto-testing
    # assert bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]) == [
    #     {"name": "wine", "price": 138},
    #     {"name": "bread", "price": 100}
    # ], "First"
    #
    # assert bigger_price(1, [
    #     {"name": "pen", "price": 5},
    #     {"name": "whiteboard", "price": 170}
    # ]) == [{"name": "whiteboard", "price": 170}], "Second"
    #
    # print('Done! Looks like it is fine. Go and check it')
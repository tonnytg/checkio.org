def bigger_price(limit: int, data: list) -> list:
    #https://py.checkio.org/mission/bigger-price
    data2 = []
    lista = []
    for i in range(len(data)):
        lista.insert(0,data[i]["price"])
        lista.sort(reverse=True)

    for h in range(limit):
        for j in range(len(data)):
            if lista[h] == data[j]["price"]:
                data2.append(data[j])

    print(data2[:limit])


if __name__ == '__main__':
    bigger_price(2, [
        {"name": "bread", "price": 10},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 25},
        {"name": "water", "price": 15}
    ])
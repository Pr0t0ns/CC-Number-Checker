class Algorithim:
    def Luhn(cc_number):
        weight = "2121212121212121"
        values = []
        index = 0
        for number in cc_number:
            num = int(weight[index])
            index += 1
            product = int(num) * int(number)
            if product >= 10:
                product = str(product)
                product = int(product[0]) + int(product[1])
                if product >= 10:
                    return False
            values.append(product)
        total = 0
        for val in values:
            total += val
        total = str(total)
        if int(total[len(total) - 1]) % 10 == 0:
            return True
        return False
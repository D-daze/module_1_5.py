# module_1_5.py

def main():
    immutable_var = (1, 2, 'a', 'b')
    print("Immutable tuple:", immutable_var)
    try:
        immutable_var[0] = 10
    except TypeError as e:
        print(f"Ошибка: {e}")
        print("Нельзя изменить элементы кортежа, потому что кортежи являются неизменяемыми объектами в Python.")
    mutable_list = [1, 2, 'a', 'b']
    mutable_list[0] = 1
    mutable_list.append('Modified')
    print("Mutable list:", mutable_list)
if __name__ == "__main__":
    main()

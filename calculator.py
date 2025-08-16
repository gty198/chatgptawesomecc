def calculate_hours(total_count, small_boards_per_big_board, time_per_big_board):
    """
    计算所需的总时间（单位：小时）

    参数：
    - total_count: 总数
    - small_boards_per_big_board: 一块大板包含的小板数量
    - time_per_big_board: 生产一块大板所需的时间（单位：秒）

    返回：
    - 总时间（单位：小时）
    """
    result = (total_count / small_boards_per_big_board) * time_per_big_board / 3600
    return result

def main():
    try:
        # 获取用户输入
        total_count = float(input("请输入总数: "))
        small_boards_per_big_board = float(input("请输入一块大板包含的小板数量: "))
        time_per_big_board = float(input("请输入生产一块大板所需的时间（秒）: "))

        # 计算结果
        result = calculate_hours(total_count, small_boards_per_big_board, time_per_big_board)

        # 输出结果
        print(f"所需总时间为: {result:.2f} 小时")
    except ValueError:
        print("请输入有效的数字！")
    except ZeroDivisionError:
        print("每块大板包含的小板数量不能为0！")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
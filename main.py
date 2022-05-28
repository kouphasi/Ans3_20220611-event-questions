def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]



    # ここから記述
    #下から検索する用のインデックス
    lower = 0
    #上から探索する用のインデックス
    higher = len(array) -1

    while True:

        #衝突するまで繰り返す
        if higher - lower > 0:

            #左側が基準値以上で右側が基準値未満のとき
            if array[lower] >= pivot and array[higher] < pivot:
                #代理の変数をおいて、配列内にある要素を入れ替える
                x = array[lower]
                array[lower] = array[higher]
                array[higher] = x

            #左側のみが交換の条件を満たしているとき
            elif array[lower] >= pivot and array[higher] >= pivot:
                higher -=  1
            #右側のみが交換の条件を満たしているとき
            elif array[lower] < pivot  and array[higher] < pivot:
                lower += 1
            #両方とも交換する条件をみたさないとき
            else:
                higher -= 1
                #lower>higherと大小関係が逆転しないよう対策
                if higher == lower:
                    lower += 1

        else:
            break


    #境界にある値が上下どちらの配列に属するかを判別する
    if array[higher] > pivot:
        front_array = array[:higher]
        print(front_array)
        back_array = array[higher:]
        print(back_array)    
    else:
        front_array = array[:higher+1]
        print(front_array)
        back_array = array[higher+1:]
        print(back_array)    
 
    
        
        #再帰を用いている
    return sort(front_array) + sort(back_array)
                    
        



    # ここまで記述



if __name__ == '__main__':
    main()
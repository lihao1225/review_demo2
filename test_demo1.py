class TestMan:

    # def test_demo1(self):
    #     for i in range(5):
    #         for j in range(5-i):
    #             print(' ',end=' ')
    #         for k in range(i*2-1):
    #             print("*",end=' ')
    #         print(" ")
    # def test_demo2(self):
    #     max_num=10
    #     for i in range(1,max_num+1):
    #         for j in range(max_num-i):
    #             print(" ",end=' ')
    #         for k in range(2*i-1):
    #             print("*",end=' ')
    #         print(' ')

    def test_demo2(self):
        ls = [20,4,5,2,89,33]
        # ls.sort()
        # print(ls)
        for i in range(len(ls)-1):
            # print(i)
            for j in range(len(ls)-i-1):
                if ls[j]>ls[j+1]:
                    k = ls[j+1]
                    ls[j+1] = ls[j]
                    ls[j] = k
            print(ls)

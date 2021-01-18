import allure


def handle_black(func):
    def wrapper(*args,**kwargs):
        #局部导入的原因是防止跟basepage页面进行反复调用
        from demo8.page.base_page import BasePage
        #args[0]代表的是basepage中的self
        instance: BasePage = args[0]
        try:
            result = func(*args,**kwargs)
            instance.error_num = 0
            return result
        except Exception as e :
            #截图
            instance.driver.save_screenshot('tmp.png')
            with open('tmp.png') as f:
                content = f.read()
            #出现异常后进行allure截图
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num+=1
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                ele[0].click()
                return wrapper(*args,**kwargs)
            raise e
    return wrapper

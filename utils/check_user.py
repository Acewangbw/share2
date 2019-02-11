from django.shortcuts import render


def check_user(fun):

    print("装饰器验证是否已经登录。。。")
    @function.wraps(fun)
    def wrapper(self, request):
        # 从session获取用户信息
        try:
            user = request.session.get("user")
            return fun(self, request)
        except Exception as e:
            print("获取用户信息失败，用户未登录-------", e)
            return render(request, "login.html")

    return wrapper
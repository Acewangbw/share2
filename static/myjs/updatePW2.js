
$("#jsResetPwdBtn").click(function(){
        alert('start')
        var submit = true;
        var newPwd=$("#pwd").val(); /*新密码1*/
        var newPwd2=$("#repwd").val(); /*新密码2*/

        if(newPwd != newPwd2 ){
            alert('密码不同')
            submit=false;
        }

        if(submit){
            $.ajax({
                type:"post",
                url:"/users/update/pwd/",
                data:$('#jsResetPwdForm').serialize(),
                success:function (data){
                    if(data.status == "success"){  //这里传值错误，需要帮忙看一下。
                        alert('success')
                    }else if(data.status != 0){
                        alert('输入错误请重新输入')
                }
            });
        }

    });

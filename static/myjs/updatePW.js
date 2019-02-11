//个人中心资料修改密码
$(function(){
    //个人资料修改密码
    $('#jsUserResetPwd').on('click', function(){
        Dml.fun.showDialog('#jsResetDialog', '#jsResetPwdTips');
    });

    $('#jsResetPwdBtn').click(function(){

        $.ajax({
            cache: false,
            type: "POST",
            dataType:'json',
            url:"/users/update/pwd/",
            data:$('#jsResetPwdForm').serialize(),
            async: true,
            success: function(data) {
                    if(data.status == "success"){
                    // Dml.fun.showTipsDialog('123')
                    alert('请重新登陆');
                    Dml.fun.showTipsDialog({
                        title:'提交成功',
                        h2:'修改密码成功，请重新登录!',
                    });
                    window.location.href='127.0.0.1:8000';
                    Dml.fun.winReload();
                    // Dml.fun.window.location.href='login.html'
                    // window.location.href='login.html'
                }else if(data.msg){
                    // alert($("#pwd"), data.msg);
                    // alert("#repwd"), data.msg);
                    Dml.fun.showValidateError($("#pwd"), data.msg);
                    Dml.fun.showValidateError($("#repwd"), data.msg);
                }

            }
        });
    });

});
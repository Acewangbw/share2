//顶部搜索栏搜索方法
function search_click(){
    var type = $('#jsSelectOption').attr('data-value'),
        keywords = $('#search_keywords').val(),
        request_url = "/sharefile/filelist?keyword="+keywords;
    if(keywords == ""){
        return
    }
    window.location.href = request_url
}

function bindSave() {

    $('#btnSave').click(function () {
        var postData = {};
        $('#Addmodel').find('input').each(function () {

            var v = $(this).val();
            var n = $(this).attr('image');
            postData[n] = v;
        });

        $.ajax({
            url: '/user/imageupload/',
            type: 'POST',
            data: postData,
            success: function (arg) {
                // arg是字符串
                // JSON.parse将字符串转换成字典， json.loads
                var dict = JSON.parse(arg);
                if (dict.status) {
                    //{#createRow(postData,dict.data);#}
                    //{#$('#addModal').modal('hide');#}
                    window.location.reload();
                } else {
                    $('#errorMsg').text(dict.message);
                }
            }
        })

        /*
        postData = {
             username: 'asdf',
             age:18,
             gender: 1,
             cls_id: 2
        }
         */


    });


}

src="{% static 'node_modules/dropify/dist/js/dropify.min.js' %}"

$(document).ready(function() {
// Basic
$('.dropify').dropify();

// Translated
$('.dropify-fr').dropify({
    messages: {
        default: 'Glissez-déposez un fichier ici ou cliquez',
        replace: 'Glissez-déposez un fichier ou cliquez pour remplacer',
        remove: 'Supprimer',
        error: 'Désolé, le fichier trop volumineux'
    }
});

// Used events
var drEvent = $('#input-file-events').dropify();

drEvent.on('dropify.beforeClear', function(event, element) {
    return confirm("Do you really want to delete \"" + element.file.name + "\" ?");
});

drEvent.on('dropify.afterClear', function(event, element) {
    alert('File deleted');
});

drEvent.on('dropify.errors', function(event, element) {
    console.log('Has Errors');
});

var drDestroy = $('#input-file-to-destroy').dropify();
drDestroy = drDestroy.data('dropify')
$('#toggleDropify').on('click', function(e) {
    e.preventDefault();
    if (drDestroy.isDropified()) {
        drDestroy.destroy();
    } else {
        drDestroy.init();
    }
})
});


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
                    Dml.fun.showTipsDialog({
                        title:'提交成功',
                        h2:'修改密码成功，请重新登录!',
                    });

                    Dml.fun.winReload();
                    // Dml.fun.window.location.href='login.html'
                    // window.location.href='login.html'
                }else if(data.msg){
                    Dml.fun.showValidateError($("#pwd"), data.msg);
                    Dml.fun.showValidateError($("#repwd"), data.msg);
                }

            }
        });
    });

    //个人资料头像
    $('.js-img-up').uploadPreview({ Img: ".js-img-show", Width: 94, Height: 94 ,Callback:function(){
        $('#jsAvatarForm').submit();
    }});


    $('.changeemai_btn').click(function(){
        Dml.fun.showDialog('#jsChangeEmailDialog', '#jsChangePhoneTips' ,'jsChangeEmailTips');
    });
    $('#jsChangeEmailCodeBtn').on('click', function(){
        sendCodeChangeEmail($(this));
    });
    $('#jsChangeEmailBtn').on('click', function(){
        changeEmailSubmit($(this));
    });


    //input获得焦点样式
    $('.perinform input[type=text]').focus(function(){
        $(this).parent('li').addClass('focus');
    });
    $('.perinform input[type=text]').blur(function(){
        $(this).parent('li').removeClass('focus');
    });

    laydate({
        elem: '#birth_day',
        format: 'YYYY-MM-DD',
        max: laydate.now()
    });

    verify(
        [
            {id: '#nick_name', tips: Dml.Msg.epNickName, require: true}
        ]
    );
    //保存个人资料
    $('#jsEditUserBtn').on('click', function(){
        var _self = $(this),
            $jsEditUserForm = $('#jsEditUserForm')
            verify = verifySubmit(
            [
                {id: '#nick_name', tips: Dml.Msg.epNickName, require: true}
            ]
        );
        if(!verify){
           return;
        }
        $.ajax({
            cache: false,
            type: 'post',
            dataType:'json',
            url:"/users/info/",
            data:$jsEditUserForm.serialize(),
            async: true,
            beforeSend:function(XMLHttpRequest){
                _self.val("保存中...");
                _self.attr('disabled',true);
            },
            success: function(data) {
                if(data.nick_name){
                    _showValidateError($('#nick_name'), data.nick_name);
                }else if(data.birday){
                   _showValidateError($('#birth_day'), data.birday);
                }else if(data.address){
                   _showValidateError($('#address'), data.address);
                }else if(data.status == "failure"){
                     Dml.fun.showTipsDialog({
                        title: '保存失败',
                        h2: data.msg
                    });
                }else if(data.status == "success"){
                    Dml.fun.showTipsDialog({
                        title: '保存成功',
                        h2: '个人信息修改成功！'
                    });
                    setTimeout(function(){window.location.href = window.location.href;},1500);
                }
            },
            complete: function(XMLHttpRequest){
                _self.val("保存");
                _self.removeAttr("disabled");
            }
        });
    });


});

<!-- bt-switch -->
src="{% static 'node_modules/bootstrap-switch/bootstrap-switch.min.js' %}"

$(".bt-switch input[type='checkbox'], .bt-switch input[type='radio']").bootstrapSwitch();
var radioswitch = function() {
    var bt = function() {
        $(".radio-switch").on("switch-change", function() {
            $(".radio-switch").bootstrapSwitch("toggleRadioState")
        }), $(".radio-switch").on("switch-change", function() {
            $(".radio-switch").bootstrapSwitch("toggleRadioStateAllowUncheck")
        }), $(".radio-switch").on("switch-change", function() {
            $(".radio-switch").bootstrapSwitch("toggleRadioStateAllowUncheck", !1)
        })
    };
    return {
        init: function() {
            bt()
        }
    }
}();
$(document).ready(function() {
    radioswitch.init()
});

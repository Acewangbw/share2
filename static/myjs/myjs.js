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



$(function () {
    bindSave();
});

//上传头像用的弹出窗口，用于保存提交。
    function bindSave() {

        $('#btnSave').click(function () {

            var postData = {};
            $('#Addmodel').find('input').each(function () {
                var v = $(this).val();
                var n = $(this).attr('name');
                // postData={"url":v};
                postData[n] = v;
            });
            alert(JSON.stringify(postData));
            $.ajax({
                url: '/users/imageupload/',
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

//上传头像用的 上传 js
// src="{% static 'node_modules/dropify/dist/js/dropify.min.js' %}"
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






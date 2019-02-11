$(function () {
    approveprocess();
});

//上传头像用的弹出窗口，用于保存提交。
    function approveprocess() {

        $('button[target="summbit"]').click(function (e) {

            var postData = {};
            var nid = $("#form_data").attr("name");
            var is_review = $(this).attr("name");
            postData['nid'] = nid;
            postData['is_review'] = is_review;
            console.log(nid);
            $("input[name='keyword']").each(function () {
                var v = $(this).val();
                var n = $(this).attr('name');
                console.log("v",v);
                if(v){
                    postData[n] = v;
                }
                // postData={"url":v};

            });




            console.log("postdata", postData);
            alert(JSON.stringify(postData));
            $.ajax({
                url: '/sharefile/filedetail/', //需要更根据写的view对应的URL修改
                type: 'POST',
                data: postData,
                success: function (arg) {
                    // arg是字符串
                    // JSON.parse将字符串转换成字典， json.loads
                    var dict = JSON.parse(arg);
                    if (dict.status) {
                        //{#createRow(postData,dict.data);#}
                        //{#$('#addModal').modal('hide');#}
                        alert('审批完成了')
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


    <script>
        $(function () {
            bindEvent();
            bindSave();
            bindDel();
            bindDelConfirm();
        });

        function bindEvent() {
            $('#addBtn').click(function () {
                $('#myModal').modal('show');
            })
        }

        function bindSave() {

            $('#btnSave').click(function () {
                var postData = {};
                $('#Addmodel').find('input').each(function () {

                    var v = $(this).val();
                    var n = $(this).attr('name');
                    postData[n] = v;
                });

                $.ajax({
                    url: '/add_keyword/',
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

        function bindDelConfirm() {
            $('#delConfirm').click(function () {
                console.log(this)

            })
            $('#delConfirm1').click(function () {
                var keywordid = $('#delNid').val();
                console.log(keywordid);

                $.ajax({
                    url: '/del_keyword/',
                    type: 'GET',
                    data: {'nid': keywordid},
                    success: function (arg) {
                        var dict = JSON.parse(arg);
                        if (dict.status) {
                            $('li[nid="' + keywordid + '"]').remove();
                        }
                        {#$('#delModal').modal('hide');#}
                    }
                });

            });
        }

        function bindDel() {
            $('.del-row').click(function () {
                {#$('#delModal').modal('show');#}
                // 回去当前行的ID
                var keywordid = $(this).attr('nid');
                {#console.log(keywordid);#}
                $('#delNid').val(keywordid);
            })
        }

    </script>

    <script type="text/javascript">
        {#<script language="javascript">#}

        function p_del() {
            var msg = "您真的确定要删除吗？";
            if (confirm(msg) == true) {
                return true;
            } else {
                return false;
            }
        }

        function post(params) {
            var temp = document.createElement("form"); //创建form表单
            console.log(this);
            {#temp.action = url;#}
            temp.method = "post";
            temp.style.display = "none";//表单样式为隐藏
            for (var item in params) {//初始化表单内部的控件
                //根据实际情况创建不同的标签元素
                var opt = document.createElement("input");  //添加input标签
                opt.type = "text";   //类型为text
                opt.id = item;      //设置id属性
                opt.name = item;    //设置name属性
                opt.value = params[item];   //设置value属性
                temp.appendChild(opt);
            }

            document.body.appendChild(temp);
            temp.submit();
            return temp;
        }

    </script>


$(function () {
    bindDelConfirm();
});
    function bindDelConfirm() {
        $('#delConfirm').click(function () {
            var rowId = $('#delNid').val();
            // console.log(rowId);
            alert(rowId);

            $.ajax({
                url: '/sharefile/delete_file/',
                type: 'GET',
                data: {'nid': rowId},
                success:function (arg) {
                    var dict = JSON.parse(arg);
                    if(dict.status){
                        $('tr[nid="'+ rowId+'"]').remove();
                    }
                    $('#delModal').modal('hide');
                }
            })

        });


    }
    function bindDel() {
        $('.del-row').click(function () {
            $('#delModal').modal('show');
            // 回去当前行的ID
            var rowId = $(this).parent().parent().attr('nid');
            $('#delNid').val(rowId);
        })
    }
    function bindEvent() {
        $('#addBtn').click(function () {
            $('#addModal').modal('show');
        })
    }
    function bindSave() {

        $('#btnSave').click(function () {
            var postData = {};
            $('#addModal').find('input,select').each(function () {
                var v = $(this).val();
                var n = $(this).attr('name');
                if(n=='gender'){
                    if($(this).prop('checked')){
                        postData[n] = v;
                    }
                }else{
                    postData[n] = v;
                }
            });

            /*
            postData = {
                 username: 'asdf',
                 age:18,
                 gender: 1,
                 cls_id: 2
            }
             */

            $.ajax({
                url: '/add_student/',
                type: 'POST',
                data: postData,
                success:function (arg) {
                    // arg是字符串
                    // JSON.parse将字符串转换成字典， json.loads
                    var dict = JSON.parse(arg);
                    if(dict.status){
                        /*
                        postData = {
                             username: 'asdf',
                             age:18,
                             gender: 1,
                             cls_id: 2
                        }
                        自增id  = dict.data
                         */
                        createRow(postData,dict.data);
                        $('#addModal').modal('hide');
                        // window.location.reload();
                    }else {
                        $('#errorMsg').text(dict.message);
                    }
                }
            })

        });
        

    }
    function  createRow(postData,nid) {
        var tr = document.createElement('tr');

        var tdId = document.createElement('td');
        tdId.innerHTML = nid;
        $(tr).append(tdId);

        var tdUser = document.createElement('td');
        tdUser.innerHTML = postData.name;
        $(tr).append(tdUser);

        {#var tdAge = document.createElement('td');#}
        {#tdAge.innerHTML = postData.age;#}
        {#$(tr).append(tdAge);#}




        var tdClass = document.createElement('td');
        var text = $('select[name="cls_id"]').find('option[value="'+ postData.cls_id +'"]').text();
        tdClass.innerHTML = text;
        $(tr).append(tdClass);

        var tdHandle = '<td> <a class="glyphicon glyphicon-remove icon"></a><a class="fa fa-pencil-square-o icon"></a> </td>';
        $(tr).append(tdHandle);

        $('#tb').append(tr);
    }

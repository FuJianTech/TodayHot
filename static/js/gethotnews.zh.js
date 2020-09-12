  $(document).ready(function () {
      var number;
      var clickCount = 0; //记录鼠标点击次数
      var infoList = new Array();
      $.ajax({
          type: "GET",
          url: "/hot/get_zhihu_hot",
          async: false,
          success: function (result) {
                  resultObj = JSON.parse(result['data']);
                  for (var k in resultObj) {
                      infoList.push(resultObj[k]);
                  }

              },
              error: function (e) {
                  console.log(e.status);
                  console.log(e.responseText);
              }
      });

      $("#addData1").empty();
      for (var i = infoList.length; i >= 0; i--) {
          number = i + 1
          if (infoList[i] != undefined) {
              $("#addData1").prepend('<tr><td><a class="" href="#" target="_blank" title="' + infoList[i] + '"><small class="font-weight-normal text-success">' + number + '，' + infoList[i] + '</small></a></td></tr>');
          }
      }

  });
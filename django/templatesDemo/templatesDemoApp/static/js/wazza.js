console.log('testing 12')
$(document).ready(function(){
    console.log("in the document.ready")
    $(".btn1").click(function(){
      $(".tbl").hide();
    });
    $(".btn2").click(function(){
      $(".tbl").show();
    });
  });
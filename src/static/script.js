$(document).ready(function(){
    $("#complexity").click(function(){
      $("#api_response").load('/complexity');
    });
  });

  $(document).ready(function(){
    $("#mine_new_block").click(function(){
      $("#api_response").load('/mine_block');
    });
  });

  $(document).ready(function(){
    $("#get_nodes").click(function(){
      $("#api_response").load('/get_nodes');
    });
  });

  $(document).ready(function(){
    $("#replace_chain").click(function(){
      $("#api_response").load('/replace_chain');
    });
  });

  $(document).ready(function(){
    $("#set_complexity").click(function(){
      $("#api_response").load('/complexity/' + $("#complexity_input").val());
    });
  });

  $(document).ready(function(){
    $("#validate_chain").click(function(){
      $("#api_response").load('/validate');
    });
  });

  $(document).ready(function(){
    $("#add_transaction").click(function(){
        $.ajax({
            type: 'POST',
            url: '/add_transaction',
            data: JSON.stringify ({sender: $("#sender").val(), receiver:$("#receiver").val(), amount: $("#amount").val()}),
            success: function(data) { 
              $("#api_response").text('Transaction will be added to the next block: ' + 
              JSON.stringify ({
                sender: $("#sender").val(), 
                receiver:$("#receiver").val(), 
                amount: $("#amount").val()}));   
            },
            contentType: "application/json",
            dataType: 'json'
        });
    });
  });

  $(document).ready(function(){
    $("#refresh_blockchain").click(function(){
      location.reload();
    });
  });
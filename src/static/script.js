$(document).ready(function(){
    $("#complexity").click(function(){
      $("#complex_value").load('/complexity');
    });
  });

  $(document).ready(function(){
    $("#mine_new_block").click(function(){
      $("#new_block_alert").load('/mine_block');
    });
  });

  $(document).ready(function(){
    $("#get_nodes").click(function(){
      $("#get_nodes_reponse").load('/get_nodes');
    });
  });

  $(document).ready(function(){
    $("#replace_chain").click(function(){
      $("#replace_chain_reponse").load('/replace_chain');
    });
  });

  $(document).ready(function(){
    $("#set_complexity").click(function(){
      $("#new_complex_value").load('/complexity/' + $("#complexity_input").val());
    });
  });

  $(document).ready(function(){
    $("#validate_chain").click(function(){
      $("#validate_chain_reponse").load('/validate');
    });
  });

  $(document).ready(function(){
    $("#add_transaction").click(function(){
        $.ajax({
            type: 'POST',
            url: '/add_transaction',
            data: JSON.stringify ({sender: $("#sender").val(), receiver:$("#receiver").val(), amount: $("#amount").val()}),
            success: function(data) { 
              $("#transaction_alert").text('Transaction will be added to the next block: ' + 
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
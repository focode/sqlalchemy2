$(
	function(){
		// Get a reference to the content div (into which we will load content).
		var jContent = $( "#message" );
						
		// Hook up link click events to load content.
		$( "#submit" ).click(
			function( objEvent ){
				var jLink = $( this );
				
				// Clear status list.
				$( "#ajax-status" ).empty();
				
				// Launch AJAX request.
				$.ajax(
					{
						// The link we are accessing.
						url: '/milkprofileForm',
						
						data: $('form').serialize(),
						
						// The type of request.
						type: "post",
						
						// The type of data that is getting returned.
						dataType: "html",
						
						error: function(val1,val2,val3){
							console.log(val3);
							
							// Load the content in to the page.
							jContent.html( "<p>Page Not Found!!</p>" );
						},
						
						beforeSend: function(){
							console.log("beforeSend");
						},
						
						complete: function(){
							console.log("complete");						},
						
						success: function( strData ){
										
							// Load the content in to the page.
							console.log(strData);
							jContent.html( strData );
							
						}
					}							
					);
				
				// Prevent default click.
				return( false );					
			}
			);
		
	}
	);
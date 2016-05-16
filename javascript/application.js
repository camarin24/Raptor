$( "#btn_search" ).click(function() {
	$.ajax({
			data: {query:$("#txt_query").val()},
			type: "POST",
			url: "http://104.214.34.46:1885/raptor/post/track",
		})
	 .done(function( data, textStatus, jqXHR ) {
	 		console.log(data);
	 		data = (jQuery.parseJSON(data)['data']['data']);
	 		console.log(data);
	 		var lon = data.length;
	 		if (lon === 0) {
	 			return toastr.error('No se han encontrado resultados para tu búsqueda.')
	 		}
	 		var template = '';
	 		for (var i = 0; i < lon; i++) {
	 			template += '<div class="row">';
 				template += '<div class="col-md-1">\
								<img src="'+data[i]['album']['cover_big']+'" width="80" alt="">\
							</div>\
							<div class="col-md 3">\
								<span><b>'+data[i]['title']+'</b></span><br>\
								<span>'+data[i]['album']['title']+'</span>\
								<p class="text-muted"><em>'+data[i]['artist']['name']+'</em></p>\
							</div>';
				template += '</div>';
 			}
			$("#div_ini").hide();
			$("#div_result").show();	
 			$("#div_result")[0].innerHTML = template;	 			
	 })
	  .fail(function( jqXHR, textStatus, errorThrown ) {
		    console.log(jqXHR);
	});
});
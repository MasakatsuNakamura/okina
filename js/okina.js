$(document).on("pagebeforeshow", "#kantei", function () {
	var sei = $("#sei").val();
	var mei = $("#mei").val();
	var sex = $("#sex").val();
	var marry = $("#marry").val();
	$.ajax({
		type: "POST",
		url: "php/index.php",
		data: 'sei=' + sei + '&mei=' + mei + '&sex=' + sex + '&marry=' + marry,
		success: function (json) {
			if (json) {
				$("#kantei-content").html(json['content']);
				$("#kantei-header").html(json['header']);
			}
		}
	});
});

function kantei(sei, mei, sex, marry) {
	$.ajax({
		type: "POST",
		url: "php/index.php",
		data: 'sei=' + sei + '&mei=' + mei + '&sex=' + sex + '&marry=' + marry,
		success: function (json) {
			if (json) {
				$("#kantei-content").html(json['content']);
				$("#kantei-header").html(json['header']);
			}
		}
	});
	location.href = '#kantei';
}
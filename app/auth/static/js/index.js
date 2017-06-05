// JavaScript Document
$(function(){
	//完整菜单效果1
		$(".menu_list").hide();
		$(".menu_list_first").show();
		$(".a_list").click(function(){
			var len = $('.a_list').length;
			var index = $(".a_list").index(this);
			for(var i=0;i<len;i++){
				if(i == index){
					$('.menu_list').eq(i).slideToggle(300);
					}else{
						$('.menu_list').eq(i).slideUp(300);
					}
				}
			});
		//完整菜单效果2
		/*$(".a_list").each(function(l){
			$(this).click(function(){
				var len = $('.a_list').length;
				for(var i=0;i<len;i++){
					if(i == l){
						$('.menu_list').eq(i).slideToggle(100);
					}else
					{
						$('.menu_list').eq(i).slideUp(100);
					}
				}
			})	
		})*/
	})
	
	//点击显示隐藏完成菜单和简洁菜单
	$(function(){
		$(".menu-oc").click(function(){
			$(".leftmenu1").animate({left:"-292px"})	;
			$(".leftmenu2").animate({left:"0px"})
			$(".rightcon").css("margin-left","52px")
		})
		$(".menu-oc1").click(function(){
			$(".leftmenu1").animate({left:"0px"})	;
			$(".leftmenu2").animate({left:"-192px"});
			$(".rightcon").css("margin-left","240px");
		})		
	})
	
	//简洁菜单点击效果
	/*
	$(function(){
		$(".j_menu_list").hide();
		$(".j_a_list").click(function(){
			var len = $('.j_a_list').length;
			var index = $(".j_a_list").index(this);
			for(var i=0;i<len;i++){
				if(i == index){
					$('.j_menu_list').eq(i).slideToggle(300);
					}else{
						$('.j_menu_list').eq(i).slideUp(300);
					}
				}
		});
		$(".j_menu_list>span>i").click(function(){
			$(".j_menu_list").slideUp(300)	
		})
	})*/
	//简洁菜单移动效果
	$(function(){
		$(".j_menu_list").hide();
		$(".j_a_list").hover(function(){
			$(".leftmenu2 ul li").hover(function(){
				$(this).find('.j_menu_list').show();	
			},function(){
				$(this).find('.j_menu_list').hide();
			});
		})
	})
	
	
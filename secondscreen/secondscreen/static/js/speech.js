/*
 Modified from http://bl.ocks.org/mbostock/1098617
*/

function timeDiff(a,b){
	return ((b.getMinutes() - a.getMinutes())*60) + b.getSeconds() - a.getSeconds()
}

function Timer(countdown,obj){
	var that = this;
	this.obj = obj;
	this.countdown = countdown;
	this.start = new Date();
	this.intervalId = 0;
	this.now = new Date();

	this.arcTween = function(b){
		var arc = d3.svg.arc()
		    .innerRadius(0)
		    .outerRadius(15)
		    .startAngle(0)
		    .endAngle(function(d) { 
		    	if(d.value > countdown){
		    		clearInterval(that.intervalId);
		    		$(that.obj).find("g").remove();
		    		return 2 * Math.PI
		    	}
				else if(d.value > 0){
			    	return ((d.value/d.size) * 2 * Math.PI);
				}else{
					return 0;
				}
			})
	  	var i = d3.interpolate({value: b.previous}, b);
	  	return function(t) {
	    	return arc(i(t));
	  	};	
	}

	this.activate = new function(){
		var w = 100,
		    h = 100,
		    x = d3.scale.ordinal().domain(d3.range(3)).rangePoints([0, w], 2);
		var fields = [
		  {name: "seconds", value: 0, size: that.countdown}
		];
		var svg = d3.select(obj)
		    .attr("width", w)
		    .attr("height", h)
		.append("svg:g")
		    .attr("transform", "translate(-10,15)");

		that.intervalId = setInterval(function() {
		  that.now = new Date();


		  fields[0].previous = fields[0].value; 
		  fields[0].value = timeDiff(that.start,that.now);


		  var path = svg.selectAll("path")
		      .data(fields.filter(function(d) { return d.value; }), function(d) { return d.name; });

		  path.enter().append("svg:path")
		      .attr("transform", function(d, i) { return "translate(" + x(i) + ",0)"; })
		    .transition()
		      .ease("elastic")
		      .duration(750)
		      .attrTween("d", that.arcTween);

		  path.transition()
		      .ease("elastic")
		      .duration(750)
		      .attrTween("d", that.arcTween);

		}, 100);
	}
}

$(".red,.blue,.inhib").click(function(){
	time = new Timer(300,this);
})
$("#dragon").click(function(){
	time = new Timer(360,this);
})
$("#baron").click(function(){
	time = new Timer(420,this);
})
// $(".ward").click(function(){
// 	time = new Timer(180,this);
// })
$(".ward").draggable({
  stop: function( event, ui ) {

	$(this).draggable( "disable" );
	//colour in css
	var exit_button = $("<svg class='exit' >"+
	"<g xmlns='http://www.w3.org/2000/svg' fill='black' id='layer1' transform='translate(25,25) scale(0.1)' >"+
   		"<path stroke-width='0.25pt' id='path4950' d='m100,60l-40,40l170,170l40,-40l-170,-170z'/>"+
   		"<path stroke-width='0.25pt' id='path4952' d='m60,230l170,-170l40,40l-170,170l-40,-40z'/>"+
  	"</g></svg>");
	$(this).append(exit_button);
	time = new Timer(180,this);
	//TODO: make the timer circle fit the ward shape

	exit_button.click(function(){
		$(".pink").append($(this).parent());
		$(this).parent().draggable( "enable" );
		$(this).parent().removeAttr( 'style' );
		$(this).remove();
	});

  }
});
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

	this.activate = new function(){

		var w = 100,
		    h = 100,
		    x = d3.scale.ordinal().domain(d3.range(3)).rangePoints([0, w], 2);
		var fields = [
		  {name: "seconds", value: 0, size: countdown}
		];
		var svg = d3.select(obj)
		    .attr("width", w)
		    .attr("height", h)
		.append("svg:g")
		    .attr("transform", "translate(-10,15)");

		intervalId = setInterval(function() {
		  now = new Date();

		  fields[0].previous = fields[0].value; 
		  fields[0].value = timeDiff(start,now);

		  var path = svg.selectAll("path")
		      .data(fields.filter(function(d) { return d.value; }), function(d) { return d.name; });

		  path.enter().append("svg:path")
		      .attr("transform", function(d, i) { return "translate(" + x(i) + ",0)"; })
		    .transition()
		      .ease("elastic")
		      .duration(750)
		      .attrTween("d", arcTween);

		  path.transition()
		      .ease("elastic")
		      .duration(750)
		      .attrTween("d", arcTween);

		}, 1000);
	}
	this.arcTween = function(b){
		var arc = d3.svg.arc()
		    .innerRadius(0)
		    .outerRadius(15)
		    .startAngle(0)
		    .endAngle(function(d) { 
		    	if(d.value > countdown){
		    		clearInterval(intervalId);
		    		console.log(this)
		    		$("g").remove();
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
}

$("svg").click(function(){
	time = new Timer(10,this);
})

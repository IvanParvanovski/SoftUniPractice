$(document).ready(function(){
    var width = 960;
      height = 538;
      var numberOfBlinds = 22;
      var margin = 4;
      var color = '#fff';
    gapHeight = 100;
  
      var container = $('#container');
  
      container.width(width).height(height);
      var blindWidth = width / numberOfBlinds;
  
    images = new Array();
      $('ul li', container).each(function() {
      images.push($(this)); 
    });
  
    images[0].addClass('active');
    activeImage = 0;
  
    for (var i = 0; i < numberOfBlinds; i++) {
      var tempEl = $(document.createElement('span'));
      var borders = calculateBorders();
  
      tempEl.css({
        'left': i * blindWidth,
        border: margin + 'px solid ' + color,
        borderTop: borders.borderWidthTop + 'px solid ' + color,
        borderBottom: borders.borderWidthBottom + 'px solid ' + color,
        'height': height,
        'width': blindWidth
      });
                  
      container.prepend(tempEl);
    };
  
    blinds = $('span', container);
    setTimeout(animateBorders, 1000);
  });
  
  function calculateBorders() {
    var random = Math.floor((Math.random()*9)+1);
    var borderWidthTop = (random / 10) * gapHeight;
    var borderWidthBottom = gapHeight - borderWidthTop;
  
    return {borderWidthTop: borderWidthTop, borderWidthBottom: borderWidthBottom};
  }
  
  function animateBorders() {
    var changeOccuredOnce = false;
  
    blinds.animate({
      borderTopWidth: height / 2,
      borderBottomWidth: height / 2
    }, 1000, function() {
      if(!changeOccuredOnce) {
        images[activeImage].removeClass('active');
        activeImage = (activeImage + 1) % images.length;
        images[activeImage].addClass('active');
        setTimeout(animateBorders, 3000);
        changeOccuredOnce = true;
      }
  
      var borders = calculateBorders();
  
      $(this).delay(300).animate({
        borderTopWidth: borders.borderWidthTop,
        borderBottomWidth: borders.borderWidthBottom
      }, 1000);
    });
  }
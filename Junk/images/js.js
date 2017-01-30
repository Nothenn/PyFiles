//variable that will increment through the images
var stage = 0
//Makes the function know what images have been through the slideshow, and what to select next
var imgno = 0

function slider(){
 //if browser does not support the image object, exit.
 if (!document.images)
  return
 document.getElementById('workSlide').src = images[stage].src
 //Finds the element in the HTML and sets it so that element changes the images source through the function
 imgno = stage
 //Makes the amount of steps = to the number of the image
 if (stage<5) //Checks if the variable is lower than five which is the final image in the array
  stage++ //Increments the variable by one, increases 
 else
  stage=0
  //Resets the stage when the parameter goes over the amount of images there are
 setTimeout("slider()",2500)
 //call function "slider()" every 2.5 seconds
}


window.onload=slider; //Loads the function when the window loads

//End of New Function


//Function for the slideshow

var i = 0; //Sets a variable that is an increment
var path = new Array(); //Sets up an array for the images

var pictures = new Array();
for(var x=1; x<51; x++ ) {
  pictures[x-1] = "images/"+x+".jpg";
}

path[0] = "images/link1.jpg"; //Sets the first image of the array
path[1] = "images/link2.jpg"; //Sets the second image of the array
path[2] = "images/link3.jpg"; //Sets the third image of the array

function swapImage() { //Makes the function for the slideshow on the work page
	document.workSlide.src = pictures[i]; //Selects the element from the HTML and sets the image to the picture in the array
		if(i < pictures.length) //Checks if the increment variable is smaller than the last image
			i++; //Adds one to the variable
			else i = 0; //When the if isnt meant it cycles to the beggining
			setTimeout("swapImage()",2000); //Sets how long between slides
}






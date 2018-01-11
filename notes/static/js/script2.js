 //notes id:text
var idCount=1; //autoincremental id for notes

//activate first note on start
(function(){
    tabcontent = document.getElementsByClassName("tabcontent");   
    tablinks = document.getElementsByClassName("tablinks");
    tablinks[0].className += " active";

    
})();

//select and open clicked note
function openNote(evt) {
    var tablinks = document.getElementsByClassName("tablinks");    

    //deactivate tablink that is currently active, if there is one
    var activeTablinkID;
    try {
        activeTablinkID = document.getElementsByClassName('tablinks active')[0].id;
        tablinks[activeTablinkID].className = tablinks[activeTablinkID].className.replace(" active", "");
    }
    catch(err) {
        
    }    

    //activate clicked tablink
    evt.currentTarget.className += " active";

    //load text for current tab
    activeTablinkID = evt.currentTarget.id;
}
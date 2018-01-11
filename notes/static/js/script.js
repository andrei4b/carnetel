var notes = {0: "text for note 0"}; //notes id:text
var idCount=1; //autoincremental id for notes

//activate first note on start
(function(){
    tabcontent = document.getElementsByClassName("tabcontent");   
    tablinks = document.getElementsByClassName("tablinks");
    tablinks[0].className += " active";
    document.getElementById('textbox').value = notes[0];
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
    document.getElementById('textbox').value = notes[activeTablinkID];
}

function saveNote() {
    var activeTablinkID;
    //save note in array notes
    activeTablinkID = document.getElementsByClassName('tablinks active')[0].id;
    notes[activeTablinkID] = document.getElementById('textbox').value;
}

function deleteNote() {
    activeTablink = document.getElementsByClassName('tablinks active')[0];
    var tab = document.getElementsByClassName("tab")[0];
    tab.removeChild(activeTablink);
    noteID = activeTablink.id;
    delete notes[noteID];
    document.getElementById('textbox').value = "";

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
}

function createNote() {
    var btn = document.createElement("BUTTON");
    var title = prompt("Please enter note title:", "");
    var t = document.createTextNode(title);
    btn.appendChild(t);  
    btn.className = "tablinks";
    btn.onclick = function() {openNote(event, 1)};
    btn.id = idCount;
    notes[idCount] = "Enter text here";
    idCount++;

    var tab = document.getElementsByClassName("tab")[0];
    tab.appendChild(btn);

}
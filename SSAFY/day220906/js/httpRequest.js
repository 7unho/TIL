function viewTime(){
    if(httpRequest.readyState == 4){
        if(httpRequest.status == 200){
            var time = httpRequest.responseText;
            var div = document.getElementById("curtime");
            div.setAttribute("class", "viewtime");
            div.innerHTML = time;
        }
    }
}

window.onload = function(){
    setInterval(getTime, 1000);
};

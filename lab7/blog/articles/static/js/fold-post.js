var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var parentElement = this.parentElement.parentElement;
        
        if (this.className == "fold-button folded") {
            this.innerHTML = "свернуть"; 
            this.className = "fold-button"; 
            parentElement.classList.remove("folded");
        }
        else {
            this.innerHTML = "развернуть"; 
            this.className = "fold-button folded"; 
            parentElement.classList.add("folded");
        }
    });
}
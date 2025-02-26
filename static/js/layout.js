document.querySelector(".scroll-container").addEventListener("scroll", function() {
    let scrollTop = this.scrollTop;
    let scrollHeight = this.scrollHeight - this.clientHeight;
    let scrollPercentage = (scrollTop / scrollHeight) * 100;
    document.querySelector(".scroll-indicator").style.width = scrollPercentage + "%";
  });
  
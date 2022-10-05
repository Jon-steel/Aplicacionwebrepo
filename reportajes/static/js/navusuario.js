let wrapper = document.querySelector("#wrapper");
let closeBtn = document.querySelector("#sidebarToggle");

closeBtn.addEventListener("click", ()=>{
  wrapper.classList.toggle("open");
});

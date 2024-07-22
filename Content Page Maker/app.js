list = document.querySelectorAll(".packages-card__prices .prices del");
for (let i = 0; i < list.length; i++) {
  const item = list[i];
  console.log("'" + item.innerHTML + "'" + ",");
}
